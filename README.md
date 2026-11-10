# Amazon Global Multi-Market Price Intelligence Pipeline

Automated data collection system for Amazon marketplace price tracking across multiple retail sectors and global endpoints (.co.uk, .com, .ca, .com.au, .de).

## Supported Markets
- **Apparel & Fashion:** Clothing, Activewear, Footwear
- **Health & Wellness:** Supplements, Vitamins, Sports Nutrition  
- **Beauty & Personal Care:** Skincare, Cosmetics, Grooming
- **Education & Lifestyle:** School bags, Stationery

## Core Features
- **Multi-Marketplace Support:** Change marketplace domain and keyword to track any Amazon region
- **Multi-Niche Toggle:** Single variable switch between markets
- **Resilient Data Extraction:** Fallback selectors for Amazon layout changes
- **Cookie & Consent Handling:** Auto-bypass for EU/UK compliance banners
- **CSV Reporting:** Structured output with Timestamp, Product Name, Price, Source URL, Status

## Workflow
- Weekly price sweeps across target sectors
- CSV export ready for pricing strategy and competitor analysis
- Configurable page depth (10+ pages per market)

## Tech Stack
Python, Selenium WebDriver, Firefox

## Usage
pip install selenium
# Set target market
search_keyword = "supplements"
python amazon_tracker.py

Output: market_prices.csv
