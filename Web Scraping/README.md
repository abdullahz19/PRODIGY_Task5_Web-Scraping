# Web Scraping Project

A comprehensive Python web scraper for extracting product information (names, prices, ratings) from e-commerce websites and storing the data in CSV format.

## Features

✨ **Core Features:**
- Extract product names, prices, and ratings from e-commerce websites
- Parse HTML using BeautifulSoup with CSS selectors
- Handle multiple products and pages
- Export data to well-formatted CSV files
- Comprehensive error handling and logging
- User-friendly interface with examples

## Installation

### Requirements
- Python 3.8 or higher
- Virtual environment (recommended)

### Step 1: Create Virtual Environment
```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Quick Start

### Basic Usage

```python
from scraper import scrape_website

# Define target website and CSS selectors
url = "https://books.toscrape.com/"

selectors = {
    'container': 'article.product_pod',
    'name': 'h3 a',
    'price': 'p.price_color',
    'rating': 'p.star-rating'
}

# Run the scraper
csv_file = scrape_website(url, selectors, 'output.csv')
print(f"Data saved to: {csv_file}")
```

### Run Examples
```bash
python examples.py
```

This will show you interactive examples including:
1. Basic scraping from Books.toscrape.com
2. Custom website template
3. Multi-page scraping
4. Guide to finding CSS selectors

## Finding CSS Selectors

### Method 1: Browser Inspector

1. **Open Developer Tools**
   - Press `F12` on Windows/Linux
   - Press `Cmd+Option+I` on Mac
   - Or right-click any element → Inspect

2. **Identify HTML Elements**
   - Each product is typically wrapped in a container (e.g., `<article>`, `<div class="product">`)
   - Product name is usually in `<h3>`, `<h2>`, or `<span>`
   - Price is typically in `<span>` or `<p>` with class containing "price"
   - Rating is usually in elements with class containing "rating" or "star"

3. **Note the Selectors**
   - Class selectors start with `.` (e.g., `.product-name`)
   - ID selectors start with `#` (e.g., `#price`)
   - Tag selectors are plain (e.g., `h3`)

4. **Test in Console**
   ```javascript
   // Open browser console (F12)
   document.querySelectorAll('article.product_pod')  // Should return products
   ```

### Method 2: Using Inspector

Look for patterns:
- **Container**: `article.product_pod`, `div.product-item`, `li.product`
- **Name**: `h3 a`, `.product-name`, `span.title`
- **Price**: `.price`, `span.price`, `p.price_color`
- **Rating**: `.star-rating`, `.rating`, `span[class*="star"]`

## Project Structure

```
Web Scraping/
├── scraper.py           # Main scraper module
├── examples.py          # Interactive examples
├── requirements.txt     # Project dependencies
├── README.md           # This file
├── scraper.log         # Log file (auto-generated)
└── products_*.csv      # Output CSV files (auto-generated)
```

## Class Reference

### WebScraper

Main class for web scraping operations.

```python
from scraper import WebScraper

scraper = WebScraper(url="https://example.com")
soup = scraper.fetch_page()
products = scraper.parse_products(soup, selectors)
```

**Methods:**
- `fetch_page()` - Fetches and parses the webpage
- `parse_products(soup, selectors)` - Extracts product information
- `get_products()` - Returns extracted products list

### CSVExporter

Class for exporting data to CSV format.

```python
from scraper import CSVExporter

filename = CSVExporter.export(products, 'output.csv')
```

**Methods:**
- `export(products, filename)` - Exports products to CSV file

## Advanced Usage

### Scraping Multiple Pages

```python
from scraper import WebScraper, CSVExporter

all_products = []
base_url = "https://example.com/page-{}"

selectors = {
    'container': '.product',
    'name': '.product-name',
    'price': '.product-price',
    'rating': '.product-rating'
}

for page in range(1, 5):
    url = base_url.format(page)
    scraper = WebScraper(url)
    soup = scraper.fetch_page()
    products = scraper.parse_products(soup, selectors)
    all_products.extend(products)

CSVExporter.export(all_products, 'all_products.csv')
```

