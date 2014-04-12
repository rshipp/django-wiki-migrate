import requests

from django_wiki_migrate.ToDjangoWiki import ToDjangoWiki, MigrationException
from django_wiki_migrate.xml2obj import xml2obj, xml

class MediaWikiToDjangoWiki(ToDjangoWiki):


    def findPages(self):
        """Fill out self.pages."""

        def xml_wget(url):
            return xml2obj(requests.get(url).text.encode('utf-8'))

        # Attempt to determine which URL format the wiki uses.
        if self.from_url.endswith("index.php?title="):
            api_base = self.from_url.rstrip("index.php?title=") + "api.php"

        elif self.from_url.endswith("/"):
            api_base = self.from_url + "api.php"
        else:
            self.from_url += "/"
            api_base = self.from_url + "api.php"
        api_allpages = api_base + "?action=query&list=allpages&format=xml&aplimit=500&apfrom="

        # Find and add all the pages.
        try:
            results = xml_wget(api_allpages)
            while True:
                for page in results.query.allpages.p:
                    self.pages += [page.title.encode('utf-8')]
                if not results.query_continue:
                    break
                results = xml_wget(api_allpages +
                    results.query_continue.allpages.apcontinue)
        except xml.sax._exceptions.SAXParseException as e:
            raise MigrationException("Error while parsing information from MediaWiki API", e)

    def getPage(self, title):
        """Retrive a page from MediaWiki's Special:Export function."""
        export_page = self.from_url + "Special:Export&action=submit"
        data = {
            'pages': title,
        }
        return requests.post(export_page, data).text.encode('utf-8')

    def migratePage(self, title):
        """Given a page title from self.pages, convert the page
        content to the expected format and send it to django-wiki with
        self.createPage(title, content)
        """
        pass
