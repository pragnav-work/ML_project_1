# Uber Eats Operational & Customer Intelligence System

## Trainee Data Analyst – ML Focus

**Duration:** 7 Days  
**Domain:** Food Delivery / Marketplace Analytics  
**Primary Focus:** Machine Learning, EDA, Feature Engineering, Model Evaluation, Business Interpretation

---

## 1. Project Overview

This project builds an end-to-end **Uber Eats Operational & Customer Intelligence System** using synthetic food-delivery marketplace data.

The objective is to simulate a real-world Data Analyst and Machine Learning workflow covering:

- Data generation
- Data understanding
- ETL and data cleaning
- Exploratory Data Analysis
- Feature engineering
- Customer segmentation
- Restaurant segmentation
- Customer sentiment analysis
- Delivery time prediction
- Tip amount prediction
- Hourly order demand forecasting
- Model evaluation
- Business interpretation

The project focuses not only on building machine learning models, but also on understanding the business problem, preparing the data, evaluating model performance, and translating the results into actionable recommendations.

---

## 2. Business Problem

A food-delivery marketplace generates large amounts of customer, restaurant, order, delivery, payment, and review data.

This data can be used to answer important business questions.

### Customer Intelligence

- What types of customers use the platform?
- Can customers be segmented based on their behavior?
- Which customer segments generate the most revenue?
- Which customers have high order frequency and spending?
- What factors are associated with higher tips?

### Restaurant Intelligence

- Which restaurant categories generate the most orders?
- Which cuisines perform best?
- How does restaurant rating affect customer behavior?
- Which restaurants generate the highest revenue?
- Which restaurants have operational or customer-experience issues?

### Delivery Operations

- What factors affect delivery time?
- How do traffic and weather affect delivery performance?
- Can actual delivery time be predicted?
- How does preparation time affect total delivery time?
- Which operational conditions result in delivery delays?

### Customer Experience

- What factors lead to positive or negative reviews?
- How does delivery performance affect customer sentiment?
- What are the most common negative customer experiences?

### Demand Forecasting

- What are the busiest hours of the day?
- When does order demand peak?
- Can hourly order demand be forecasted?
- How can driver and restaurant capacity be planned around expected demand?

---

## 3. Project Objective

The primary objective is to use machine learning and analytical techniques to:

1. Segment customers and restaurants.
2. Analyze customer sentiment.
3. Predict delivery time or tip amount.
4. Forecast hourly order demand.
5. Translate model outputs into actionable business recommendations.

---

## 4. Technology Stack

### Programming

- Python

### Data Manipulation

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn

### Natural Language Processing

- NLTK
- spaCy

### Statistical Analysis

- Statsmodels

### Time Series Forecasting

- Prophet
- Statsmodels

### Development

- Jupyter Notebook
- Python Virtual Environment

### Version Control

- Git
- GitHub

---

## 5. Project Structure

```text
ML_assignment_1/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── restaurants.csv
│   │   ├── orders.csv
│   │   ├── deliveries.csv
│   │   ├── drivers.csv
│   │   ├── reviews.csv
│   │   └── payments.csv
│   │
│   └── processed/
│
├── docs/
│   ├── data_dictionary.md
│   └── prompt_engineering.md
│
├── models/
│
├── notebooks/
│
├── outputs/
│
├── src/
│   └── generate_data.py
│
├── .gitignore
├── requirements.txt
└── ReadMe.md
````

---

## 6. Dataset Architecture

The project contains seven related datasets:

1. Customers
2. Restaurants
3. Orders
4. Deliveries
5. Drivers
6. Reviews
7. Payments

The main relationships are:

```text
Customers
    |
    | customer_id
    ↓
Orders
    |
    ├── restaurant_id → Restaurants
    |
    ├── order_id → Deliveries
    |                 |
    |                 └── driver_id → Drivers
    |
    ├── order_id → Payments
    |
    └── order_id → Reviews
