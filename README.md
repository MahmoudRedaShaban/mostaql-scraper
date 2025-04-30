# Mostaql.com Scraper

This is a professional web scraper to extract freelance project listings from [Mostaql.com](https://mostaql.com), focusing on the "Development" category.

## 🔧 Tech Stack

- Python
- httpx + BeautifulSoup
- SQLite3 for storage
- dotenv for environment management

## 🚀 Features

- Async scraping with `httpx`
- Extracts project title, meta info, description, and link
- Deduplication using SQLite
- Logs stored in `scraper.log`

## 📦 Setup

```bash
pip install -r requirements.txt
cp .env.example .env  # Set your DB_SQL and URL
