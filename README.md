# Software Engineer Salary Estimator: Project Overview
* Created a tool that estimates software engineer salaries to help software engineers negotiate their income when they get a job.
* Scrapped over 1000 job descriptions from Glassdoor using Python and Selenium
* Engineered features from the text of each job description to quantify the value companies put on Java, Python, Back-end, Web Developer, Mobile Developer, etc.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
## Code and Resources Used

* **Python Version**: 3.7
* **Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium
* **For Web Framework Requirements:** pip install -r requirements.txt
* **Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium
* **Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
* **Idea of the project based on:** https://github.com/PlayingNumbers/ds_salary_proj

## Web Scrapping

Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:

* Job title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Headquarters
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

![1](https://user-images.githubusercontent.com/30380242/93692468-40a36300-fb26-11ea-98a6-f819ff1523f8.png)


## Data Cleaning

After scraping the data, we make changes and create some new variables to clean up the data:

* Parsed numeric data out of salary
* Parsed rating out of company text
* Transformed founded data into age of company
* Made columns for different categories in the job description:
  * Java
  * Python
  * Back-end
  * Web Developer
  * Mobile Developer
  * AWS

* Created a new column for description length

## EDA

We have a look at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.

![2](https://user-images.githubusercontent.com/30380242/93692518-e2c34b00-fb26-11ea-82bc-ec57893e70e7.png)

## Model Building

Firstly, we transform the categorical variables into dummy variables, then split the data into train and test sets with the train size of 80%

We use three models:

* **Multiple Linear Regression**
* **Lasso Regression**
* **Random Forest**

## Model performance

The Random Forest model is outstanding among three models on the test and validation sets.

* **Random Forest**: 
* **Linear Regression**: 
* **Ridge Regression**: 

