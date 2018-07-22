# Defaul Rate Prediction: Machine Learning

##### Data and Reference

The data set is from the https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients and the relevent paper is Yeh, I. C., & Lien, C. H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. Expert Systems with Applications, 36(2), 2473-2480.

##### Object 

This project uses Machine Learning algorithms such as logistic regression, artificial neural network, KNN, and SVM to compares the predictive accuracy of default rate.

The application of machine learning on results could be used to predict if the customer is credible or not credible clients for credit card application.

##### Variables

The dataset tracked the payment amount and status on credit car bills on each client from April to September 2015

The the response variable (Y) is  a binary variable, default payment (Yes = 1, No = 0).  The explanatory variables are :

X1: amount of the given credit (NT dollar): it includes both the individual consumer credit and his/her family (supplementary) credit.

X2: gender (1 = male; 2 = female). 

X3: education (1 = graduate school; 2 = university; 3 = high school; 4 = others). 

X4: marital status (1 = married; 2 = single; 3 = others). 

X5: age 

X6 - X11:  The measurement scale for the repayment status, 

X6 = the repayment status in September, 2005,

X7 = the repayment status in August, 2005,

....

X11 = the repayment status in April, 2005. 

*The measurement scale for the repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above.  is: -1 = pay duly, 1 = payment delay for one month, 2 = payment delay for two months……, 8 = payment delay for eight months*

X12-X17: "amount to bill statement" from April to September 2015

X12 = amount of bill statement in September, 2005,

X13 = amount of bill statement in August, 2005,

 ....

X17 = amount of bill statement in April, 2005. 

X18-X23: "amount paid to bill" form April to September 2015

X18 = amount paid in September, 2005,

X19 = amount paid in August, 2005,

.....

X23 = amount paid in April, 2005. 

##### Reference

"Many statistical methods, including discriminant analysis, logistic regression, Bayes classifier, and nearest neigh bor, have been used to develop models of risk prediction (Hand & Henley, 1997). With the evolution of artificial intelligence and machine learning, artificial neural net- works and classification trees were also employed to fore- cast credit risk (Koh & Chan, 2002; Thomas, 2000). Credit risk here means the probability of a delay in the repayment of the credit granted (Paolo, 2001)." (Yeh and Lien, 2009, p2473)

 



