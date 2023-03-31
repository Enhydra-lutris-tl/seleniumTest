import pandas as pd
from prettytable import PrettyTable


def main():
    path = open('/Users/tanglei/life/alipay_record_20230331_103351.csv')
    df = pd.read_csv(path)
    df2 = df.drop(range(23))
    # print(df2)
    count = df2.shape[1]
    cl = df2.columns
    newcl = []
    for i in range(count):
        newcl.append(df2.iloc[0][cl[i]])
    df3 = df2.set_axis(newcl, axis=1).reset_index().drop(labels=0).drop(labels="index",axis=1)
    # print(df3)
    # 表格库使用
    cl3 = df3.columns
    count3 = df3.shape[1]
    table = PrettyTable(newcl)
    for i in range(df3.shape[0]):
        ceshi = []
        for b in range(count3):
            ceshi.append(df3.iloc[i][cl3[b]])
        table.add_row(ceshi)
    print(table)


main()
