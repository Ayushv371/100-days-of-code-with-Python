import pandas as pd
data = pd.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")

#primary fur color | count
gray = black = cinnamon = 0

for datasets in data["Primary Fur Color"]:
    if datasets == 'Gray':
        gray += 1
    if datasets == 'Cinnamon':
        cinnamon += 1
    if datasets == 'Black':
        black += 1

data_dict = {
    'Fur Color' : ['Gray', 'Cinnamon', 'Black'],
    'Count' : [gray, cinnamon, black]
}

ds = pd.DataFrame(data_dict)
ds.to_csv('SquirrelCount.csv')