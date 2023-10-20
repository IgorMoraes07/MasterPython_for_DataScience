##pip install tables

import pandas as pd

store = pd.HDFStore('Fontes/stocks.h5')

store.keys()

df = store['stocks']

df.columns
