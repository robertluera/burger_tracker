import pandas as pd


sheet_id = '1j9OD3wtRJ5XE_yjIt2TZtAHhARXqRtOuIlHdoh9cdrs'

sheet_name = 'Burger_Total'

url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
# url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url)

total = df.iloc[0,0]

print(f'\nSo far, {total} burgers have been consumed this year.')
