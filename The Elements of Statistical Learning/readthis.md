 <h2 align="center">The Elements of Statistical Learning</h2>
  <p align="center">
    Foundational reading on statistical methods for machine learning. Lays the groundwork for everything else...
    <br />
    <br />
 
 # Disclaimer
 Formulas are rendered as white text (because dark mode rocks!). If you are on light mode, you won't be able to see the formulas.
 
 # Chapter 2
 ## 2.1
 **Supervised Learning** -> Using input-output pairs (dataset) to map inputs to outputs (coming up with a function that does this)
 ## 2.2 Variable Types and Terminology
 **Regression** -> Predicting quantitative outputs
 **Classification** -> Predicting qualitative outputs
 **Inputs** denoted by `X`, **Quantitative Outputs** by 	`Y` or `y`and **Qualitative Outputs** by `G` or by `Y` in some range (ex. `[0, 1]` for binary classification where `Y < 0.5` will correspond to a label in `G`
 ## 2.3 Two Simple Approached: Least Squares and Nearest Neighbours
 ### 2.3.1 Linear Models and Least Squares
 Given a vector of inputs `X^T = (X1, X2, ..., Xp)`, the output `Y` via the model: 


![Equation](https://latex.codecogs.com/svg.image?%5Cbg%7Bwhite%7D%5Ccolor%7Bwhite%7D%5Chat%7BY%7D%20=%20%5Chat%7B%5Cbeta%7D_0%20&plus;%20%5Csum_%7Bj=1%7D%5E%7Bp%7D%20X_j%20%5Chat%7B%5Cbeta%7D_j)
or equivalently ![Equation](https://latex.codecogs.com/svg.image?%5Cbg%7Bwhite%7D%5Ccolor%7Bwhite%7D%5Chat%7BY%7D%20=%20X%5ET%5Chat%7B%5Cbeta%7D)

where $\hat{\beta}_0$ is the intercept, or **bias** as it is known in ML.

To fit a linear model to a set of training data, the most popular method is **Least Square**, as given by the following formula:

![Equation](https://latex.codecogs.com/svg.image?%5Cbg%7Bwhite%7D%5Ccolor%7Bwhite%7DRSS(%7B%5Cbeta%7D)%20=%20%5Csum_%7Bi=1%7D%5E%7BN%7D(y_i-x_i%5ET%7B%5Cbeta%7D)%5E2)

Example Least Squares classification:
 
 ![img 1](<Images/Img1.png>)
 
### 2.3.2 Nearest-Neighbor Methods
 The object is classified using a vote of it's neighbors and is assigned to the class most common among its k nearest neighbors (k is a positive integer, typically small). If k = 1, then the object is simply assigned to the class of that single nearest neighbor.


# This book is quite dense so I may or may not come back to it. Reading 'An Introduction to Statistical
Learning' by the same authors instead
