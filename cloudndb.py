from google.cloud import ndb

VERSION = 'cloud-ndb'

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
  client = ndb.Client()
  with client.context():
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
  client = ndb.Client()
  with client.context():
    thread = get_or_create_thread()
    number = len(thread.messages) + 1
    message = ThreadMessage(number=number, text=text)
    thread.messages.append(message)
    thread.put()
