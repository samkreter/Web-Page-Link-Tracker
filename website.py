from sets import Set
from pprint import pprint


class Website():

    def __init__(self,details):
       self.id = details['id']
       self.name = details['name']
       self.pages = {}
       self.homepage = -1
       self.pageIds = Set()
       self.pageCount = 0

    def addPage(self,page):
        pageId = page.getPageId()
        self.pageIds.add(pageId)
        self.pageCount = self.pageCount + 1
        if pageId not in self.pages:
            self.pages[pageId] = page
            if page.isHomepage():
                self.homepage = pageId

    def getHomepage(self):
        return self.homepage

    def addLink(self,fromLink, to):
        self.pages[fromLink].addLink(to)

    def getPages(self):
      return self.pageIds

    def getPages(self):
      return self.pages

    def getPage(self,pageId):
      if pageId in self.pages:
        return self.pages[pageId]
      else:
        return -1

    def getPageCount(self):
      return self.pageCount


