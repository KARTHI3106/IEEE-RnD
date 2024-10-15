import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv('/content/sample_data/Salary_Data.csv')
print(data.columns)
x = data['yoe'].values #years_of_experience

y = data['salary'].values

xs = x.shape[0]
xy = y.shape[0]

mx = np.mean(x)

my = np.mean(y)


m, c = np.polyfit(x, y, 1)  # Degree 1 for linear regression
y_predicted = m*x+c

print('slope and intercept is : ',m,c)

mse = np.mean((y - y_predicted) ** 2)
print(f'mean squared error (mse) is : {mse}')




s1 = np.sum((y-y_predicted)**2)
s2 = np.sum((y-my)**2)
r2 = 1-(s1/s2)
print(f'the r_squared val is :{r2}')


plt.scatter(x,y_predicted, color='red')
plt.plot(x,y_predicted,color = 'grey',linewidth='2')

plt.plot(mx,my,'g*',ms=10)



plt.plot([x,x],[y,y_predicted],ls='dashed')

print(f'the mean of experince and salary {mx,my}')

plt.scatter(x,y,marker='o')





plt.show()

