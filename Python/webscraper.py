#webscraper that scrapes for resources on a website and then follows those resources found inititally to n depth
import sys
from bs4 import BeautifulSoup as bs
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def webscrape(domain, start_url, depth):
    x = 0
    """
    uses sets to store the data generated from the parse webpage function and
    runs through however deep it needs to go
    """
    total_media = set() #set to store all of the final links
    total_urls = set() #set to store all of the final media links
    new_urls = set() #set to use for new links (ie: stores all the depth 2 links to search through from depth 1)
    new_media = set() #same as above except these are not searched through
    i = 0
    while i < depth:
        if i == 0:
            parse_webpage(domain, start_url, total_media, total_urls) #ran with the starting URL to get depth of 1
            temp_urls = total_urls.copy() #fills the temps with values
            temp_media = total_media.copy()
            x+=1
            print(x)
        else:
            for url in temp_urls: #since temp urls has all of the next depth, it is used for looping through
                parse_webpage(domain, url, new_media, new_urls)
                x+=1
                print(x) #just had it printing out x to see how many pages it would go through by the end, and so i had a rough idea of when it was done
            temp_urls = new_urls.difference(total_urls) #gets the diff for only the new urls
            temp_media = new_media.difference(total_media) #gets the diff for the new media files
            total_urls = total_urls.union(temp_urls) #adds all of the new urls to total urls
            total_media = total_media.union(temp_media) #same for media
        i+=1
    return total_urls.union(total_media)

def parse_webpage(domain, url, media, urls):
    """
    This function parses the html from each page
    it uses the defined here to search for places in html/js/css
    that will have resources that need to be documented
    and crawled.
    """
    tags = ['img', 'link', 'a'] #img -> data-src, link/a -> href
    session = requests.Session() #this section is to fix issues with having max retries get reset, ssl errors, and other weird edge case errors
    retry = Retry(connect=2, backoff_factor=.1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    try:
        r = session.get(url)
    except Exception as e:
        print(e)
        return #bad coding practice but it's the only way to realistically deal with errors that arise from this as they're server side and not on this end
    try:
        tree = bs(r.text, 'html.parser') #creates the tree to be able to be parsed through, but gave an error so there's a try except around it
    except AssertionError:
        print("script tried to parse something weird, could be a bug with BS4 or some other weird error, only happens on depth 3+ and is NOT debuggable as the output is \"expected name token at '<![�Z#��n\x19�~j1g��S��'\" and the trace\ is in the html parser itself\nTLDR: don't worry about it")
        return #gets out of function because the page is invalid
    for link in tree.find_all(tags):
        if link.get('href') != None: #link.get returns None if it doesn't have the value, checks for not None
            if len(link.get('href')) == 0: #some values with # at the front gave a string length of zero, so they were excluded (and never led to actual resources)
                continue
            elif str(link.get('href'))[0] == '/': #for resources without a domain in front, which means they're on the domain already
                urls.add(domain + link.get('href'))
            elif str(link.get('href'))[0:len(domain)] == domain: #checks with the domain given to see if the domain isn't the same
                urls.add(link.get('href'))
        elif link.get('data-src') != None: #data-src is for media/img headers 
            if str(link.get('data-src'))[0] == '/':
                media.add(domain + link.get('data-src'))
            elif str(link.get('data-src'))[0:len(domain)] == domain:
                media.add(link.get('data-src'))
    
def main():
    domain,url,depth =  [sys.argv[1],sys.argv[2],sys.argv[3]]
    links = webscrape(domain, url, int(depth))
    print(len(links)) #total number of links printed
    with open('allthelinks.txt', 'w') as file:
        for i in links:
            file.write(i+'\n') #writes it out to the text file

if __name__ == "__main__":
    main()