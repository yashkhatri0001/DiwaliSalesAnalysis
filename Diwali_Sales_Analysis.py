# import python libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # visualizing data
%matplotlib inline
import seaborn as sns

# import csv file
df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')

# check the number of rows and columns
print(f"Shape of the DataFrame: {df.shape}")

# display the first few rows of the DataFrame
print("\nFirst 5 rows of the DataFrame:")
print(df.head())

# get a concise summary of the DataFrame, including data types and non-null values
print("\nInformation about the DataFrame:")
df.info()

# drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# check for null values in each column
print("\nNumber of null values in each column:")
print(pd.isnull(df).sum())

# drop rows with any null values
df.dropna(inplace=True)

# change the data type of the 'Amount' column to integer
df['Amount'] = df['Amount'].astype('int')

# verify the data type of the 'Amount' column
print("\nData type of the 'Amount' column:")
print(df['Amount'].dtypes)

# print the names of all columns in the DataFrame
print("\nColumn names:")
print(df.columns)

# rename the 'Marital_Status' column to 'Shaadi'
df.rename(columns= {'Marital_Status':'Shaadi'}, inplace=True)
print("\nColumn names after renaming 'Marital_Status':")
print(df.columns)

# get descriptive statistics of the numerical columns in the DataFrame
print("\nDescriptive statistics of the DataFrame:")
print(df.describe())

# get descriptive statistics for specific columns: 'Age', 'Orders', and 'Amount'
print("\nDescriptive statistics for 'Age', 'Orders', and 'Amount':")
print(df[['Age', 'Orders', 'Amount']].describe())

# Exploratory Data Analysis

### Gender
# plotting a bar chart for Gender and its count
plt.figure(figsize=(7, 5))
ax = sns.countplot(x = 'Gender', data = df)
plt.title('Count of Buyers by Gender')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# plotting a bar chart for gender vs total amount
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(7, 5))
sns.barplot(x = 'Gender', y = 'Amount', data = sales_gen)
plt.title('Total Amount Spent by Gender')
plt.ylabel('Total Amount')
plt.show()

print("\n*From above graphs we can see that most of the buyers are females and even the purchasing power of females is greater than men*")

### Age
plt.figure(figsize=(10, 6))
ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')
plt.title('Count of Buyers by Age Group and Gender')
for bars in ax.containers:
    ax.bar_label(bars)
plt.legend(title='Gender')
plt.show()

# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x = 'Age Group', y = 'Amount', data = sales_age)
plt.title('Total Amount Spent by Age Group')
plt.ylabel('Total Amount')
plt.show()

print("\n*From above graphs we can see that most of the buyers are of age group between 26-35 yrs female*")

### State
# total number of orders from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
plt.figure(figsize=(15, 5))
sns.barplot(data = sales_state, x = 'State', y = 'Orders')
plt.title('Total Number of Orders from Top 10 States')
plt.ylabel('Number of Orders')
plt.show()

# total amount/sales from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
plt.figure(figsize=(15, 5))
sns.barplot(data = sales_state, x = 'State', y = 'Amount')
plt.title('Total Sales/Amount from Top 10 States')
plt.ylabel('Total Amount')
plt.show()

print("\n*From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively*")

### Marital Status
plt.figure(figsize=(7, 5))
ax = sns.countplot(data = df, x = 'Shaadi') # Using the renamed column 'Shaadi'
plt.title('Count of Buyers by Marital Status')
plt.xlabel('Marital Status')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

sales_state = df.groupby(['Shaadi', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(6, 5))
sns.barplot(data = sales_state, x = 'Shaadi', y = 'Amount', hue='Gender')
plt.title('Total Amount Spent by Marital Status and Gender')
plt.xlabel('Marital Status')
plt.ylabel('Total Amount')
plt.legend(title='Gender')
plt.show()

print("\n*From above graphs we can see that most of the buyers are married (women) and they have high purchasing power*")

### Occupation
plt.figure(figsize=(20, 5))
ax = sns.countplot(data = df, x = 'Occupation')
plt.title('Count of Buyers by Occupation')
plt.xlabel('Occupation')
for bars in ax.containers:
    ax.bar_label(bars)
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(20, 5))
sns.barplot(data = sales_state, x = 'Occupation', y = 'Amount')
plt.title('Total Amount Spent by Occupation')
plt.xlabel('Occupation')
plt.ylabel('Total Amount')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

print("\n*From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector*")

### Product Category
plt.figure(figsize=(20, 5))
ax = sns.countplot(data = df, x = 'Product_Category')
plt.title('Count of Buyers by Product Category')
plt.xlabel('Product Category')
for bars in ax.containers:
    ax.bar_label(bars)
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
plt.figure(figsize=(20, 5))
sns.barplot(data = sales_state, x = 'Product_Category', y = 'Amount')
plt.title('Total Amount Spent by Top 10 Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Total Amount')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

print("\n*From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category*")

sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
plt.figure(figsize=(20, 5))
sns.barplot(data = sales_state, x = 'Product_ID', y = 'Orders')
plt.title('Top 10 Most Ordered Product IDs')
plt.xlabel('Product ID')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

# top 10 most sold products (same thing as above)
plt.figure(figsize=(12, 7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
plt.title('Top 10 Most Ordered Product IDs (Alternative Visualization)')
plt.xlabel('Product ID')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

print("\n## Conclusion:\n")
print("*Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category*")
print("\nComplete project on YouTube: https://www.youtube.com/@RishabhMishraOfficial")
print("\nComplete project on GitHub: https://github.com/rishabhnmishra/Python_Diwali_Sales_Analysis")
print("Thank you!")
