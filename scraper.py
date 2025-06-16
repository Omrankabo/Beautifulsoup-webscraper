import requests
from bs4 import BeautifulSoup
from config import BASE_URL
import pandas as pd
import time

# escaping characters for the terminal indecators
CLR = '\033[02J'
CLR_RETURN = '\033[0H'


def fetcher(page):
    # headers so the site does not think it's a bot
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    url = BASE_URL.format(page)
    response = requests.get(url,headers=headers)
    # check for status code
    if response.status_code != 200:
        return []
    #geting page html
    soup = BeautifulSoup(response.text, 'lxml')
    books = soup.find_all('article', 'product_pod')
    
    print(f"{CLR_RETURN}Scraping Page....{page}")
    
    books_list = []
    #extracting info from the page
    for book in books:
        try:
            
            book_name = book.find('h3').a.get('title').strip()
            book_price = book.find("p","price_color").text.strip().replace("Â",'')
            book_availability = " ".join(book.find('p','instock availability').text.split())
            book_img = "https://books.toscrape.com/" + book.find('img')['src'].replace('../','')
                
            books_list.append({
                "name": book_name,
                "price": book_price,
                "availability": book_availability,
                "img_url": book_img
            })
        except Exception as e:
            continue
        print(CLR_RETURN)
        
    
    return books_list

def scraper():
    all_books = []
    print(f"{CLR}Starting to fetch data...")
    for page in range(1,51):
        #delay between pages
        time.sleep(1.5)
        all_books += fetcher(page)
        
    print(f"Done fetching data... ✅ {CLR_RETURN}")
    df = pd.DataFrame(all_books)
    df.to_csv("books.csv", index=False, encoding="utf-8")

    print("✅ saved to books.csv")
    exit()
    
    


scraper()