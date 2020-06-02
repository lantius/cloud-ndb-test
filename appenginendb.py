# import subprocess
# import sys
# from requests import post
VERSION = 'appengine-ndb'

# def init_appengine():
#   # default appengine path.
#   appengine_path = subprocess.check_output([
#       'bash', '-c',
#       'echo $(gcloud info --format="value(installation.sdk_root)")/platform/google_appengine'
#   ])
#   appengine_path = appengine_path.strip()
#   sys.path.insert(0, appengine_path)
#   try:
#     import dev_appserver
#   except ImportError:
#     print("ImportError importing dev_appserver. Check appengine_path.")
#     sys.exit(1)
#   dev_appserver.fix_sys_path()
# init_appengine()

from google.appengine.ext import ndb
# context = ndb.get_context()
# context.set_cache_policy(False)
# context.set_memcache_policy(False)


class ThreadMessage(ndb.Model):
  """Models the individual messages in a thread."""
  number = ndb.IntegerProperty(indexed=True)
  created_by = ndb.StringProperty(default=VERSION)
  text = ndb.TextProperty()
  created = ndb.DateTimeProperty(auto_now=True, indexed=True)


class Thread(ndb.Model):
  """Models a thread of messages."""
  created_by = ndb.StringProperty()
  messages = ndb.LocalStructuredProperty(ThreadMessage,
                                         repeated=True,
                                         compressed=True)


def get_or_create_thread():
  thread = Thread.query().get()
  if not thread:
    thread = Thread(created_by=VERSION)
    thread.put()
  return thread


def read_thread():
  thread = get_or_create_thread()
  resp = ""
  if thread.messages:
    for message in thread.messages:
      resp += ("#%s: Created in: %s || Text: %s\n" %
            (message.number, message.created_by, message.text))
  else:
    resp += "No thread messages found."
  return resp

def write_to_thread(text):
  thread = get_or_create_thread()
  number = len(thread.messages) + 1
  message = ThreadMessage(number=number, text=text)
  thread.messages.append(message)
  thread.put()


def reset_datastore():
  post("http://localhost:8089/reset")
  print("Resetting datastore!")


if __name__ == '__main__':
  response = 0
  while response != 4:
    print("Choose action:")
    print("1. Read current messages")
    print("2. Write a new message")
    print("3. Reset datastore")
    print("4. Quit")
    response = input("Action to take: ")

    if response == 1:
      read_thread()
    elif response == 2:
      text = raw_input("What message to write?: ")
      write_to_thread(text)
    elif response == 3:
      reset_datastore()
    print("")
