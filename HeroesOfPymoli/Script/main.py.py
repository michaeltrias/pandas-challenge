import pandas as pd
import os
total_players_dict ={}


csvpath = os.path.join('..',"Resources","HeroesOfPymoli_data.csv")

#csv_path = "Resources/HeroesOfPymoli_data.csv"
purchase_df = pd.read_csv(csvpath)

purchase_df = purchase_df.dropna()

#print(purchase_df.columns)

#value_df = pd.DataFrame(purchase_df["SN"].value_counts())

'''
total_players = (len(purchase_df["SN"].value_counts()))
total_players_df = total_players_df.DataFrame({"Total Players" : total_players})

print(total_players_df)
'''


#Player Count
total_players = (len(purchase_df["SN"].value_counts()))

total_players_dict = {"Total Players": total_players}

#total_players_df = pd.DataFrame.from_dict(total_players_dict)
print(total_players_dict)

#print(purchase_df.columns)
#Purchasing Analysis (Total)

# number of unique items
print(len(purchase_df['Item ID'].unique()))

# average price
print(purchase_df.columns)
grouped_item_df = purchase_df["Price"]

print(grouped_item_df.mean())
print(grouped_item_df.sum())
print(purchase_df["Purchase ID"].count())

#make into dataframe


#gender demographics

print(purchase_df["Gender","SN"].value_counts())
#output value given does not match, hw guide