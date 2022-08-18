import requests

import pandas as pd
from pandasgui import show

url = "https://www.alko.fi/INTERSHOP/static/WFS/Alko-OnlineShop-Site/-/Alko-OnlineShop/fi_FI/Alkon%20Hinnasto%20Tekstitiedostona/alkon-hinnasto-tekstitiedostona.xlsx"

df = pd.read_excel(url, header=3)

text_fields = ['Nimi', 'Valmistaja', 'Pullokoko', 'Hinta', 'Litrahinta',
   'Uutuus', 'Tyyppi', 'Alatyyppi', 'Erityisryhmä', 'Oluttyyppi',
   'Valmistusmaa', 'Alue', 'Vuosikerta', 'Etikettimerkintöjä', 'Huomautus',
   'Rypäleet', 'Luonnehdinta', 'Pakkaustyyppi', 'Suljentatyyppi', 'Valikoima']

for f in text_fields:
    df[f] = df[f].replace({pd.NA: 'Nan'})

df['Alkoholi-%/Litrahinta'] = df['Alkoholi-%'] / df['Litrahinta']

df.to_csv('alko.csv', index=False)

show(df)
