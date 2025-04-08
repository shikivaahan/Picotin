import pandas as pd

def clean_itemgroup_data(file_path):
    df = pd.read_excel(file_path, engine='xlrd', skiprows=4)
    df = df[:-1]
    df = df.dropna(axis=1, how='all')
    df.columns = ['Date'] + list(df.columns[1:])
    if 'Unnamed: 2' in df.columns:
        df = df.drop(columns=['Unnamed: 2'])
    df = df[df['Date'] != 'Total']
    df = df[df['Date'].notna()]
    unnamed_columns = [col for col in df.columns if col.startswith('Unnamed')]
    df = df.drop(columns=unnamed_columns)
    return df

def clean_daily_summary(file_path):
    ASQ_itemgroup = pd.read_csv(file_path)
    unnamed_columns = [col for col in ASQ_itemgroup.columns if col.startswith('Unnamed:')]
    ASQ_itemgroup.drop(columns=unnamed_columns, inplace=True)
    return ASQ_itemgroup

ASQ_daily_summary = clean_itemgroup_data(r'daily_data\ASQ_itemgroup_daily.xls')

print(ASQ_daily_summary.head())
