import pandas as pd
df = pd.read_csv("athlete_events.csv")
noc = pd.read_csv("noc_regions.csv")

def preporcess():
    global df,region_df    
    df = df[df["Season"] =="Summer"]
    df= pd.merge(df,noc, on = "NOC" ,how = "left")
    df.drop_duplicates(inplace=True)
    df = pd.concat([df, pd.get_dummies(df['Medal'],dtype=float)],axis=1)
    return df