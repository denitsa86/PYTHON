import pandas as pd
#
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# df = pd.DataFrame(data)
#
# data_two = {
#   "calories": [200, 201, 300],
#   "duration": [5, 4, 10]
# }
# df2 = pd.DataFrame(data)
#
# new_df = pd.concat([df,df2])
# new_df.reset_index(drop=True, inplace=True)
# print(new_df)

data1 = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}

data2 = {
  "qualified": [True, False, False]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

new_df = df1.join(df2, how="right")

print(new_df)