```

---

## 7. Synthetic Data

The project uses synthetically generated data rather than real Uber Eats customer or operational data.

The synthetic data is generated using Python and Faker.

This approach allows the project to:

* Define the required schema.
* Control dataset size.
* Create relationships between tables.
* Introduce realistic business patterns.
* Reproduce the dataset using a fixed random seed.
* Avoid using real customer information.
* Create data specifically suited to the planned analytical and ML tasks.

The data-generation pipeline is located at:

```text
src/generate_data.py
```

---

## 8. Dataset Size

The current dataset configuration is:

| Dataset     | Approximate Rows |
| ----------- | ---------------: |
| Customers   |            1,500 |
| Restaurants |              200 |
| Drivers     |              300 |
| Orders      |           10,000 |
| Deliveries  |           ~9,200 |
| Reviews     |            7,500 |
| Payments    |           10,000 |

The dataset size was intentionally reduced from the initial 50,000-order design to keep machine learning experiments computationally manageable while still providing enough observations for meaningful analysis.

---

## 9. Dataset Description

### Customers

Contains customer demographic, location, signup, and membership information.

Main columns:

```text
customer_id
age
gender
city
signup_date
membership_type
```

### Restaurants

Contains restaurant information and pricing characteristics.

Main columns:

```text
restaurant_id
restaurant_name
city
cuisine
restaurant_category
restaurant_rating
average_price
```

### Drivers

Contains driver demographic, vehicle, experience, and rating information.

Main columns:

```text
driver_id
age
gender
vehicle_type
experience_years
driver_rating
```

### Orders

Contains the main transaction-level information.

Main columns:

```text
order_id
customer_id
restaurant_id
order_timestamp
order_status
order_amount
tip_amount
items_count
payment_method
weather
traffic_condition
```

### Deliveries

Contains delivery and operational information.

Main columns:

```text
delivery_id
order_id
driver_id
delivery_distance_km
preparation_time_min
estimated_delivery_time_min
actual_delivery_time_min
```

### Reviews

Contains customer feedback and sentiment information.

Main columns:

```text
review_id
order_id
customer_id
restaurant_id
review_rating
review_text
sentiment
```

### Payments

Contains payment transaction information.

Main columns:

```text
payment_id
order_id
payment_method
payment_status
transaction_amount
```

---

## 10. Data Generation

The synthetic datasets are generated through:

```text
src/generate_data.py
```

Run the generator from the project root:

```bash
python src/generate_data.py
```

The script performs the following workflow:

```text
Generate Customers
        ↓
Generate Restaurants
        ↓
Generate Drivers
        ↓
Generate Orders
        ↓
Generate Deliveries
        ↓
Generate Payments
        ↓
Generate Reviews
        ↓
Validate Data
        ↓
Export CSV Files
```

The generated files are stored in:

```text
data/raw/
```

---

## 11. Reproducibility

The data-generation script uses a fixed random seed:

```python
SEED = 42
```

The Faker library is also seeded.

This allows the synthetic data-generation process to be reproduced consistently.

---

## 12. Data Relationships

The datasets are connected through primary and foreign keys.

### Customer → Orders

```text
customers.customer_id
        ↓
orders.customer_id
```

### Restaurant → Orders

```text
restaurants.restaurant_id
        ↓
orders.restaurant_id
```

### Order → Delivery

```text
orders.order_id
        ↓
deliveries.order_id
```

### Driver → Delivery

```text
drivers.driver_id
        ↓
deliveries.driver_id
```

### Order → Payment

```text
orders.order_id
        ↓
payments.order_id
```

### Order → Review

```text
orders.order_id
        ↓
reviews.order_id
```

---

## 13. Data Validation

The data-generation pipeline includes validation checks before exporting the datasets.

Validation covers:

* Primary key uniqueness
* Missing primary keys
* Foreign key validity
* Customer age ranges
* Restaurant rating ranges
* Driver rating ranges
* Driver experience
* Restaurant prices
* Order amounts
* Tip amounts
* Delivery distances
* Preparation times
* Delivery times
* Review ratings
* Customer signup dates
* Delivery consistency
* Review consistency
* Payment amount consistency

The generator raises an error if validation fails.

This prevents invalid relational data from being exported.

---

# 14. Machine Learning Plan

The project contains multiple machine learning and analytical tasks.

---

## 14.1 Customer Segmentation

### Objective

Segment customers based on their behavior and transaction history.

Potential features include:

* Order frequency
* Total spending
* Average order value
* Average tip
* Recency
* Membership type
* Ordering frequency

Potential algorithms:

```text
K-Means Clustering
Agglomerative Clustering
```

Potential business applications:

* Identify high-value customers.
* Identify frequent customers.
* Identify occasional customers.
* Design targeted promotions.
* Develop customer retention strategies.

---

## 14.2 Restaurant Segmentation

### Objective

Group restaurants based on business and operational characteristics.

Potential features include:

* Order volume
* Revenue
* Average order value
* Restaurant rating
* Cuisine
* Delivery performance
* Customer sentiment

Potential algorithms:

```text
K-Means Clustering
Agglomerative Clustering
```

Potential business applications:

* Identify high-performing restaurants.
* Identify restaurants requiring operational support.
* Compare restaurant categories.
* Improve restaurant partner strategies.

---

# 15. Customer Sentiment Analysis

### Objective

Analyze customer reviews and classify customer sentiment.

Primary input:

```text
review_text
```

Target:

```text
sentiment
```

Potential workflow:

```text
Raw Review
    ↓
