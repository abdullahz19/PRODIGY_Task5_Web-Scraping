"""
CONFIGURATION GUIDE FOR WEB SCRAPER
====================================

This guide explains how to configure the web scraper for different websites.
"""

# STEP 1: IDENTIFY THE WEBSITE
# =============================
# Choose an e-commerce website you want to scrape
# Important: Always check the website's robots.txt and terms of service!
# Visit: https://website.com/robots.txt
# 
# Recommended sites for testing:
# - books.toscrape.com (allows scraping, perfect for testing)
# - Any public e-commerce site that allows web scraping

# STEP 2: FIND THE CSS SELECTORS
# ==============================

"""
HOW TO FIND SELECTORS:

A. Using Browser Inspector:
   1. Right-click on a product → Inspect Element
   2. Look at the HTML structure
   3. Identify the container div/article for each product
   4. Find the elements containing: name, price, rating

B. HTML Structure Example:
   <article class="product_pod">           ← CONTAINER
       <div class="image_container">
           <a href="...">
               <img src="..." />
           </a>
       </div>
       <h3>
           <a href="...">Product Name</a>   ← NAME
       </h3>
       <p class="price_color">£39.99</p>   ← PRICE
       <p class="star-rating">Four</p>     ← RATING
   </article>

C. CSS Selector Patterns:
   - By class:  .classname
   - By id:     #idname
   - By tag:    tagname
   - Nested:    parent child
   - Multiple:  .class1.class2

D. Testing Selectors:
   In browser console (F12):
   document.querySelectorAll('article.product_pod')
   If elements appear, your selector works!
"""

# STEP 3: CONFIGURE THE SCRAPER
# ==============================

# Example 1: Books.toscrape.com
example_1 = {
    'url': 'https://books.toscrape.com/',
    'selectors': {
        'container': 'article.product_pod',
        'name': 'h3 a',
        'price': 'p.price_color',
        'rating': 'p.star-rating'
    }
}

# Example 2: Custom Website Template
example_2 = {
    'url': 'https://your-ecommerce-site.com/products',
    'selectors': {
        'container': '.product-container',  # Update based on actual site
        'name': '.product-title',            # Update based on actual site
        'price': '.product-price',           # Update based on actual site
        'rating': '.product-rating'          # Update based on actual site
    }
}

# STEP 4: USE THE SCRAPER
# =======================

"""
Basic Usage:

from scraper import scrape_website

url = 'https://books.toscrape.com/'

selectors = {
    'container': 'article.product_pod',
    'name': 'h3 a',
    'price': 'p.price_color',
    'rating': 'p.star-rating'
}

csv_file = scrape_website(url, selectors, 'output.csv')
print(f"Data saved to: {csv_file}")
"""

# STEP 5: MULTIPLE PAGES
# ======================

"""
Scraping Multiple Pages:

from scraper import WebScraper, CSVExporter
import time

all_products = []
base_url = 'https://website.com/page-{}'
selectors = {...}

for page in range(1, 6):  # Pages 1 through 5
    url = base_url.format(page)
    scraper = WebScraper(url)
    soup = scraper.fetch_page()
    products = scraper.parse_products(soup, selectors)
    all_products.extend(products)
    
    # Be respectful - add delay between requests
    time.sleep(2)  # Wait 2 seconds between requests

CSVExporter.export(all_products, 'all_products.csv')
"""

# STEP 6: COMMON SELECTOR PATTERNS
# ==================================

common_patterns = {
    'container': [
        'article.product',
        'div.product-item',
        'li.product',
        'div[class*="product"]',
        'article[data-product-id]'
    ],
    'name': [
        'h3 a',
        '.product-name',
        '.title',
        'span.name',
        'h2.product-title'
    ],
    'price': [
        '.price',
        '.product-price',
        'span[class*="price"]',
        'p.price_color',
        '.cost'
    ],
    'rating': [
        '.rating',
        '.star-rating',
        '.stars',
        'span[class*="rating"]',
        '.review-score'
    ]
}

# STEP 7: INSPECTOR BROWSER SHORTCUTS
# ====================================

inspector_tips = """
Windows/Linux:     Press F12
Mac:               Press Cmd+Option+I
Right-click:       Inspect Element

Console shortcuts to test selectors:
- document.querySelectorAll('selector') → Returns matching elements
- document.querySelector('selector') → Returns first match
- $('selector') → JQuery shortcut (if available)
"""

# STEP 8: TROUBLESHOOTING
# =======================

troubleshooting = """
Problem: "No products found"
Solution:
  1. Right-click on a product → Inspect
  2. Check the container class/id
  3. Test selector in console: document.querySelectorAll('your-selector')
  4. Update selectors dict with correct values

Problem: "Page load fails"
Solution:
  1. Check if URL is correct
  2. Verify website is accessible in browser
  3. Check internet connection
  4. Some sites may block scrapers - check robots.txt

Problem: "Price/Rating fields showing 'N/A'"
Solution:
  1. Inspect the element for the actual selector
  2. The content might be in a nested element
  3. Try different selector combinations

Problem: "Connection refused / timeout"
Solution:
  1. Increase timeout: WebScraper(url, timeout=30)
  2. Add retry logic
  3. Check if website blocks requests
"""

# STEP 9: ETHICAL SCRAPING CHECKLIST
# ===================================

ethical_checklist = """
Before scraping a website:

☐ Check robots.txt (https://website.com/robots.txt)
☐ Read Terms of Service
☐ Check if API is available (preferred over scraping)
☐ Plan to add delays between requests
☐ Set appropriate User-Agent header
☐ Limit concurrent requests
☐ Use appropriate cache/persistence
☐ Respect rate limits
☐ Contact website if unsure about scraping

The scraper already includes:
✓ Proper User-Agent header
✓ Error handling and logging
✓ Timeout settings
✓ Clean data extraction
"""

# STEP 10: OUTPUT EXAMPLE
# =======================

output_example = """
The scraper creates a CSV file like this:

name,price,rating
"A Light in the Attic","£51.77","Three"
"Twig","£23.19","One"
"Soumission","£49.79","One"
"Sharp Objects","£47.82","Four"
"Sapiens: A Brief History of Humankind","£54.23","Five"
...

You can open this file with:
- Excel
- Google Sheets
- Python (pandas.read_csv())
- Any text editor
"""

# QUICK START COMMANDS
# ====================

quick_start = """
1. Open command prompt in the Web Scraping folder

2. Run one of these:
   
   a) Using batch file (Windows):
      run.bat
   
   b) Using Python directly:
      python quickstart.py
      python examples.py
      python test_scraper.py

3. Follow the prompts in the terminal

4. Check output .csv file
"""

print(__doc__)
print(quick_start)
print(output_example)
