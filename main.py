import requests
import pandas as pd
from bs4 import BeautifulSoup
# goal to find company names and skills required
def main():
    html_text = requests.get('https://books.toscrape.com/').text
    soup = BeautifulSoup(html_text, 'lxml')
    book_shop = soup.find_all('article','product_pod')
    
    books_list = []
    #for loop
    for book in book_shop:
        book_title = book.find('h3').a.text
        book_price = book.find('p','price_color').text.replace('Â','')
        book_availabilty = book.find('p','instock availability').text.strip()
        books_list.append({
            'Title':book_title,
            'Price': book_price,
            'availabilty': book_availabilty
        })
        
    df = pd.DataFrame(books_list)
    df.to_csv('books_list.csv',index=False)
    print('done....')

if __name__ == "__main__":
    main()
