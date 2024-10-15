# IEEE-RnD
**Linear Regression Model**



Implementation of linear regression model and then optimizing the same using Gradient Descent Algorithm.


Inside folder src , there are 3 files 
1) IEEE_reg.py # file before using gradient descent
2) IEEE_reg_gradient.py # after gradient descent
3) linear_regression.ipynb


# **Installation**

The code can be run either using google colab or jupyter in the cloud or can be used locally in your system

Make sure to download these packages :
1) Numpy
2) Matplotlib
3) Pandas

To install these use this command in your terminal

  ```
   pip install numpy
   pip install pandas
   pip install matplotlib
  ```
To use the file locally on your system :

1) Clone or Download the file .
   To clone it . Make sure git is installed
   ```
   gh repo clone KARTHI3106/IEEE-RnD
   ```
2) Run these files

  IEEE_reg.py
  IEEE_reg_gradient.py




# **Approach**

In this project, i've implemented a simple linear regression model to predict salaries based on years of experience using both the numpy library and gradient descent optimization. The steps are as follows:


Feeding the Dataset :

The dataset containing salaries and years of experience is loaded from a CSV file using the pandas library.

Extracting data :

Extracted  x,y (column : years of experince vs salary) from the dataset.

Calculated the mean values of x and y for visualization purposes.


Gradient Descent Algorithm:

Initialized the slope (m) and intercept (c) to zero.
Defined a gradient_descent function that iteratively updates the values of m and c based on the learning rate and the number of epochs.
In each iteration, the predicted values are calculated, and the gradients for m and c are computed. The values are then updated accordingly.
Model Evaluation:

After training the model using gradient descent, predicted salaries were calculated.
The mean squared error (MSE) and R-squared value were computed to evaluate the model's performance.

Visualization:

Plotted the original data points and the regression line to visualize the model's predictions against actual salaries.


Testing Different Learning Rates:

Experimented with various learning rates and epochs to observe their impact on the regression line and model accuracy.
By following this structured approach, we were able to implement and visualize a basic linear regression model effectively.


Possible Errors :
1) File Path  - Make sure the file path is correct . 
2) Column Names - The column names in the code file and the csv file should match . 
3) Shape Mismatch - The size of columns should match .



