import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv('/content/sample_data/Salary_Data.csv')
print(data.columns)
x = data['yoe'].values 

y = data['salary'].values


xs = x.shape[0]
ys = y.shape[0]


mx = np.mean(x)

my = np.mean(y)


m=0
c=0

def gradient_descent(m,c,lr,epoch):

  for i in range(epoch):
    y_predicted = m*x+c
    m1 = -2*(np.mean((y-y_predicted)*x))
    c1 = -2*(np.mean((y-y_predicted)))

    m -=  lr * m1
    c -=  lr * c1

  return m,c


m,c = gradient_descent(m,c,0.01,1000)

print(f"Final slope (m): {m}")
print(f"Final intercept (c): {c}")


y_predicted = m*x+c
print(y_predicted)

mse = np.mean((y - y_predicted) ** 2)
print(f'mean squared error (mse) is : {mse}')


s1 = np.sum((y-y_predicted)**2)
s2 = np.sum((y-my)**2)
r2 = 1-(s1/s2)
print(f'the r_squared val is :{r2}')





plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.scatter(x,y_predicted, color='blue')
plt.plot(x,y_predicted,color = 'grey',linewidth='2')

plt.plot(mx,my,'g*',ms=10)

plt.grid(True)


plt.plot([x,x],[y,y_predicted],ls='dashed')

print(mx,my)

plt.scatter(x,y,marker='o')





plt.show()

