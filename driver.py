import json
from sets import Set

from pprint import pprint
from website import Website
from page import Page


class Driver:
    def __init__(self):
        self.websites = self.getWebsites()
        self.pageLookup = dict()
        self.pages = self.getPages()
        self.links = self.getLinks()


        #adding pages to their websites
        for pageId, page in self.pages.iteritems():
            if page.getWebId() in self.websites:
                self.websites[page.getWebId()].addPage(page);

        for link in self.links:
            self.websites[self.pageLookup[link['from']]].addLink(link['from'],link['to'])



    def pageCount(self,websiteId):
        if websiteId in self.websites:
            return self.websites[websiteId].getPageCount()
        else:
            return -1

    def checkOrphans(self,websiteId):
        if websiteId in self.websites:
            website = self.websites[websiteId]
            homepage = website.getHomepage()
            if  homepage != -1:
                return list(website.getPages() - website.getPage(homepage).getLinks())
            else:
                return website.getPages();
        else:
            return -1

    #used to query the homepage
    def hasHomepage(self,websiteId):
        if websiteId in self.websites:
            if self.websites[websiteId].getHomepage() != -1:
                return True
            else:
                return False
        else:
            return -1


    def getWebsites(self):
        websites = dict()

        with open('data0/websites.json') as data_file:
            websitesData = json.load(data_file)['websites']

        for website in websitesData:
            websites[website['id']] = Website(website)

        return websites



    def getPages(self):
        pages = dict()
        with open('data0/pages.json') as data_file:
            pagesData = json.load(data_file)['pages']

        for page in pagesData:
            pages[page['id']] = Page(page)
            if page['id'] not in self.pageLookup:
                self.pageLookup[page['id']] = page['website']

        return pages


    def getLinks(self):
        with open('data0/links.json') as data_file:
             return json.load(data_file)['links']


