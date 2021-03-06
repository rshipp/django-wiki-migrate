import requests
import execjs

from django_wiki_migrate import urlify

# Constants
CREATE = '/_create'

# Custom exception
class MigrationException(Exception):
    """Error while migrating."""

# Base class
class ToDjangoWiki(object):
    def __init__(self, from_url, to_url, username, password):
        self.from_url = from_url
        self.to_url = to_url
        self.username = username
        self.password = password
        self.pages = list()

    def migrate(self):
        print("Collecting information from your old wiki...")
        self.findPages()
        for index, page in enumerate(self.pages):
            print("Migrating page " + str(index+1) + " of " +
                    str(len(self.pages)) + ": " + page)
            self.migratePage(page)
        print("All done!")

    def findPages(self):
        raise NotImplementedError("Override the findPages method in your subclass")

    def migratePage(self, title):
        raise NotImplementedError("Override the migratePage method in your subclass")

    def slugify(self, title):
        """Turn a title into a slug, using Django-wiki's JS algorithms."""
        urlify = execjs.compile(urlify.URLIFY + urlify.URLIFY_DJANGO_WIKI)
        urlify.call("slugify", title)

    def createPage(self, title, content):
        """Create a new page on the django-wiki site."""
        data = {
            'title': title,
            'slug': slugify(title),
            'content': content,
            'summary': 'Page created automatically by django-wiki-migrate.',
        }
        requests.post(self.to_url + CREATE, data)
