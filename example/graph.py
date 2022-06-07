import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tips = sns.load_dataset('tips')

print(tips.head())
print(type(tips))

tips.to_excel(excel_writer='tips.xlsx')

# sns.pairplot(tips,kind='scatter')
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')

plt.show()