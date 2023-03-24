import pandas as pd


def main():
    df = pd.read_excel('/Users/tanglei/Downloads/订单.xlsx')
    dataframe = df.drop([0, 3])
    print(dataframe)
    return dataframe


