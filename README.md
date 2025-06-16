# Book Scraper — Base Version

Scrapes book data from books.toscrape.com and uploads it to Google Sheets.

## Features
- Scrapes all books with pagination
- Uploads only new titles (no duplicates) (not yet)
- Modular code structure (ready for growth)

## To Use
1. Set up `credentials.json` for your service account
2. Create a Google Sheet and share it with the service account email
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   playwright install
