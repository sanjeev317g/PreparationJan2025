import pandas as pd

df = pd.read_excel("C:\\Users\\SanjeevaKumarGeejula\\Desktop\\Ramp_GMQA_Resource_Details.xlsx", sheet_name='IPC')
print(df['B'])