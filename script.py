import pandas as pd 
import math

df = pd.read_csv('data.csv')

class RST:
    name = ""
    total_items = 0
    under_400 = 0
    pctHealthy = 0.0

    def __init__(self, name, total, numHealthy):
        self.name = name
        self.total_items = total
        self.under_400 = numHealthy
        self.pctHealthy = (numHealthy/total) * 100

    def __str__(self):
        return ' '.join((self.name, str(self.total_items), str(self.under_400), str(self.pctHealthy)))

data = []

currentRestaurant = "null"
count = 0
healthy = 0

for index, row in df.iterrows():
    thisRestaurant = row['restaurant']
    cals = row['calories']
    if(currentRestaurant == "null"):
        currentRestaurant = thisRestaurant
        count = count+1
        if cals < 400:
            healthy = healthy+1
    if(currentRestaurant != thisRestaurant):
        rest = RST(currentRestaurant, count, healthy)
        data.append(rest)
        currentRestaurant = thisRestaurant
        count = 1
        healthy = 0
        if cals < 400:
            healthy = 1
    else:
        count = count+1
        if cals < 400:
            healthy = healthy + 1

    print(' '.join((currentRestaurant, str(row['calories']), str(count), str(healthy))))

rest = RST(currentRestaurant, count, healthy)
data.append(rest)
pdData = []
for rest in data:
    thisData = []
    thisData.append(rest.name)
    thisData.append(rest.total_items)
    thisData.append(rest.under_400)
    thisData.append(rest.pctHealthy)
    pdData.append(thisData)


output = pd.DataFrame(pdData, columns=['restaurant', 'num_items', 'num_items_under_400_cals', 'percent_items_under_400_cals'])

output.to_csv(r'under_400_cals.csv', index=False)








