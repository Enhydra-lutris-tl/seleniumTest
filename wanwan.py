import pandas as pd

df = pd.read_excel('/Users/tanglei/Downloads/订单.xlsx')
print(df.drop([0, 3]))  # 删除某一行
