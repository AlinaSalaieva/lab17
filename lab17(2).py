import json
import pandas as pd

with open('agrofirms_data.json') as f:
    data = json.load(f)

areas = pd.Series(data)
mean_area = areas.mean()
deviations = areas - mean_area

print('Відхилення від середнього арифметичного:')
print(deviations)

