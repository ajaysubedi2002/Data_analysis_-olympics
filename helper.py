import pandas as pd
df = pd.read_csv("athlete_events.csv")
noc = pd.read_csv("noc_regions.csv")

def medaltally (df):    
    medal_tally = df.drop_duplicates(subset=['Year', 'Medal','region',"Team","NOC","Games","City","Sport","Event"])
    medal_summary = medal_tally.groupby("region")[['Bronze','Gold',"Silver"]].sum().sort_values(by='Gold', ascending=False).reset_index()
    medal_summary["Total"] = medal_summary['Gold'] + medal_summary['Silver']+ medal_summary['Bronze']
    return medal_summary
