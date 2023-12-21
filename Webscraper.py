# Import necessary libraries
import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

# Define database-related variables
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = 'top_50_films.csv'

# Create an empty DataFrame with specified column names
df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])

# Initialize a counter
count = 0

# Fetch the HTML content from the specified URL
html_page = requests.get(url).text

# Parse the HTML content using BeautifulSoup
data = BeautifulSoup(html_page, 'html.parser')

# Find all tables in the HTML content
tables = data.find_all('tbody')

# Extract rows from the first table
rows = tables[0].find_all('tr')

# Iterate over each row
for row in rows:
    # Limit the loop to the first 50 rows
    if count < 50:
        # Extract columns from the row
        col = row.find_all('td')
        
        # Check if there are any columns
        if len(col) != 0:
            # Create a dictionary with column data
            data_dict = {
                "Average Rank": int(col[0].contents[0]),
                "Film": str(col[1].contents[0]),
                "Year": int(col[2].contents[0])
            }
            
            # Convert the dictionary to a DataFrame
            df1 = pd.DataFrame(data_dict, index=[0])
            
            # Concatenate the new DataFrame to the main DataFrame
            df = pd.concat([df, df1], ignore_index=True)
            
            # Increment the counter
            count += 1
    else:
        break

# Print the resulting DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv(csv_path)

# Connect to SQLite database, replace the existing table if it exists, and close the connection
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()
