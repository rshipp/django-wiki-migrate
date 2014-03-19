class ToDjangoWiki(object):
    def __init__(self, url):
        self.url = url
        self.pages = dict()

    def migrate(self):
        print("Collecting information from your old wiki...")
        self.findPages()
        for index, page in enumerate(self.pages):
            print("Migrating page " + str(index+1) + " of " + \
                    str(len(self.pages)) + ": " + page)
            self.migratePage(page)
        print("All done!")

    def findPages(self):
        raise NotImplementedError("Override the findPages method in your subclass")

    def migratePage(self, title):
        raise NotImplementedError("Override the migratePage method in your subclass")

    def createPage(self, title, content):
        # TODO: Create a new page on the django-wiki site.
        pass
