import pandas as pd
url = "http://127.0.0.1:8080/temp.html"
tables = pd.read_html(url) # Returns list of all tables on page
table = tables[1]
#print(table_2)
res=[]
table=table.iloc[1:,:]
table.columns=['Job','Job Min','Job Max','Heat','Laddle','Mac Id','Date','Time','Temp']
table1=table.loc[table["Laddle"]=="7"].iloc[0]
table2=table.loc[table["Laddle"]=="8"].iloc[0]
json=table1.to_json()
print(json)
json1=table2.to_json()
print(json1)
