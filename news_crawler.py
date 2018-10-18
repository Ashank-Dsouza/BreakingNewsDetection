import requests
from bs4 import BeautifulSoup
from lxml import html
import scrapy
import index
import os 

website_links = ["https://www.aljazeera.com/", "https://www.thehindu.com/", "https://www.ndtv.com/", "http://zeenews.india.com/"]
#website_links = index.listOfLinks


title = ""
#content = ""

clean_contents = ""

consolidatedTitles = []
consolidatedTitleString = ""

for i, website in enumerate(website_links):
   page = requests.get(website)
   soup = BeautifulSoup(page.text, 'html.parser')
   
   #to get the headings and display
   title = soup.find('h1').get_text()
   #print(title.strip("\n"))
   consolidatedTitles.append(title.strip("\n"))
   consolidatedTitleString += "\n\n" + str(i) + ")   "+ title.strip("\n")
   """
   #to get the content of the page
   contents = soup.find_all("p")
   for content in contents:
      clean_contents += content.get_text()
   new_one = os.linesep.join([s for s in soup.find('h1').get_text().splitlines() if s])
   main_story += "\n" + new_one
   print("New Content")
   print(main_story)
   """ 

#To improve attach the twitter mined links instead the website links 

#main_story = "\n\n".join([ll.rstrip() for ll in main_story.splitlines() if ll.strip()])
#print(main_story)
print(consolidatedTitleString)
#res = [tit for tit in consolidatedTitles if "Verified account" not in tit]
#print(res)