Text Cleaning
    ↓
Tokenization
    ↓
Stopword Removal
    ↓
Feature Extraction
    ↓
TF-IDF
    ↓
Classification Model
    ↓
Sentiment Prediction
```

Potential models:

* Logistic Regression
* Naive Bayes

Potential evaluation metrics:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

# 16. Delivery Time Prediction

### Objective

Predict the actual delivery time for an order.

Target variable:

```text
actual_delivery_time_min
```

Potential features:

* Delivery distance
* Preparation time
* Weather
* Traffic condition
* Driver experience
* Driver rating
* Order amount
* Restaurant characteristics

Potential models:

```text
Linear Regression
Random Forest Regression
```

Potential evaluation metrics:

* MAE
* RMSE
* R²
* MAPE

Business application:

A reliable delivery-time prediction model can improve ETA accuracy and help the platform plan delivery capacity.

---

# 17. Tip Amount Prediction

An alternative regression problem is predicting:

```text
tip_amount
```

Potential features:

* Order amount
* Delivery distance
* Weather
* Traffic
* Membership type
* Delivery performance
* Restaurant category

Potential models:

```text
Linear Regression
Random Forest Regression
```

The final regression target will be selected based on data quality and analytical suitability.

---

# 18. Hourly Demand Forecasting

### Objective

Forecast the number of orders expected during future hours.

The `order_timestamp` field will be transformed into an hourly time series.

Potential forecasting approaches:

```text
ARIMA
ETS
Prophet
```

Potential evaluation metrics:

* MAE
* RMSE
* MAPE

Business applications:

* Driver allocation
* Restaurant staffing
* Peak-hour capacity planning
* Operational resource planning
* Demand prediction

---

# 19. Exploratory Data Analysis

EDA will be performed before machine learning.

### Customer Analysis

Potential questions:

* How are customers distributed across cities?
* What is the membership distribution?
* Which customer groups place the most orders?
* Which customers generate the most revenue?

### Restaurant Analysis

Potential questions:

* Which cuisines receive the most orders?
* Which restaurant categories generate the most revenue?
* Does restaurant rating affect order volume?
* Which restaurants perform best?

### Delivery Analysis

Potential questions:

* What is the distribution of delivery time?
* How does distance affect delivery time?
* How does traffic affect delivery time?
* How does weather affect delivery time?
* How does preparation time affect delivery time?

### Review Analysis

Potential questions:

* What percentage of reviews are positive, neutral, and negative?
* Which factors are associated with negative reviews?
* Does delivery delay affect customer sentiment?

### Demand Analysis

Potential questions:

* What are the busiest hours?
* What are the busiest days?
* What are the peak ordering periods?
* How does demand change over time?

---

# 20. Feature Engineering

Features will be created from the raw datasets based on EDA findings and modeling requirements.

Potential features include:

```text
order_hour
order_day
order_day_of_week
order_month
is_weekend
delivery_delay
delivery_speed
tip_percentage
average_order_value
customer_order_count
customer_total_spend
customer_average_spend
restaurant_order_count
restaurant_revenue
```

Feature engineering will be performed after understanding the underlying data and relationships.

---

# 21. Model Evaluation

Different evaluation metrics will be used depending on the machine learning problem.

### Regression

```text
MAE
RMSE
R²
MAPE
```

### Classification

```text
Accuracy
Precision
Recall
F1-score
Confusion Matrix
```

### Clustering

```text
Silhouette Score
Adjusted Rand Index
```

### Forecasting

```text
MAE
RMSE
MAPE
```

Model selection will be based on both performance metrics and business interpretability.

---

# 22. Business Interpretation

The final objective is to convert analytical and machine learning results into business recommendations.

Examples:

### Customer Segmentation

If a high-value customer segment is identified:

> Develop targeted loyalty campaigns and personalized offers for high-frequency, high-spending customers.

### Delivery Time Prediction

If traffic and delivery distance are major contributors to delivery time:

> Improve driver allocation and ETA estimates during high-traffic periods.

### Sentiment Analysis

If negative sentiment is strongly associated with delivery delays:

> Prioritize improvements in delivery reliability and operational efficiency.

### Demand Forecasting

If evening demand consistently peaks:

> Increase driver availability and restaurant capacity during peak evening hours.

---

# 23. Git Workflow

The project uses Git for version control.

Development branch:

```text
feature/uber-eats-pipeline
```

Typical workflow:

```bash
git status
git add .
git commit -m 'descriptive commit message'
git push
```

Meaningful commits will be used throughout the project to track major milestones.

---

# 24. Prompt Engineering

Synthetic data generation was supported through prompt engineering.

The project uses:

* P.T.C.F. prompting
* Few-shot prompting
* Role-based prompting
* Structured output prompting

The prompt engineering process and the exact prompt used to generate the data-generation script are documented in:

```text
docs/prompt_engineering.md
```

---

# 25. Documentation

Project documentation is maintained in the `docs/` directory.

### Data Dictionary

```text
docs/data_dictionary.md
```

Contains:

* Dataset descriptions
* Column definitions
* Data types
* Expected values
* Business meaning

### Prompt Engineering

```text
docs/prompt_engineering.md
```

Contains:

* Prompting techniques used
* P.T.C.F. framework
* Few-shot examples
* Role-based prompting
* Structured output requirements
* Exact prompt used for data generation

---

# 26. Seven-Day Project Plan

## Day 1 — Project Setup & Synthetic Data Generation

* Git setup
* Git configuration
* Project structure
* Requirements
* Prompt engineering
* Dataset schema design
* Synthetic data generation
* Data validation
* Data dictionary
* Initial Git commit

## Day 2 — Data Understanding, ETL & EDA

* Load datasets
* Inspect schemas
* Check missing values
* Check duplicates
* Check data types
* Validate relationships
* Clean datasets
* Perform exploratory data analysis
* Identify important business patterns

## Day 3 — Feature Engineering & Segmentation

* Create customer-level features
* Create restaurant-level features
* Scale numerical features
* Customer segmentation
* Restaurant segmentation
* Evaluate clustering models
* Interpret customer and restaurant segments

## Day 4 — Sentiment Analysis

* Clean review text
* Perform NLP preprocessing
* Feature extraction
* Build sentiment classification models
* Evaluate classification performance
* Analyze negative and positive customer experiences

## Day 5 — Predictive Modeling

* Select prediction target
* Create training features
* Train regression models
* Compare models
* Evaluate MAE, RMSE, R² and MAPE
* Identify important features
* Interpret business implications

## Day 6 — Demand Forecasting

* Aggregate orders by hour
* Analyze time-series patterns
* Build forecasting models
* Compare forecasting approaches
* Evaluate forecast accuracy
* Identify peak-demand periods

## Day 7 — Final Analysis & Business Recommendations

* Consolidate model results
* Compare model performance
* Identify key findings
* Develop business recommendations
* Prepare final outputs
* Clean notebooks
* Update documentation
* Final Git commit
* Prepare project presentation

---

# 27. End-to-End Workflow

```text
Business Problem
       ↓
