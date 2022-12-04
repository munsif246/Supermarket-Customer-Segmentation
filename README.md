# Supermarket Customer Segmentation

## Deployed web application

https://user-images.githubusercontent.com/83495853/205478511-a0180473-cf72-42d0-85bb-1ead36e2675d.mp4
## Introduction

Customer segmentation and marketing strategies are two key strategies to focus on the customer value for a business enterprise. Segmentation helps identify or reveal distinct groups of customers who think and function differently and follow varied approaches in their spending and purchasing habits. Analyzing customer behavior and categorization often help to understand the customer needs and identify the target market.

## Description of the question 

Businesses are increasing their expenditure on marketing strategies toachieve competitive advantage. Understanding customers prior to marketing or manufacturing and modifying products is essential for the survival of the business. Customer segmentation is one of the most used techniques to analyze customer behaviors. Results obtained from this analysis may help the organization to understand the characteristics of each customer segments.

## Dataset 
Source: https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis

## EDA

![ed2](https://user-images.githubusercontent.com/83495853/205257749-64826eee-38bb-4420-be7b-84b3dbcf5f28.png) ![ed2](https://user-images.githubusercontent.com/83495853/205257749-64826eee-38bb-4420-be7b-84b3dbcf5f28.png)

From the above plots, it can be observed that as the income increases, the total amount spent and the total number of purchases increase. It is obvious that people who earn more tend to spend more. 

![ed3](https://user-images.githubusercontent.com/83495853/205258283-a4ceca1e-8652-479c-b984-464a09ea47a2.png) ![ed4](https://user-images.githubusercontent.com/83495853/205258299-7c35c5aa-d264-4eb9-93de-518599e29879.png)

From the below plots we can observe that people with child are more likely to respond to deal purchases and Middle-aged and adult customers are also more willing to respond to deal purchases than the rest of the age groups.  

![ed5](https://user-images.githubusercontent.com/83495853/205258329-13dcc1e3-000c-444d-950f-9d0b0bb9ed89.png)

According to the correlation heat map income variable has positive linear relationships with Total spending and Total number of purchases.  Also, Total number of purchases and total spending variables are highly correlated.  


![rsz_picture1](https://user-images.githubusercontent.com/83495853/205260742-7151e048-3d5c-4d0a-b237-57daffce9db3.png) 50.2% of the Total amounts were spent on Wine in last 2 years. So wine is the most selling product in the company and it is followed by gold.

![Picture2](https://user-images.githubusercontent.com/83495853/205260906-b126d2b9-132f-45b9-8394-ab4b44ffd002.png) ![Picture3](https://user-images.githubusercontent.com/83495853/205261344-50d4fd78-068d-45c4-beb6-568c9292daa8.png) ![Picture4](https://user-images.githubusercontent.com/83495853/205261374-29539b17-6af8-475f-859f-e13afefe2e8a.png)

From the above plots itcan be said that More than 50% of the customers of the company are graduates but PHD holders have the highest average spending that the rest and also PHD holders more likely to respond to deal offers than the rest.

![rsz_1picture5](https://user-images.githubusercontent.com/83495853/205262259-c5347f38-a851-43ba-9447-0056da005725.png)

Customers with basic knowledge have less income as well as they spend less when compare to the graduate and post- graduate people. 

![Picture6](https://user-images.githubusercontent.com/83495853/205264648-da96cd02-41c1-4253-9892-82f9c19a45a6.png)

The incomes of seniors and young adults are higher than those of adults and middle-aged.

![Picture7](https://user-images.githubusercontent.com/83495853/205265135-01a5af51-39ac-4452-8033-980f0689901a.jpg)
Mean spending of customers who haven't complained at least once is pretty high than the who have complained. So we can conclude that customers who doesn't complain tendspend more on the company products.

## Clustering
### Latent Profile Analysis
<img src="https://user-images.githubusercontent.com/83495853/205266465-b146fb86-a34d-4de9-867d-f9711305c899.png" width="600" height="400"/>
Highest BIC value we got for model (VVV,3) this suggests that our dataset has 3 profiles that allows Varying variances and varying covariances across each profile

<img src="https://user-images.githubusercontent.com/83495853/205267272-6b00d630-e800-461b-bfa5-4c3b61c45660.png" width="600" height="400"/>

Profile 1- Average spending, average income, fairly small family size, moderately educated.

Profile 2 – high spending, highly educated, higher number of purchase, less children, small family size and with high income

Profile 3 – big family, not educated much, low spending and low income. 

### K-means Clustering

#### Finding Optimum Number of Clusters
<img src="https://user-images.githubusercontent.com/83495853/205268241-360ae9ab-cbe8-4bdd-9cfe-37b7eeb28eea.png" width="600" height="400"/>

Before clustering the dataset, we need to find the optimal number of clusters in the dataset. We used the disortion score to determine the number of clusters in this case. the greatest bend occurs at index 4, so we proceed the analysis with four clusters. 

## EDA on Clusters



