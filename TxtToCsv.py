import pandas as pd

df = pd.read_csv('merged.txt',
                 sep=':', parse_dates=True)

df.to_csv('merged.csv',encoding='utf-8-sig')
