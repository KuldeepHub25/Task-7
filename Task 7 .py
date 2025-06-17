# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 16:15:56 2025

@author: Kuldeep
"""

# Import necessary libraries
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the SQLite database
conn = sqlite3.connect("sales_data.db")  # Make sure the DB is in same folder

# Step 2: Run SQL query
query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Step 3: Print the result
print(df)

# Step 4: Plot the revenue by product
df.plot(kind='bar', x='product', y='revenue', legend=False, title='Revenue by Product', color='skyblue')
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Optional: Saves image
plt.show()

# Close the connection
conn.close()
