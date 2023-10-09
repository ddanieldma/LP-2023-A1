import pandas as pd
from read import ler_csv

df_guilherme = ler_csv("ed-superior-inep.csv")

print(df_guilherme.head())