### Custom Error Handling

```python
from scraper import WebScraper
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

try:
    scraper = WebScraper("https://example.com")
    soup = scraper.fetch_page()
    products = scraper.parse_products(soup, selectors)
except requests.RequestException as e:
    print(f"Network error: {e}")
except Exception as e:
    print(f"Scraping error: {e}")
```

## Output Format

The CSV output contains the following columns:
- **name**: Product name
- **price**: Product price (cleaned)
- **rating**: Product rating/review score

Example output:
```csv
name,price,rating
Product 1,£29.99,Four
Product 2,£44.99,Three
Product 3,£34.99,Five
```

## Logging

The scraper automatically logs all operations to:
- **Console**: Real-time output
- **File**: `scraper.log` (persistent log file)

Log levels:
- `INFO`: General information
- `DEBUG`: Detailed information (product extraction)
- `WARNING`: Non-critical issues
- `ERROR`: Critical errors

## Important Notes

### Ethical Scraping
- ✅ Check the website's `robots.txt` file
- ✅ Read the website's terms of service
- ✅ Don't overload the server with requests
- ✅ Add delays between requests for multiple pages
- ✅ Respect rate limits and robots.txt rules

### Best Practices
1. **Test selectors** using browser inspector before running
2. **Add delays** between page requests: `time.sleep(2)`
3. **Use proper headers** (user-agent already set by default)
4. **Handle errors gracefully** with try-except blocks
5. **Monitor logs** for any issues
6. **Respect robots.txt** rules

### Common Issues

**Issue**: "No products found"
- **Solution**: Check if selectors are correct using browser inspector

**Issue**: "Connection error"
- **Solution**: Verify URL is correct, check internet connection

**Issue**: "Permission denied"
- **Solution**: The website may block scrapers. Check robots.txt and terms of service

**Issue**: "Invalid selector"
- **Solution**: Make sure CSS selector syntax is correct (use `.` for class, `#` for id)

## Example Selectors by Website

### Books.toscrape.com
```python
selectors = {
    'container': 'article.product_pod',
    'name': 'h3 a',
    'price': 'p.price_color',
    'rating': 'p.star-rating'
}
```

## Requirements

See `requirements.txt` for all dependencies:
- **requests**: HTTP library for fetching web pages
- **beautifulsoup4**: HTML parsing and CSS selector support
- **pandas**: Data manipulation and CSV export
- **lxml**: XML/HTML parser (used by BeautifulSoup)

## Troubleshooting

### Virtual Environment Issues
```bash
# Deactivate current environment
deactivate

# Remove and recreate
rmdir venv /s
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Import Errors
```bash
# Ensure all packages are installed
pip install -r requirements.txt --force-reinstall
```

### Permission Errors on Windows
```bash
# Run terminal as Administrator
# Or use full path to Python executable
"C:/path/to/venv/Scripts/python.exe" scraper.py
```

## Future Enhancements

Potential features to add:
- [ ] Support for JavaScript-heavy websites (Selenium)
- [ ] Database export (SQLite, PostgreSQL)
- [ ] Email notification when scraping completes
- [ ] Scheduled scraping (daily, weekly, etc.)
- [ ] Data deduplication and cleaning
- [ ] Price change tracking
- [ ] Web GUI for easier configuration
- [ ] Proxy rotation support
- [ ] Image download capability

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the logs in `scraper.log`
3. Verify selectors using browser inspector
4. Test with the examples provided

## Tips for Success

1. **Start Simple**: Begin with a single page before attempting multi-page scraping
2. **Test Selectors**: Always verify CSS selectors in the browser console
3. **Monitor Logs**: Check `scraper.log` for detailed error information
4. **Be Respectful**: Follow website's robots.txt and ToS
5. **Handle Errors**: Use try-except blocks for robust code
6. **Add Delays**: Use `time.sleep()` between requests for multiple pages

---

Happy Scraping! 🚀
