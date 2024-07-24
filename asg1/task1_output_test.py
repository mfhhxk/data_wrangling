import json
import pandas as pd
groupnum=input("015")
with open("task1_015.json","r") as file:
    content=file.read()
    try:
        data=json.loads(content)
    except:
        raise TypeError("Invalid json: unable to load data!")
    try:
        df=pd.DataFrame(data)
        table = pd.pivot_table(df, values=df.columns, columns=df.index, aggfunc="max")
    except Exception as e:
        raise ValueError("Invalid daya structure: check your data structure!")
    
    indexnames1=['assignees-info', 'assignors-info', 'conveyance-text',
       'correspondent-party', 'last-update-date', 'property-count']
    
    indexnames2=['assignees-info', 'assignors-info', 'conveyance-text',
       'correspondent-party', 'last-updated-date', 'property-count']
    
    assert set(indexnames1)==set(df.index.to_list()) or set(indexnames2)==set(df.index.to_list()), "Invalid key in json: check your json keys!"
    print("Task 1 json file passed!")


