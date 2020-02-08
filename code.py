# --------------
import pandas as pd 

# Read the data using pandas module.
df = pd.read_csv(path)
# Find the list of unique cities where matches were played
unique_cities = df['city'].unique()
print (unique_cities)
# Find the columns which contains null values if any ?
missing_coulmn = df.isnull().sum()
print (missing_coulmn[missing_coulmn > 0])
# List down top 5 most played venues

top_5_venue = df[['match_code','venue']].drop_duplicates()['venue'].value_counts().head()
# df.groupby(['venue'])['match_code'].nunique().sort_values().head()
print (top_5_venue)

# Make a runs count frequency table
print (df['runs'].value_counts())
# How many seasons were played and in which year they were played 

df['year'] = df['date'].apply(lambda x : x[:4])
seasons =  df['year'].nunique()
years =  df['year'].unique()
print (seasons, ":",years)

#df.date = pd.to_datetime (df.date,infer_datetime_format = True) 

# No. of matches played per season
print (df.groupby(['year'])['match_code'].nunique())

# Total runs across the seasons
print (df.groupby(['year'])['total'].sum())

# Teams who have scored more than 200+ runs. Show the top 10 results

var200 = df.groupby(['match_code','batting_team'])['total'].sum().sort_values(ascending = False) 
print (var200[var200 > 200].head (10))


# What are the chances of chasing 200+ target

g1 = df.groupby(['match_code','batting_team','inning'])['total'].sum().reset_index()
prob_winning = g1.loc[((g1['total'] > 200) & (g1.inning == 2)),:].shape[0]
prob_total = df['match_code'].nunique()
print (prob_winning*100/prob_total)

# Which team has the highest win count in their respective seasons ?

h1 = df.groupby(['year','winner'])['match_code'].nunique()
h2 = h1.groupby(level = 0, group_keys = False)
print (h2.apply(lambda x : x.sort_values(ascending = False).head(1)))


