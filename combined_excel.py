# Prepare Enviroment
import glob
import pandas as pd
import numpy as np


excel_list = glob.glob("*.xlsx")
print(excel_list)

df_list = []
for file in excel_list:
	df = pd.read_excel(file, engine = 'openpyxl').dropna(how = 'all')
	df_list.append(df)
	combined_df = pd.concat(df_list)

combined_df.to_csv('data_combined.csv', index = False)