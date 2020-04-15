from tkinter import *
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
root = Tk()
seed_url=""
root.title("WEB CRAWLER")
root.geometry("700x700")
frame=Frame(root)
frame.pack()
heading=Label(frame,text="WEB CRAWLER",height=5,width=12)
heading.grid(row=0,column=1)

url=Label(frame,text="URL")
url.grid(row=1,column=0,padx=10,pady=10)

url_en=Entry(frame,width=80)
url_en.grid(row=1,column=1,padx=10,pady=10)

def getLink(page):
	href_index = page.find( '<a href=' )	
	if href_index != -1:
		start_quote = page.find('"', href_index + 1)
		end_quote = page.find('"', start_quote + 1)
		url = page[start_quote + 1:end_quote]
		return url, end_quote
	else:
		return -1, -1
	    
def text_input(event):        
    global links_tocrawl,links_crawled
    maximum_tries = 2
    seed_url = url_en.get()
    print(seed_url)
    links_crawled = []
    links_tocrawl = [seed_url]
    links_broken = []
    links_unvalid = ["javascript", "png", "jpeg", "jpg", "gif", "deb", "exe", "facebook", "linkedin", "ieee", "twitter.com"]
    not_valid_url = 0
    crawled_unvalid_links = []
    session = requests.Session()
    session.mount('http://', HTTPAdapter(max_retries=maximum_tries))
    for url in links_tocrawl:
            print("Crawling URL", url)
            # If link is broken then try for maximum number of times, and throw an exception. And move to next url in links_tocrawl list
            try:
                    req = requests.get(url)
            except (requests.exceptions.ConnectionError, e):
                    links_broken.append(url)
                    print("Maximum retires exceeded for", url)
                    links_tocrawl.pop(0)
                    continue
            except (requests.exceptions.TooManyRedirects, e):
                    print("Too many redirects therefore continuing to next link")
                    continue
            page = str(BeautifulSoup(req.content,'html5lib'))
            link, end_quote = getLink(page)
            while link!=-1:		
                    page = page[end_quote:]
                    for non in links_unvalid:
                            if non in link:
                                    not_valid_url = 1
                                    break
                    if (not_valid_url == 1):
                            not_valid_url = 0
                            pass
		#if ("javascript" in link or "jpg" in link or "png" in link or "jpeg" in link):
		#	pass
                    else:
                            if ('http://' not in link and 'https://' not in link):
                                    link = url + link
                            link = link.strip(' /') + '/'
                            if link in links_tocrawl or link in links_crawled:
                                    pass
                            else:
                                    links_tocrawl.append(link)
                                    if len(links_tocrawl) is 15:
                                            break
                    link, end_quote = getLink(page)
            links_crawled.append(url)

            link1=Entry(frame,width=80)
            link1.grid(row=4,column=1,pady=5)
            link1.insert(0,str(links_tocrawl[0]))

            link2=Entry(frame,width=80)
            link2.grid(row=4,column=1,pady=5)
            link2.insert(0,str(links_tocrawl[1]))
            
            link3=Entry(frame,width=80)
            link3.grid(row=6,column=1,pady=5)
            link3.insert(0,str(links_tocrawl[2]))

            link4=Entry(frame,width=80)
            link4.grid(row=7,column=1,pady=5)
            link4.insert(0,str(links_tocrawl[3]))

            link5=Entry(frame,width=80)
            link5.grid(row=8,column=1,pady=5)
            link5.insert(0,str(links_tocrawl[4]))

            link6=Entry(frame,width=80)
            link6.grid(row=9,column=1,pady=5)
            link6.insert(0,str(links_tocrawl[5]))

            link7=Entry(frame,width=80)
            link7.grid(row=10,column=1,pady=5)
            link7.insert(0,str(links_tocrawl[6]))
            
            link8=Entry(frame,width=80)
            link8.grid(row=11,column=1,pady=5)
            link8.insert(0,str(links_tocrawl[7]))
            
            link9=Entry(frame,width=80)
            link9.grid(row=12,column=1,pady=5)
            link9.insert(0,str(links_tocrawl[8]))
            
            link10=Entry(frame,width=80)
            link10.grid(row=13,column=1,pady=5)
            link10.insert(0,str(links_tocrawl[9]))
            
            links_tocrawl.pop(0)

crawl=Button(frame,text="CRAWL",height=2,width=5)
crawl.grid(row=2,column=1,padx=10,pady=10)
crawl.bind('<Button-1>' , text_input)

links=Label(frame,text="LINKS CRAWLED ARE :",height=5,width=17)
links.grid(row=3,column=0,padx=10,pady=10)

root.mainloop()
