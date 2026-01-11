"""
Pre-configured Website Examples
================================

This file contains ready-to-use configurations for various websites.
Simply copy the configuration and use it with the scraper.
"""

# IMPORTANT: Always check robots.txt and ToS before scraping!
# Visit: https://website.com/robots.txt

WEBSITES = {
    # =========================================
    # RECOMMENDED FOR TESTING (Allows Scraping)
    # =========================================
    
    'books_toscrape': {
        'name': 'Books.toscrape.com',
        'url': 'https://books.toscrape.com/',
        'description': '✓ Perfect for testing, explicitly allows scraping',
        'selectors': {
            'container': 'article.product_pod',
            'name': 'h3 a',
            'price': 'p.price_color',
            'rating': 'p.star-rating'
        },
        'notes': 'No authentication needed, good for learning'
    },
    
    # =========================================
    # POPULAR E-COMMERCE SITES (Verify ToS First!)
    # =========================================
    
    'amazon_example': {
        'name': 'Amazon',
        'url': 'https://www.amazon.com/s',
        'description': 'Complex JavaScript rendering - requires Selenium',
        'selectors': {
            'container': '[data-component-type="s-search-result"]',
            'name': 'h2 a span',
            'price': '.a-price-whole',
            'rating': '.a-star-small'
        },
        'notes': '⚠ Requires: 1) Selenium browser automation 2) User-Agent rotation 3) Proxy rotation',
        'difficulty': 'HARD'
    },
    
    'ebay_example': {
        'name': 'eBay',
        'url': 'https://www.ebay.com/sch/i.html',
        'description': 'Offers API as better alternative',
        'selectors': {
            'container': '.s-item',
            'name': '.s-item__title',
            'price': '.s-item__price',
            'rating': '.s-item__reviews'
        },
        'notes': '📌 eBay provides official API - consider using that instead',
        'difficulty': 'MEDIUM'
    },
    
    'walmart_example': {
        'name': 'Walmart',
        'url': 'https://www.walmart.com/search/',
        'description': 'JavaScript heavy, dynamic content',
        'selectors': {
            'container': '[data-item-id]',
            'name': 'a.absolute[href*="/ip/"]',
            'price': 'span.price',
            'rating': 'div[aria-label*="star"]'
        },
        'notes': '⚠ May require JavaScript rendering (Selenium/Playwright)',
        'difficulty': 'HARD'
    },
    
    # =========================================
    # STRUCTURED DATA SITES (Easier)
    # =========================================
    
    'quotes_example': {
        'name': 'Quotes.toscrape.com',
        'url': 'https://quotes.toscrape.com/',
        'description': 'Simple structured website for learning',
        'selectors': {
            'container': 'div.quote',
            'name': 'span.text',
            'price': 'span.tag-item',  # Uses tags instead of price
            'rating': 'small.author'    # Uses author instead of rating
        },
        'notes': 'Great for learning basic scraping techniques',
        'difficulty': 'EASY'
    },
    
    # =========================================
    # STATIC HTML SITES (Easier)
    # =========================================
    
    'generic_store': {
        'name': 'Generic E-commerce Store',
        'url': 'https://example-ecommerce.com/products',
        'description': 'Template for static HTML e-commerce sites',
        'selectors': {
            'container': 'div.product, article.product-item',
            'name': 'h3.product-name, .product-title',
            'price': 'span.price, .product-price',
            'rating': '.rating, .stars, [class*="review"]'
        },
        'notes': 'Customize selectors based on actual site structure',
        'difficulty': 'EASY'
    },
}


# ============================================================================
# USAGE EXAMPLES
# ============================================================================

def example_1_simple():
    """Simple example for books.toscrape.com"""
    from scraper import scrape_website
    
    config = WEBSITES['books_toscrape']
    
    csv_file = scrape_website(
        url=config['url'],
        selectors=config['selectors'],
        output_file='books.csv'
    )
    
    print(f"Scraped data saved to: {csv_file}")


def example_2_multiple_pages():
    """Scrape multiple pages from books.toscrape.com"""
    from scraper import WebScraper, CSVExporter
    import time
    
    config = WEBSITES['books_toscrape']
    all_products = []
    
    # Scrape first 3 pages
    for page in range(1, 4):
        url = f"{config['url']}catalogue/page-{page}.html"
        
        print(f"Scraping page {page}...")
        scraper = WebScraper(url)
        soup = scraper.fetch_page()
        products = scraper.parse_products(soup, config['selectors'])
        all_products.extend(products)
        
        # Wait 1 second between requests (be respectful)
        time.sleep(1)
    
    filename = CSVExporter.export(all_products, 'all_books.csv')
    print(f"Saved {len(all_products)} products to {filename}")


