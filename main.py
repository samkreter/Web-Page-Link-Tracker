from driver import Driver

driver = Driver()


print("Enter Option")
print("1:hasHomepage")
print("2:page Count")
print("3:orphan Pages")
print("4:Number sites linked to")
print("5:N distant links")
print("q: to quite")

choice = raw_input()

while choice != "q":

    if choice == "1":
        print("Enter websiteId")
        webId = raw_input()
        webId = int(webId)
        if driver.hasHomepage(webId) == -1:
            print("invalid id")

    elif choice == "2":
        print("Enter websiteId")
        webId = raw_input()
        webId = int(webId)
        if driver.pageCount(webId) == -1:
           print("invalid id")

    elif choice == "3":
        print("Enter websiteId")
        webId = raw_input()
        webId = int(webId)
        if driver.checkOrphans(webId) == -1:
            print("invalid id")

    elif choice == "4":
        print("Enter websiteId")
        webId = raw_input()
        webId = int(webId)
        if driver.numSitesLinkedTo(webId) == -1:
            print("Invalid id")

    elif choice == "5":
        print("Enter webpageId")
        pageId = raw_input()
        pageId = int(pageId)
        print("Enter N")
        n = raw_input()
        if n >= 0:
            if driver.accessWithNLinks(pageId,n) == -1:
                print("invalid id")
        else:
            print("invalid n")
    else:
        print("Enter a valid Number")

    print("Enter choice")
    choice = raw_input()
