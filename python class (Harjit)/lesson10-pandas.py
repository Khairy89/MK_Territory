#libraries - pandas
#lesson 11: pandas module
import pandas as pd

# Create a dataframe from a dictionary
data = {'Name': ['John', 'Jane', 'Bob', 'Alice'],
        'Age': [25, 30, 28, 23],
        'Gender': ['M', 'F', 'M', 'F']}
df = pd.DataFrame(data)
print(df)

# Create a dataframe from a list of lists
data = [['John', 25, 'M'], ['Jane', 30, 'F'], ['Bob', 28, 'M'], ['Alice', 23, 'F']]
df = pd.DataFrame(data, columns=['Name', 'Age', 'Gender'])
print(df)

# Accessing data in a dataframe
print(df['Name'])
print(df.Name)
print(df[['Name', 'Age']])

# Selecting rows based on conditions
print(df[df['Age'] > 25])

# Sorting data in a dataframe
print(df.sort_values(by='Age'))

# Applying functions to data in a dataframe
print(df['Age'].apply(lambda x: x*2))

# Grouping data in a dataframe
grouped_df = df.groupby('Gender')
print(grouped_df.mean())

# Merging dataframes
new_df = pd.DataFrame({'Name': ['Sarah', 'David'], 'Age': [32, 29]})
merged_df = pd.merge(df, new_df, on='Name')
print(merged_df)