# Similar imports as above

# Add your scraping logic for title, price, and URL

# Save the data to a CSV file
df = pd.DataFrame(item_data)
df.to_csv('items.csv', index=False)
