import json
from sets import Set
from Queue import Queue

from pprint import pprint

#custom Classes
from website import Website
from page import Page


#used to controller the quering and store the lookup tables
class Driver:
    def __init__(self):
        #stores websites witht their id as the key to the dict
        self.websites = self.getWebsites()
        #used for fast lookup of what website a page belongs to
        self.pageLookup = dict()
        #stores pages with their id as the key to the dict
        self.pages = self.getPages()
        #json info for the links
        self.links = self.getLinks()
        #create an ajancency list to call bfs to find paths between pages
        self.alistForLinks = self.getAlistForLinks()

        #adding pages to their websites
        for pageId, page in self.pages.iteritems():
            if page.getWebId() in self.websites:
                self.websites[page.getWebId()].addPage(page);

        #add links into the pages of each website
        for link in self.links:
            self.websites[self.pageLookup[link['from']]].addLink(link['from'],link['to'])



    def accessWithNLinks(self,webpageId,n):
        if webpageId not in self.pages:
            return -1
        else:
            linkablePage = []
            website = self.websites[self.pageLookup[webpageId]]
            for page in website.getPages():
                if self.bfs(webpageId,page) <= n:
                    linkablePage.append(page)
            print(linkablePage)


    def numSitesLinkedTo(self,websiteId):
        if websiteId not in self.websites:
            return -1
        else:
            otherSites = list()
            website = self.websites[websiteId]
            for page in website.getPages():
                for link in self.pages[page].getLinks():
                    if(self.pageLookup[link] != websiteId):
                        otherSites.append(self.pageLookup[link])
            print("Linked Websites Ids are:")
            print(otherSites)


    def pageCount(self,websiteId):
        if websiteId in self.websites:
            print("page count %d"%self.websites[websiteId].getPageCount())
        else:
            return -1

    def checkOrphans(self,websiteId):
        if websiteId not in self.websites:
           return -1
        else:
            website = self.websites[websiteId]
            homepage = website.getHomepage()
            if  homepage != -1:
                print("Orphan Pages are:")
                print(list(website.getPages() - website.getPage(homepage).getLinks() - Set([websiteId])))
            else:
                print("Orphan Pages are:")
                print(website.getPages())

    #used to query the homepage
    def hasHomepage(self,websiteId):
        if websiteId not in self.websites:
            return -1
        else:
            if self.websites[websiteId].getHomepage() != -1:
                print("Has Homepage")
            else:
                print("doeesn't have homepage")

    #parese the json and extract the websites
    def getWebsites(self):
        websites = dict()

        with open('data1/websites.json') as data_file:
            websitesData = json.load(data_file)['websites']

        for website in websitesData:
            websites[website['id']] = Website(website)

        return websites


    #parse to get pages info
    def getPages(self):
        pages = dict()
        with open('data1/pages.json') as data_file:
            pagesData = json.load(data_file)['pages']

        for page in pagesData:
            pages[page['id']] = Page(page)
            if page['id'] not in self.pageLookup:
                self.pageLookup[page['id']] = page['website']

        return pages


    def getLinks(self):
        with open('data1/links.json') as data_file:
             return json.load(data_file)['links']

    #construct the alist
    def getAlistForLinks(self):
        graph = {}
        for link in self.links:
            if link['from'] in graph:
                graph[link['from']].append(link['to'])
            else:
                graph[link['from']] = [link['to']]

        return graph


    #return the shortest path for the pages passed in
    def bfs(self, src, dest):
        vis = set() # stores the vertices that have been visited
        par = {} # stores parent information. vertex -> parent vertex in BFS tree
        distDict = {} # stores distance of visited vertices from the source. This is the number of edges between the source vertex and the given vertex
        q = Queue()
        q.put((src, 0)) # enqueue (source, distance) pair
        par[src] = -1 # source has no parent
        vis.add(src) # minor technicality, will explain later
        while not q.empty():
            (v,dist) = q.get() # grab vertex in queue
            distDict[v] = dist # update the distance
            if v == dest:
                break # reached destination, done
            nextDist = dist+1
            if v in self.alistForLinks:
                for nextV in self.alistForLinks[v]:
                    # visit vertices adjacent to the current vertex
                    if nextV not in vis:
                        # not yet visited
                        par[nextV] = v # update parent of nextV to v
                        q.put((nextV, nextDist)) # add into queeu
                        vis.add(nextV) # mark as visited
        # obtained shortest path now
        if dest in distDict:
            return distDict[dest]
        else:
            return (-1, []) # no shortest path


