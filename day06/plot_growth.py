import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

growth_data = pd.read_excel('growth_data.xlsx')
data_titles = growth_data.columns

growth_data.plot.scatter(x='Time (hr)',y='Turbidity (OD600)')
plt.savefig('growth_plot.png')
plt.show()



