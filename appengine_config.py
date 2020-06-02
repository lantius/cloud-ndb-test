import pkg_resources

from google.appengine.ext import vendor
vendor.add('lib')

pkg_resources.working_set.add_entry('lib')