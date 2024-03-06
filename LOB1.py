import pandas as pd
import random
 
# Define the lines of business
lobs = ['Mobile', 'Internet', 'TV', 'Landline', 'VoIP']
 
# Generate random prices for each LOB
prices = [random.uniform(20.0, 100.0) for _ in lobs]
 
# Create a DataFrame
df = pd.DataFrame(list(zip(lobs, prices)), columns=['LOB', 'Price'])
 
# Optionally, format the Price column to two decimal places
df['Price'] = df['Price'].map('{:,.2f}'.format)
 
# Display the DataFrame
print(df)