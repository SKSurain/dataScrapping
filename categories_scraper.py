import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.tradingpost.com.au/search-results/?q=&filter-location-text=&filter-location-dist=25&cat="
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

# Find all categories
category_elements = soup.find_all('a', class_='sc-row')

# Initialize a list to store the category data
category_data = []

# Loop through each category element and extract the necessary information
for element in category_elements:
    # Extract the category name
    category_name = element.find('span', class_='category').get_text(strip=True)
    
    # Extract the number associated with the category
    category_number = element.find('small').get_text(strip=True)
    category_number = category_number.strip('()').replace(',', '')  # Remove parentheses and commas

    # Add the extracted data to the list
    category_data.append({'Category': category_name, 'Number': category_number})

# Create a DataFrame from the list
df = pd.DataFrame(category_data)

# Save the data in a DataFrame to a CSV file
df.to_csv('categories.csv', index=False)
