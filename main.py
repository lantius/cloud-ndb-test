import webapp2

# This is necessary due to an issue with dev_appserver.
# Please see https://github.com/googleapis/python-ndb/issues/249 for more info.
# pylint: disable=wrong-import-position
import six
reload(six)

from appenginendb import read_thread, write_to_thread
#from cloudndb import read_thread, write_to_thread

class Main(webapp2.RequestHandler):
  def get(self):
    self.response.write(
      '<html><body><pre>' +
        read_thread() +
      '</pre><p><form method="post">' +
      '<input type=text" name="text"><input type="submit">' +
      '</form></p></body></html>'
    )

  def post(self):
    text = self.request.get("text")
    write_to_thread(text)
    self.redirect('/')

app = webapp2.WSGIApplication(
    [
        (r'/', Main),
    ]
)