from django_wiki_migrate.ToDjangoWiki import ToDjangoWiki

class MediaWikiToDjangoWiki(ToDjangoWiki):

    def findPages(self):
        # TODO: Fill out self.pages.
        pass

    def migratePage(self, title):
        # TODO: Given a page title from self.pages, convert the page
        # content to the expected format and send it to django-wiki with
        # self.createPage(title, content)
        pass
