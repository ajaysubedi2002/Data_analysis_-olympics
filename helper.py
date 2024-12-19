import pandas as pd
import numpy as np 

# def medaltally (df):    
#     medal_tally = df.drop_duplicates(subset=['Year', 'Medal','region',"Team","NOC","Games","City","Sport","Event"])
#     medal_summary = medal_tally.groupby("region")[['Bronze','Gold',"Silver"]].sum().sort_values(by='Gold', ascending=False).reset_index()
#     medal_summary["Total"] = medal_summary['Gold'] + medal_summary['Silver']+ medal_summary['Bronze']
#     return medal_summary


def country_year_list (df):
    years = df["Year"].unique().tolist()
    years.sort()
    years.insert(0,"overall")
    
    country = np.unique(df["region"].dropna().values).tolist()
    country.sort()
    country.insert(0,"overall")
    
    return years, country

def fetch_medall_tally(df,year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    # Initialize temp_df as None
    temp_df = None
    flag =0
    
    # Both year and country are "overall"
    if year == "overall" and country == "overall":
        temp_df = medal_df
    
    # Year is "overall" but a specific country is given
    elif year == "overall" and country != "overall":
        flag =1
        temp_df = medal_df[medal_df["region"] == country]
    
    # A specific year is given but country is "overall"
    elif year != "overall" and country == "overall":
        temp_df = medal_df[medal_df["Year"] == int(year) ]
    
    # Both year and country are specific
    elif year != "overall" and country != "overall":
        temp_df = medal_df[(medal_df["Year"] == int(year) ) & (medal_df["region"] == country)] 
        
    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

    x['Gold'] = x['Gold'].astype('int')
    x['Silver'] = x['Silver'].astype('int')
    x['Bronze'] = x['Bronze'].astype('int')
    x['total'] = x['total'].astype('int')

    return x




# import numpy as np


# def fetch_medal_tally(df, year, country):
#     medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
#     flag = 0
#     if year == 'Overall' and country == 'Overall':
#         temp_df = medal_df
#     if year == 'Overall' and country != 'Overall':
#         flag = 1
#         temp_df = medal_df[medal_df['region'] == country]
#     if year != 'Overall' and country == 'Overall':
#         temp_df = medal_df[medal_df['Year'] == int(year)]
#     if year != 'Overall' and country != 'Overall':
#         temp_df = medal_df[(medal_df['Year'] == year) & (medal_df['region'] == country)]

#     if flag == 1:
#         x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
#     else:
#         x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
#                                                                                       ascending=False).reset_index()

#     x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

#     x['Gold'] = x['Gold'].astype('int')
#     x['Silver'] = x['Silver'].astype('int')
#     x['Bronze'] = x['Bronze'].astype('int')
#     x['total'] = x['total'].astype('int')

#     return x


# def country_year_list(df):
#     years = df['Year'].unique().tolist()
#     years.sort()
#     years.insert(0, 'Overall')

#     country = np.unique(df['region'].dropna().values).tolist()
#     country.sort()
#     country.insert(0, 'Overall')

#     return years,country
