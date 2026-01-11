"""
Example usage of the web scraper for extracting product information.
This demonstrates how to use the scraper with different e-commerce websites.
"""

from scraper import WebScraper, CSVExporter
import logging

logger = logging.getLogger(__name__)


def example_1_basic_scraping():
    """
    Example 1: Basic web scraping from a simple e-commerce site
    """
    print("\n" + "="*60)
    print("EXAMPLE 1: Basic Product Scraping")
    print("="*60)
    
    # URL of the target website
    url = "https://books.toscrape.com/"
    
    # CSS selectors for the website structure
    selectors = {
        'container': 'article.product_pod',
        'name': 'h3 a',
        'price': 'p.price_color',
        'rating': 'p.star-rating'
    }
    
    try:
        scraper = WebScraper(url)
        soup = scraper.fetch_page()
        products = scraper.parse_products(soup, selectors)
        
        print(f"\nExtracted {len(products)} products")
        print("\nFirst 3 products:")
        for i, product in enumerate(products[:3], 1):
            print(f"\n{i}. {product.get('name', 'N/A')}")
            print(f"   Price: {product.get('price', 'N/A')}")
            print(f"   Rating: {product.get('rating', 'N/A')}")
        
        # Export to CSV
        filename = CSVExporter.export(products, 'books_products.csv')
        print(f"\n✓ Data saved to: {filename}")
        
    except Exception as e:
        print(f"Error: {e}")


def example_2_custom_website():
    """
    Example 2: Template for scraping a custom e-commerce website
    """
    print("\n" + "="*60)
    print("EXAMPLE 2: Custom Website Scraping Template")
    print("="*60)
    
    # This is a template - replace with actual website details
    url = "https://your-ecommerce-site.com/products"
    
    # To find the right selectors:
    # 1. Open the website in a browser
    # 2. Right-click on a product element
    # 3. Select "Inspect" or "Inspect Element"
    # 4. Find the class or id names for product containers, names, prices, ratings
    
    selectors = {
        'container': '.product-container',  # Update this
        'name': '.product-title',            # Update this
        'price': '.product-price',           # Update this
        'rating': '.product-rating'          # Update this
    }
    
    print("\nTemplate for custom website:")
    print(f"URL: {url}")
    print("\nSelectors to customize:")
    for key, selector in selectors.items():
        print(f"  - {key}: {selector}")
    
    print("\n📝 How to find selectors:")
    print("  1. Inspect the website in your browser (F12)")
    print("  2. Right-click on a product → Inspect Element")
    print("  3. Identify class names or IDs")
    print("  4. Update the selectors dictionary")
    print("  5. Run the scraper")


def example_3_multiple_pages():
    """
    Example 3: Scraping multiple pages
    """
    print("\n" + "="*60)
    print("EXAMPLE 3: Multi-Page Scraping Template")
    print("="*60)
    
    from scraper import WebScraper, CSVExporter
    
    all_products = []
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    
    selectors = {
        'container': 'article.product_pod',
        'name': 'h3 a',
        'price': 'p.price_color',
        'rating': 'p.star-rating'
    }
    
    print("\nScraping multiple pages...")
    
    try:
        # Scrape first 3 pages
        for page in range(1, 4):
            url = base_url.format(page)
            print(f"\nFetching page {page}: {url}")
            
            scraper = WebScraper(url)
            soup = scraper.fetch_page()
            products = scraper.parse_products(soup, selectors)
            all_products.extend(products)
            
            print(f"Found {len(products)} products on page {page}")
        
        print(f"\n✓ Total products collected: {len(all_products)}")
        
        # Export all products
        filename = CSVExporter.export(all_products, 'all_books.csv')
        print(f"✓ Data saved to: {filename}")
        
    except Exception as e:
        print(f"Error: {e}")


def get_inspector_guide():
    """
    Display guide on how to use browser inspector to find selectors
    """
    print("\n" + "="*60)
    print("GUIDE: How to Find CSS Selectors")
    print("="*60)
    
    guide = """
1. OPEN BROWSER DEVELOPER TOOLS
   - Press F12 on Windows/Linux
   - Press Cmd+Option+I on Mac
   - Or right-click → Inspect

2. LOCATE PRODUCT CONTAINER
   - Look for repeated HTML blocks (one per product)
   - Common patterns: <div class="product">, <article class="item">
   - Note the class name or id

3. FIND PRODUCT NAME
   - Look for <h3>, <h2>, <span> with product title
   - Example: <h3 class="product-title">Product Name</h3>

4. FIND PRICE
   - Look for $ symbol or .price class
   - Example: <span class="price">$29.99</span>

5. FIND RATING
   - Look for star icons or .rating class
   - Example: <span class="rating">4.5/5</span>

6. TEST THE SELECTORS
   - Open browser console (F12)
   - Type: document.querySelectorAll('your-selector')
   - If results appear, the selector works!

COMMON SELECTORS:
- By class: .class-name
- By id: #id-name
- By tag: div, span, p
- Nested: .parent .child
- Combined: div.product-container

EXAMPLE:
Container: div.product
Name: .product-name or h3.title
Price: .price or span[class*="price"]
Rating: .rating or .stars
    """
    print(guide)


if __name__ == "__main__":
    import sys
    
    print("\n" + "="*60)
    print("WEB SCRAPER EXAMPLES")
    print("="*60)
    
    print("\nAvailable examples:")
    print("1. Basic scraping (Books.toscrape.com)")
    print("2. Custom website template")
    print("3. Multi-page scraping template")
    print("4. CSS Selector finding guide")
    print("0. Exit")
    
    choice = input("\nSelect an example (0-4): ").strip()
    
    if choice == '1':
        example_1_basic_scraping()
    elif choice == '2':
        example_2_custom_website()
    elif choice == '3':
        example_3_multiple_pages()
    elif choice == '4':
        get_inspector_guide()
    elif choice == '0':
        print("Goodbye!")
    else:
        print("Invalid choice")