Project Setup
       ↓
Synthetic Data Generation
       ↓
Data Validation
       ↓
Data Understanding
       ↓
ETL / Data Cleaning
       ↓
EDA
       ↓
Feature Engineering
       ↓
Machine Learning
       ↓
Model Evaluation
       ↓
Business Interpretation
       ↓
Actionable Recommendations
```

---

# 28. Current Status

## Day 1

* [x] Git repository initialized
* [x] Git identity configured
* [x] Feature branch created
* [x] Project folder structure created
* [x] Requirements file created
* [x] Synthetic data schema designed
* [x] Data-generation script created
* [x] Prompt engineering documentation created
* [ ] Synthetic CSV datasets generated
* [ ] Data dictionary finalized
* [ ] Data validation completed
* [ ] Initial Git commit

---

# 29. Expected Final Deliverables

At the end of the seven-day project, the repository is expected to contain:

* Synthetic datasets
* Data-generation Python script
* Data dictionary
* Prompt engineering documentation
* ETL notebooks/scripts
* EDA notebooks
* Feature engineering notebooks
* Customer segmentation model
* Restaurant segmentation model
* Sentiment analysis model
* Regression model
* Demand forecasting model
* Model evaluation results
* Business recommendations
* Final project documentation

---

# 30. Project Goal

The overall goal is to demonstrate an end-to-end Data Analyst workflow:

**Understand the business → Prepare the data → Analyze the data → Engineer useful features → Build machine learning models → Evaluate them → Interpret the results → Recommend business actions.**

The project therefore focuses not only on machine learning accuracy, but also on data quality, analytical reasoning, model evaluation, and business impact.

```
```
