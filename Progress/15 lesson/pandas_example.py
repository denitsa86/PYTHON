import matplotlib.pyplot as plt
import pandas as pd

# # data = [10, 20, 30, 40]
# # series = pd.Series(data)
# # print(series)
# #
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
# df = pd.DataFrame(data)
# print(df)
# # #
# # df = pd.read_csv('output.csv')
# # print(df)
# #
# # df = pd.read_excel('output.xlsx')
# # print(df)
# #
# # print(df.head())
# # print(df.tail())
# # print(df.info())
# # print(df.shape)
# #
# # print(df['Name'])  # access 'Name' column
# # print(df[['Name', 'Age']])  # access multiple columns
# # print(df.iloc[1])  # rows are accessed by index
# # print(df[df['Age'] > 30])  # rows can be accessed based on a condition
# #
# df['Salary'] = [50000, 60000, 70000]  # adds a column
# print(df)
# #
# df.rename(columns={'Name': 'Full Name', 'Age': 'Age (years)'}, inplace=True)
# print(df)
# #
# df.drop('Salary', axis=1, inplace=True)  # Drop 'Salary' column
# print(df)
# #
# print(df.isnull())
# df.fillna(0, inplace=True)  # replace NaN with 0
# print(df)
#
# df.dropna(inplace=True)  # drop rows with no value
#
# df.sort_values(by='Age (years)', ascending=False, inplace=True)  # Sort by 'Age' in descending order
# new = (df.reset_index(drop=True))
# print(df)
#
# df = pd.DataFrame({
#     'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
#     'Value': [10, 20, 30, 40, 50, 60]
# })
# grouped = df.groupby('Category').mean()  # Group by 'Category' and compute the mean of 'Value'
# print(grouped)
#
# df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
# df2 = pd.DataFrame({'ID': [1, 2, 4], 'Age': [25, 30, 35]})
# merged_df = pd.merge(df1, df2, on='ID', how='inner')  # Perform an inner join on 'ID'
# print(merged_df)
#
# df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
# df2 = pd.DataFrame({'ID': [3, 4], 'Name': ['Charlie', 'David']})
# concatenated_df = pd.concat([df1, df2], ignore_index=True)  # Concatenate vertically
# print(concatenated_df)
#
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
# df = pd.DataFrame(data)
# #
# df['Age Plus Ten'] = df['Age'].apply(lambda x: x + 10)  # Add 10 years to each value in the 'Age' column
# print(df)
# #
# df = df.applymap(lambda x: str(x) + '!')
# print(df)
#
# df = pd.DataFrame({
#     'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
#     'Value': [10, 20, 30, 40, 50, 60],
#     'Sales': [100, 200, 300, 400, 500, 600]
# })
# pivot = df.pivot_table(values='Sales', index='Category', aggfunc='sum')
# print(pivot)
#
# df = pd.DataFrame({'Date': ['2024-01-01', '2024-02-01', '2024-03-01']})
# df['Date'] = pd.to_datetime(df['Date']) #datetime object
# print(df)
#
# df.to_csv('output.csv', index=False)
# df.to_excel('output.xlsx', index=False)
#
# df['Date'].plot(kind='line')  # Line plot of 'Age' column
# plt.show()