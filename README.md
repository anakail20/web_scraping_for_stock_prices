# Web Scraping for Stock Data

## Overview

This project demonstrates a web scraping application to extract stock-related data from a financial website. The script retrieves information such as stock symbols, company names, current prices, and price changes. 
This project is designed to create a clean dataset from a structured webpage.

## Features

### 1. Web Scraping
- Uses `requests` to fetch the webpage content.
- Leverages `BeautifulSoup` to parse and navigate the HTML structure.

### 2. Data Extraction
- Extracts the following information for each stock:
  - **Stock Symbol**
  - **Company Name**
  - **Current Price**
  - **Price Change**
  - **Percent Change**

### 3. Data Cleaning
- Handles issues like inconsistent data lengths by aligning extracted arrays.

### 4. Data Presentation
- Outputs the scraped data into a structured `pandas` DataFrame for analysis and export.

## Requirements

The project uses the following Python libraries:

```bash
pandas
requests
beautifulsoup4
```

## How to Run

1. Clone the repository:
   ```bash
   git clone <https://github.com/anakail20/web_scraping_for_stock_prices>
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python WebScrapingPythonScript.py
   ```

## Workflow

1. **Fetch Web Page**: The script sends a GET request to the website to retrieve the HTML content.
2. **Parse HTML**: Using `BeautifulSoup`, the script parses the HTML to locate and extract the desired elements.
3. **Build Dataset**:
   - Identifies and processes tags containing stock data.
   - Compiles extracted information into Python lists.
   - Converts the lists into a `pandas` DataFrame.
4. **Save Data**:
   - The DataFrame can be exported to a CSV or used for further analysis.

## Sample Dataset

| Symbol | Company            | Price   | PriceChange | PercentChange |
|--------|--------------------|---------|-------------|---------------|
| AAPL   | Apple Inc.         | $150.00 | +$1.50      | +1.01%        |
| MSFT   | Microsoft Corp.    | $300.00 | -$2.00      | -0.67%        |
| AMZN   | Amazon.com, Inc.   | $100.00 | +$0.50      | +0.50%        |

## Customization

You can easily adapt this script for other web scraping tasks by modifying:
- The target URL.
- The HTML tags and classes used to identify the data.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- **Libraries**: Thanks to the developers of `requests` and `BeautifulSoup` for enabling efficient web scraping.
- **Website**: Data sourced from [The Motley Fool](https://www.fool.com/investing/top-stocks-to-buy.aspx).

---

Feel free to contribute to this repository by submitting issues or pull requests.
