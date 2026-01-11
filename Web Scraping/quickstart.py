"""
Quick Start Script - Run this to test the web scraper
This script demonstrates basic functionality with books.toscrape.com
"""

from scraper import scrape_website
import sys

def main():
    print("\n" + "="*70)
    print("WEB SCRAPER - QUICK START TEST")
    print("="*70)
    
    # Using books.toscrape.com as a test website (allows scraping)
    url = "https://books.toscrape.com/"
    
    # These selectors work with books.toscrape.com
    selectors = {
        'container': 'article.product_pod',
        'name': 'h3 a',
        'price': 'p.price_color',
        'rating': 'p.star-rating'
    }
    
    print("\n📚 Test Configuration:")
    print(f"Website: {url}")
    print(f"Output file: books_products.csv")
    print("\nSelectors:")
    for key, value in selectors.items():
        print(f"  • {key}: {value}")
    
    print("\n⏳ Starting scraper...")
    
    try:
        # Run the scraper
        csv_file = scrape_website(url, selectors, 'books_products.csv')
        
        if csv_file:
            print("\n" + "="*70)
            print("✅ SUCCESS!")
            print("="*70)
            print(f"\n📁 Output file: {csv_file}")
            print("\n📋 To view the results:")
            print(f"   1. Open {csv_file} with Excel or a text editor")
            print("   2. Check the scraper.log file for detailed information")
            
            # Try to display the data
            try:
                import pandas as pd
                df = pd.read_csv(csv_file)
                print(f"\n📊 Scraped {len(df)} products:")
                print("\nFirst 5 products:")
                print(df.head().to_string(index=False))
            except:
                pass
        else:
            print("\n⚠️  No products were found. Check the selectors.")
    
    except Exception as e:
        print("\n" + "="*70)
        print("❌ ERROR OCCURRED")
        print("="*70)
        print(f"\nError: {e}")
        print("\n💡 Troubleshooting tips:")
        print("   1. Check your internet connection")
        print("   2. Verify the website is accessible")
        print("   3. Check scraper.log for detailed error info")
        print("   4. Make sure all dependencies are installed:")
        print("      pip install -r requirements.txt")
        sys.exit(1)


if __name__ == "__main__":
    main()
