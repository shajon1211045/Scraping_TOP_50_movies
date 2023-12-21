# Scraping Top 50 Movies

This Python script performs web scraping to extract information about the "50 Most Highly-Ranked Films" from a specific URL. The script processes the data, transforms it, and then loads it into both a CSV file and an SQLite database.

## Requirements

- Python 3.x
- Libraries:
  - requests
  - sqlite3
  - pandas
  - BeautifulSoup

Install the required libraries using the following command:

```bash
pip install pandas beautifulsoup4
```

## Usage
### Clone the repository  
```bash
git clone https://github.com/shajon1211045/Scraping_Top_50_movies.git  
cd Scraping_Top_50_movies
```
### Run the scraping script  
```bash
python Webscraper.py
```  
## Project Structure

- `scraping_top_50_movies.py`: The main Python script for web scraping, data transformation, and loading.
- `top_50_films.csv`: CSV file containing the transformed data.
- `Movies.db`: SQLite database containing the transformed data.

