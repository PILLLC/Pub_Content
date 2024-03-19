import requests
from bs4 import BeautifulSoup

# URL of the news article webpage
url = "https://www.news.com/news/article"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract the title of the article
    title = soup.find("h1").text.strip()
    print("Title:", title)
    
    # Extract the publication date of the article
    date = soup.find("time").text.strip()
    print("Publication Date:", date)
    
    # Extract the author(s) of the article
    author = soup.find("div", class_="author").text.strip()
    print("Author:", author)
    
    # Extract the main content of the article
    content = soup.find("div", class_="article-content").text.strip()
    print("Content:", content)
    
    # Extract other relevant information as needed
    
else:
    print("Failed to retrieve the webpage.")