from sets import Set


#stores all the page data
class Page():
    def __init__(self, details):
        self.id = details['id']
        self.url = details['url']
        self.website = details['website']
        self.homepage = details['home']
        self.links = Set()

    def isHomepage(self):
        return self.homepage

    def getWebId(self):
        return self.website

    def isHomepage(self):
        return self.homepage

    def addLink(self,to):
        self.links.add(to)

    def getLinks(self):
        return self.links

    def getPageId(self):
        return self.id
