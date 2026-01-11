"""
Web Scraper for E-commerce Product Information
This module extracts product information (names, prices, ratings) from e-commerce websites
and stores the data in a structured CSV format.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class WebScraper:
    """Main web scraper class for extracting product information from e-commerce sites."""
    
    def __init__(self, url: str, timeout: int = 10):
        """
        Initialize the scraper with a target URL.
        
        Args:
            url: The e-commerce website URL to scrape
            timeout: Request timeout in seconds
        """
        self.url = url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.products = []
    
    def fetch_page(self) -> BeautifulSoup:
        """
        Fetch the webpage and return BeautifulSoup object.
        
        Returns:
            BeautifulSoup: Parsed HTML content
            
        Raises:
            requests.RequestException: If the request fails
        """
        try:
            logger.info(f"Fetching URL: {self.url}")
            response = self.session.get(self.url, timeout=self.timeout)
            response.raise_for_status()
            logger.info("Page fetched successfully")
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            logger.error(f"Failed to fetch the page: {e}")
            raise
    
    def parse_products(self, soup: BeautifulSoup, selectors: Dict[str, str]) -> List[Dict]:
        """
        Parse product information from the BeautifulSoup object.
        
        Args:
            soup: BeautifulSoup object of the webpage
            selectors: Dictionary with CSS selectors for:
                      - 'container': Product container selector
                      - 'name': Product name selector
                      - 'price': Price selector
                      - 'rating': Rating selector
        
        Returns:
            List of dictionaries containing product information
        """
        products = []
        
        try:
            containers = soup.select(selectors['container'])
            logger.info(f"Found {len(containers)} product(s)")
            
            for idx, container in enumerate(containers):
                try:
                    product = self._extract_product(container, selectors)
                    if product:
                        products.append(product)
                        logger.debug(f"Extracted product {idx + 1}: {product.get('name', 'N/A')}")
                except Exception as e:
                    logger.warning(f"Error extracting product {idx + 1}: {e}")
                    continue
            
            self.products = products
            logger.info(f"Successfully extracted {len(products)} product(s)")
            return products
            
        except Exception as e:
            logger.error(f"Error parsing products: {e}")
            raise
    
    def _extract_product(self, container, selectors: Dict[str, str]) -> Dict:
        """
        Extract individual product information from a container element.
        
        Args:
            container: BeautifulSoup element containing product info
            selectors: Dictionary of CSS selectors
        
        Returns:
            Dictionary with product information or None if extraction fails
        """
        product = {}
        
        # Extract product name
        name_elem = container.select_one(selectors['name'])
        product['name'] = name_elem.get_text(strip=True) if name_elem else 'N/A'
        
        # Extract price
        price_elem = container.select_one(selectors['price'])
        if price_elem:
            price_text = price_elem.get_text(strip=True)
            # Clean price (remove currency symbols, keep only numbers and decimal)
            product['price'] = self._clean_price(price_text)
        else:
            product['price'] = 'N/A'
        
        # Extract rating
        rating_elem = container.select_one(selectors['rating'])
        product['rating'] = rating_elem.get_text(strip=True) if rating_elem else 'N/A'
        
        return product
    
    @staticmethod
    def _clean_price(price_text: str) -> str:
        """
        Clean price text to extract numeric value.
        
        Args:
            price_text: Raw price text from webpage
        
        Returns:
            Cleaned price string
        """
        # Remove common currency symbols and whitespace
        import re
        cleaned = re.sub(r'[^\d.,]', '', price_text)
        return cleaned.strip() if cleaned else 'N/A'
    
    def get_products(self) -> List[Dict]:
        """Get extracted products."""
        return self.products


class CSVExporter:
    """Class for exporting scraped data to CSV format."""
    
    @staticmethod
    def export(products: List[Dict], filename: str = None) -> str:
        """
        Export product data to CSV file.
        
        Args:
            products: List of product dictionaries
            filename: Output filename (default: products_TIMESTAMP.csv)
        
        Returns:
            Filename of the created CSV file
        """
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'products_{timestamp}.csv'
        
        try:
            # Convert to DataFrame
            df = pd.DataFrame(products)
            
            # Ensure proper column order
            columns = ['name', 'price', 'rating']
            df = df[[col for col in columns if col in df.columns]]
            
            # Export to CSV
            df.to_csv(filename, index=False, encoding='utf-8')
            logger.info(f"Data exported successfully to {filename}")
            logger.info(f"Total products exported: {len(products)}")
            
            return filename
        except Exception as e:
            logger.error(f"Error exporting to CSV: {e}")
            raise


def scrape_website(url: str, selectors: Dict[str, str], output_file: str = None) -> str:
    """
    Complete web scraping workflow.
    
    Args:
        url: Target website URL
        selectors: CSS selectors for product elements
        output_file: Optional output CSV filename
    
    Returns:
        Filename of the created CSV
    """
    try:
        # Initialize scraper
        scraper = WebScraper(url)
        
        # Fetch and parse
        soup = scraper.fetch_page()
        products = scraper.parse_products(soup, selectors)
        
        # Export to CSV
        if products:
            filename = CSVExporter.export(products, output_file)
            return filename
        else:
            logger.warning("No products found to export")
            return None
    
    except Exception as e:
        logger.error(f"Scraping failed: {e}")
        raise


if __name__ == "__main__":
    # Example usage with a sample e-commerce site
    # Replace these with actual website and selectors
    
    URL = "https://example-ecommerce.com/products"
    
    # CSS selectors - these need to be customized per website
    SELECTORS = {
        'container': '.product-item',      # Container for each product
        'name': '.product-name',            # Product name element
        'price': '.product-price',          # Product price element
        'rating': '.product-rating'         # Product rating element
    }
    
    OUTPUT_FILE = "products.csv"
    
    try:
        csv_file = scrape_website(URL, SELECTORS, OUTPUT_FILE)
        print(f"\nScraping completed! Data saved to: {csv_file}")
    except Exception as e:
        print(f"Error: {e}")
