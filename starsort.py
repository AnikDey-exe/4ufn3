import pandas as pd
import csv 

df = pd.read_csv('starfinal.csv')

del df['Luminosity']

df.to_csv('starmain.csv')