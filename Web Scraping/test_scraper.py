"""
Simple test to verify the scraper works
"""
import sys
sys.path.insert(0, '.')

from scraper import WebScraper, CSVExporter
import requests

print("Testing Web Scraper...\n")

try:
    # Test with a site that allows scraping
    print("1. Testing page fetch...")
    scraper = WebScraper("https://books.toscrape.com/")
    soup = scraper.fetch_page()
    print("   ✓ Page fetched successfully")
    
    print("\n2. Testing product extraction...")
    selectors = {
        'container': 'article.product_pod',
        'name': 'h3 a',
        'price': 'p.price_color',
        'rating': 'p.star-rating'
    }
    
    products = scraper.parse_products(soup, selectors)
    print(f"   ✓ Found {len(products)} products")
    
    if products:
        print(f"\n3. Sample product:")
        p = products[0]
        print(f"   Name: {p['name']}")
        print(f"   Price: {p['price']}")
        print(f"   Rating: {p['rating']}")
    
    print("\n4. Testing CSV export...")
    filename = CSVExporter.export(products, 'test_output.csv')
    print(f"   ✓ Exported to {filename}")
    
    print("\n✅ All tests passed!")
    
except requests.exceptions.ConnectionError:
    print("❌ Network error - could not connect to website")
    print("   Make sure you have internet connection")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
