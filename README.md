# Lending case study

A consumer finance company which specialises in lending various types of loans would like to design a model which help the company has to make a decision for loan approval based on the applicant’s profile. 
Two types of risks are associated with the bank’s decision:

If the applicant is likely to repay the loan, then not approving the loan results in a loss of business to the company
If the applicant is not likely to repay the loan, i.e. he/she is likely to default, then approving the loan may lead to a financial loss for the company.

Now this would require a preliminary understanding of the features that define whether applicant's loan should be accepted or rejected.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Conclusions](#conclusions)
* [Acknowledgements](#acknowledgements)

<!-- You can include any other section that is pertinent to your problem -->

## General Information
- Data set contain 39717 rows and 111 columns
- 111 attributes includes:
	applicant relevant information
	Loan characteristics
	Customer behavior variables


<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

## Conclusions
- Annual income - Applicant with lesser income tend to default especially in the range of 0-25K. Income with more than 100K are good and 50-100K are moderate.
- Term – Rate of defaulters increase with the term. As the length of period is more, there could be many factors coming with time which could give more chance for defaulting.
- Interest rate - Applicant with interest rate greater than 15% are more likely to default.
- Home ownership – Home ownership is relatively not affecting the defaulters count.
- DTI: Applicant with lower DTI score are preferrable. Customer falling under 16-25% highly risky applicants.
- Grade – It is clear from analysis that with the loan amount, grade increases, which inturn increase the interest rate, so LC should be careful while granting loans with higher grade(A?G)
- Sub-grade: Same as grade
- Address State: Among the top business states(based on maximum applicants), highest defaulters are from FL.  Order: FL>CA>MD>GA>NJ>WA>AZ>NY>IL>OH>VA>PA>MA>TX
- Purpose: LC should be careful while granding loan to "small business" have higher defaulters. 
- Portion of loan amount to annual income: As per analysis, LC also should make sure the portion of the loan amount doesnot exceed 20-40% of the annual salary irrespective of term.



<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- Jupyter notebook - version 6.4.12
- Python - version 3.10.0
- Pandas - version 2.0
- Numpy - version 1.24.2
- Matplotlib.pyplot - version - 3.7.1
- seaborn - version - 0.12.2

<!-- As the libraries versions keep on changing, it is recommended to mention the version of library used in this project -->

## Acknowledgements
Give credit here.
- seaborn documentation
- Google in general


## Contact
Created by [suryabandari247@githubusername] - feel free to contact me!



<!-- You don't have to include all sections - just the one's relevant to your project -->