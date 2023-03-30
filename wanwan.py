import pandas as pd


def main():
    path = open('F:/记账测试/alipay_record_20221104_115554.csv')
    df = pd.read_csv(path)
    df2 = df.reset_index()
    count = df2.shape[1]
    cl = df2.columns
    newcl = []
    for i in range(count):
        newcl.append(df2.iloc[0][cl[i]])

    df3 = df2.set_axis(newcl,axis=1)
    print(df3.drop(labels=0))



main()
