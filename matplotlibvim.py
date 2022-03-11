import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# x = np.linspace(0,10,1000)
# # x is a 1000 evenly spaced numbers from 0 to 10
plt.style.use('ggplot')
presidents_df = pd.read_csv('president_heights_party.csv')
y = np.sin(x)
plt.xlabel('x')
plt.ylabel('y')
plt.title('function sin(x)')
plt.plot(x, np.sin(x), color= 'k', label='sin(x)')
plt.plot(x, np.cos(x), color= 'r' , linestyle='--', label='cos(x)')
plt.savefig('fig.png')
plt.show()

x = np.linspace(0,2, 100)
y1 = x**2
y2 = x
plt.plot(x,y1,color='k', label='y1')
plt.plot(x, y2,color='b', label='y2')
plt.legend()
plt.show()


plt.scatter(presidents_df['height'],presidents_df['age'],marker='<',color='r')
plt.xlabel('height')
plt.ylabel('age')
plt.title('U.S. Presidents')
plt.savefig('plot.png')
plt.show()

presidents_df.plot(kind = 'scatter',x='height', y='age', title='US Presidents')
plt.savefig('plot.png')
plt.show()

presidents_df['height'].plot(kind='hist', title='height', bins=5)
plt.show()

print(presidents_df['height'].describe())
plt.style.use('classic')
presidents_df.boxplot(column='height')
plt.savefig('boxplot.png')
plt.show()

print(presidents_df['party'].value_counts())
party_cnt = presidents_df['party'].value_counts()
party_cnt.plot(kind='bar',color='b',x='Party', y='Presidency', title='Party Power Years')
plt.savefig('bargraph.png')
plt.show()