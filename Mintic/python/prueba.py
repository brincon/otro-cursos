import pandas as pd

archivo = pd.read_excel("200030-V0025-MGA.XLSM", sheet_name=18)
delete_empty_rows = archivo.dropna(axis=0, thresh=21)

print(archivo)