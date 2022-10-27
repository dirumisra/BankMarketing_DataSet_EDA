##### EDA Process on Bank Marketing Data 

##### Supporting Documents Link

#### https://seaborn.pydata.org/generated/seaborn.boxplot.html
#### https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/style.html

______________________________________________________________________________________________________________________________________________________________________

### Bank Telemarketing Campaign Case Study.

In this case study you’ll be learning Exploratory Data Analytics with the help of a case study on "Bank marketing campaign". This will enable you to understand why EDA is a most important step in the process of Machine Learning.

______________________________________________________________________________________________________________________________________________________________________

### Problem Statement

The bank provides financial services/products such as savings accounts, current accounts, debit cards, etc. to its customers. In order to increase its overall revenue, the bank conducts various marketing campaigns for its financial products such as credit cards, term deposits, loans, etc. These campaigns are intended for the bank’s existing customers. However, the marketing campaigns need to be cost-efficient so that the bank not only increases their overall revenues but also the total profit. You need to apply your knowledge of EDA on the given dataset to analyse the patterns and provide inferences/solutions for the future marketing campaign.

The bank conducted a telemarketing campaign for one of its financial products ‘Term Deposits’ to help foster long-term relationships with existing customers. The dataset contains information about all the customers who were contacted during a particular year to open term deposit accounts.

______________________________________________________________________________________________________________________________________________________________________

### What is the term Deposit?

Term deposits also called fixed deposits, are the cash investments made for a specific time period ranging from 1 month to 5 years for predetermined fixed interest rates. The fixed interest rates offered for term deposits are higher than the regular interest rates for savings accounts. The customers receive the total amount (investment plus the interest) at the end of the maturity period. Also, the money can only be withdrawn at the end of the maturity period. Withdrawing money before that will result in an added penalty associated, and the customer will not receive any interest returns.

______________________________________________________________________________________________________________________________________________________________________


### Take aways from the lecture on missing values:

  - Set values as missing values**: Identify values that indicate missing data, for example, treat blank strings, "NA", "XX", "999", etc., as missing.
  - Adding is good, exaggerating is bad**: You should try to get information from reliable external sources as much as possible, but if you can’t, then it is better to retain missing values rather than exaggerating the existing rows/columns.
  - Delete rows and columns**: Rows can be deleted if the number of missing values is insignificant, as this would not impact the overall analysis results. Columns can be removed if the missing values are quite significant in number.
  - Fill partial missing values using business judgement**: Such values include missing time zone, century, etc. These values can be identified easily.

### Types of missing values:
  - MCAR : It stands for Missing completely at random (the reason behind the missing value is not dependent on any other feature).
  - MAR : It stands for Missing at random (the reason behind the missing value may be associated with some other features).
  - MNAR : It stands for Missing not at random (there is a specific reason behind the missing value).

Your target is to do end to end EDA on this bank telemarketing campaign data set to infer knowledge that where bank has to put more effort to improve it's positive response rate. 

______________________________________________________________________________________________________________________________________________________________________

There are multiple types of data types available in the data set. some of them are numerical type and some of categorical type. You are required to get the idea about the data types after reading the data frame. 

### Following are the some of the types of variables:
  - Numeric data type**: banking dataset: salary, balance, duration and age.
  - Categorical data type**: banking dataset: education, job, marital, poutcome and month etc.
  - Ordinal data type**: banking dataset: Age group.
  - Time and date type** 
  - Coordinates type of data**: latitude and longitude type.


### Checklist for fixing rows:

  - Delete summary rows**: Total and Subtotal rows
  - Delete incorrect rows**: Header row and footer row
  - Delete extra rows**: Column number, indicators, Blank rows, Page No.

### Checklist for fixing columns:

  - Merge columns for creating unique identifiers**, if needed, for example, merge the columns State and City into the column Full address.
  - Split columns to get more data**: Split the Address column to get State and City columns to analyse each separately. 
  - Add column names**: Add column names if missing.
  - Rename columns consistently**: Abbreviations, encoded columns.
  - Delete columns**: Delete unnecessary columns.
  - Align misaligned columns**: The data set may have shifted columns, which you need to align correctly.
______________________________________________________________________________________________________________________________________________________________________
