 <h2 align="center">The Elements of Statistical Learning</h2>
  <p align="center">
    Foundational reading on statistical methods for machine learning. Lays the groundwork for everything else...
    <br />
    <br />
 
 # Chapter 2
 ## 2.1
 **Supervised Learning** -> Using input-output pairs (dataset) to map inputs to outputs (coming up with a function that does this)
 ## 2.2 Variable Types and Terminology
 **Regression** -> Predicting quantitative outputs
 
 **Classification** -> Predicting qualitative outputs
 
 **Inputs** denoted by `X`, **Quantitative Outputs** by 	`Y` or `y`and **Qualitative Outputs** by `G` or by `Y` in some range (ex. `[0, 1]` for binary classification where `Y < 0.5` will correspond to a label in `G`
 
 ## 2.3 Two Simple Approached: Least Squares and Nearest Neighbours
 ### 2.3.1 Linear Models and Least Squares
 Given a vector of inputs $X^T = (X_1, X_2, ..., X_p)$, the output `Y` is via the model: 
![equation](https://latex.codecogs.com/svg.image?%5Cbg%7Bwhite%7D%5Chat%7BY%7D%20=%20%5Chat%7B%5Cbeta%7D_0%20&plus;%20%5Csum_%7Bj=1%7D%5E%7Bp%7D%20X_j%20%5Chat%7B%5Cbeta%7D_j)
  where $\hat{\beta}_0$ is the intercept, or **bias** as it is known in ML