def example_3_custom_site():
    """Template for scraping any custom site"""
    from scraper import scrape_website
    
    # Replace with your website
    YOUR_URL = "https://example-store.com/products"
    
    # You'll need to find these selectors using browser inspector
    YOUR_SELECTORS = {
        'container': '.product-item',      # ← Find this
        'name': '.product-name',            # ← Find this
        'price': '.product-price',          # ← Find this
        'rating': '.product-rating'         # ← Find this
    }
    
    csv_file = scrape_website(
        url=YOUR_URL,
        selectors=YOUR_SELECTORS,
        output_file='custom_products.csv'
    )
    
    return csv_file


# ============================================================================
# HELPER FUNCTION TO LIST ALL SITES
# ============================================================================

def list_websites():
    """Display all available website configurations"""
    print("\n" + "="*70)
    print("AVAILABLE WEBSITE CONFIGURATIONS")
    print("="*70 + "\n")
    
    for key, config in WEBSITES.items():
        difficulty = config.get('difficulty', 'MEDIUM')
        print(f"📌 {config['name']}")
        print(f"   Key: {key}")
        print(f"   URL: {config['url']}")
        print(f"   Difficulty: {difficulty}")
        print(f"   {config['description']}")
        if 'notes' in config:
            print(f"   Notes: {config['notes']}")
        print()


def get_config(website_key):
    """Get configuration for a specific website"""
    if website_key in WEBSITES:
        return WEBSITES[website_key]
    else:
        print(f"Website '{website_key}' not found")
        print("Available websites:")
        for key in WEBSITES.keys():
            print(f"  - {key}")
        return None


# ============================================================================
# ADVANCED CONFIGURATIONS
# ============================================================================

# Configuration for JavaScript-heavy sites (requires Selenium)
SELENIUM_EXAMPLE = {
    'url': 'https://dynamic-website.com',
    'wait_time': 10,  # Wait 10 seconds for JS to render
    'selectors': {
        'container': '.dynamic-product',
        'name': '.dynamic-name',
        'price': '.dynamic-price',
        'rating': '.dynamic-rating'
    }
}

# Configuration for paginated sites
PAGINATED_EXAMPLE = {
    'base_url': 'https://example.com/products?page={}',
    'pages': range(1, 6),  # Pages 1 through 5
    'delay': 2,  # 2 seconds between requests
    'selectors': {
        'container': '.product',
        'name': '.name',
        'price': '.price',
        'rating': '.rating'
    }
}

# Configuration with proxy rotation (for advanced use)
PROXY_EXAMPLE = {
    'url': 'https://example.com',
    'proxies': [
        'http://proxy1.com:8080',
        'http://proxy2.com:8080',
        'http://proxy3.com:8080',
    ],
    'selectors': {
        'container': '.product',
        'name': '.name',
        'price': '.price',
        'rating': '.rating'
    }
}


# ============================================================================
# MAIN - DEMONSTRATE USAGE
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("WEB SCRAPER - WEBSITE CONFIGURATIONS")
    print("="*70)
    
    # List all available websites
    list_websites()
    
    print("\n" + "="*70)
    print("TO USE A CONFIGURATION:")
    print("="*70)
    print("""
1. Import the function:
   from website_configs import get_config
   
2. Get the configuration:
   config = get_config('books_toscrape')
   
3. Use with scraper:
   from scraper import scrape_website
   csv_file = scrape_website(
       url=config['url'],
       selectors=config['selectors'],
       output_file='output.csv'
   )
    """)
    
    print("="*70)
    print("IMPORTANT REMINDERS")
    print("="*70)
    print("""
✓ Always check robots.txt: https://website.com/robots.txt
✓ Read the website's Terms of Service
✓ Some sites require: User-Agent, delays, proxy rotation
✓ Dynamic sites (JavaScript) need Selenium or Playwright
✓ Add delays between requests: time.sleep(2)
✓ Respect rate limits and server resources
✓ Use official APIs when available
    """)
