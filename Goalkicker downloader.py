from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re
import requests

#sets up the link, taking data from goalkicker 
r = requests.get("https://books.goalkicker.com/")
data = r.text
soup = BeautifulSoup(data, features="html.parser")
path = input("Enter the path in which the pdfs will be saved: ")
#Repeats the code for every link found
for link in soup.find_all('a'):
    links = link.get('href')
    #makes python run on the next page that was found from the link
    resp = ("https://books.goalkicker.com/" + links)
    s = requests.get(resp)
    newData = s.text
    soup = BeautifulSoup(newData, features="html.parser")
    #finds the button that says download, button is the class listed in the css
    new = str(soup.find('button', "download"))
    #splits the css so the pdf title is separated and is the 2nd element
    url = new.split('\'')
    amt = len(url)
    #skips the first one b/c its not an actual download in this case
    if amt>1:
        ending = url[1]
        name = path + ending
        #downloads the file to the directory set above
        urllib.request.urlretrieve(resp+ending, name)
    
    
    
    
    
        
    
    
    
    
    
