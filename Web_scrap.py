import requests

from bs4 import BeautifulSoup

//Creating an instances of a requests.
result = requests.get("https://www.google.com/");  

//Accessing the status_code attribute and it will return 200 for OK.
print(result.status_code) 

//prints a long list of headers
print(result.headers) 

//Scraping the content of a web and storing it.
src = result.content

//Creating an instances of BeautifulSoup
soup = BeautifulSoup(src, "html.parser")

//Find all the elements with html <a></a> tag.
links = soup.find_all("a")
print(links)
