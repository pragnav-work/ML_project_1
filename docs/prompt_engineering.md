# Prompt Engineering Documentation

## 1. Purpose

Prompt engineering was used during Day 1 to generate the Python script responsible for creating the synthetic Uber Eats datasets.

The objective was to provide an LLM with enough context about the project, dataset requirements, relationships, realism constraints, and expected code structure so that it could generate a reusable Python data-generation script.

The generated script was then reviewed and modified to fit the project's requirements.

---

# 2. Prompt Engineering Techniques Used

The following prompting techniques were used:

- P.T.C.F. Framework
- Role-Based Prompting
- Few-Shot Prompting
- Structured Output Prompting

---

# 3. P.T.C.F. Framework

P.T.C.F. stands for:

- Persona
- Task
- Context
- Format

## Persona

The model was given the role of an experienced Python Data Engineer / Data Analyst who understands synthetic data generation, relational datasets, and machine learning requirements.

This helps guide the model toward producing code that is suitable for an analytical and machine learning project rather than generic sample data.

## Task

The model was explicitly asked to create a Python script that generates synthetic Uber Eats marketplace data.

The script needed to generate multiple related datasets:

- Customers
- Restaurants
- Orders
- Deliveries
- Drivers
- Reviews
- Payments

## Context

The prompt provided the business domain, project objective, required features, relationships between datasets, expected dataset sizes, and downstream machine learning use cases.

The generated data needed to support:

- Customer segmentation
- Restaurant segmentation
- Sentiment analysis
- Delivery-time prediction
- Tip prediction
- Demand forecasting

## Format

The model was instructed to return a complete Python script with:

- Imports
- Configuration
- Constants
- Dataset generation functions
- Validation
- CSV export
- Main execution logic
- Comments explaining the code

The script was expected to be directly usable as:

```text
src/generate_data.py
````

---

# 4. Role-Based Prompting

The prompt assigned the model a specific professional role.

Example:

> Act as an experienced Python Data Engineer and Data Analyst specializing in synthetic marketplace data generation and machine learning datasets.

The purpose of role-based prompting was to encourage the model to consider:

* Data relationships
* Realistic distributions
* Referential integrity
* Business logic
* Machine learning requirements
* Reproducibility
* Data validation

---

# 5. Few-Shot Prompting

Few-shot prompting was used by providing examples of the expected structure and characteristics of the generated data.

For example, the prompt specified example categories such as:

```text
Restaurant Categories:
Budget
Mid-range
Premium
```

Example weather conditions:

```text
Clear
Cloudy
Rain
Heavy Rain
```

Example traffic conditions:

```text
Low
Medium
High
Severe
```

Example review sentiment:

```text
Positive
Neutral
Negative
```

These examples helped define the expected format and vocabulary of the synthetic data.

---

# 6. Structured Output Prompting

The model was instructed to organize the generated Python script into clearly separated sections.

The expected structure was:

```text
Imports
Configuration
Random Seed
Output Directory
Reference Categories
Customer Generation
Restaurant Generation
Driver Generation
Order Generation
Delivery Generation
Payment Generation
Review Generation
Validation
CSV Export
Main Execution
```

This made the generated code easier to inspect, modify, and maintain.

---

# 7. Data Generation Requirements

The prompt instructed the model to generate seven related datasets.

## Customers

Required characteristics included:

* Customer ID
* Age
* Gender
* City
* Signup date
* Membership type

## Restaurants

Required characteristics included:

* Restaurant ID
* Restaurant name
* City
* Cuisine
* Restaurant category
* Restaurant rating
* Average price

## Orders

Required characteristics included:

* Order ID
* Customer ID
* Restaurant ID
* Order timestamp
* Order status
* Order amount
* Tip amount
* Number of items
* Payment method
* Weather
* Traffic condition

## Deliveries

Required characteristics included:

* Delivery ID
* Order ID
* Driver ID
* Delivery distance
* Preparation time
* Estimated delivery time
* Actual delivery time

## Drivers

Required characteristics included:

* Driver ID
* Age
* Gender
* Vehicle type
* Experience
* Driver rating

## Reviews

Required characteristics included:

* Review ID
* Order ID
* Customer ID
* Restaurant ID
* Review rating
* Review text
* Sentiment

## Payments

Required characteristics included:

* Payment ID
* Order ID
* Payment method
* Payment status
* Transaction amount

---

# 8. Realism Requirements

The prompt instructed the model to create data that represents realistic food-delivery marketplace behavior rather than generating completely independent random values.

Examples of relationships requested included:

* Premium restaurants should generally have higher average prices.
* Customer membership should influence ordering behavior.
* Order amount should depend on restaurant pricing and number of items.
* Delivery time should depend on distance, preparation time, traffic, weather, and driver experience.
* Tips should be associated with order value and delivery conditions.
* Review ratings should have a relationship with delivery performance.
* Cancelled or failed orders should not have delivery records.
* Reviews should reference delivered orders.
* Payments should reference valid orders.

---

# 9. Reproducibility

The prompt required the use of a fixed random seed.

The generated script uses:

```python
SEED = 42
```

The Faker instance is also seeded.

This allows the synthetic dataset to be reproduced consistently.

---

# 10. Data Validation

The prompt required the generated script to include validation checks.

The validation process checks:

* Primary key uniqueness
* Missing primary keys
* Foreign key relationships
* Valid age ranges
* Valid rating ranges
* Positive transaction amounts
* Positive delivery distances
* Valid delivery times
* Valid review ratings
* Customer signup dates
* Delivery consistency
* Review consistency
* Payment amount consistency

The purpose is to ensure that the generated data can be safely used in later ETL, EDA, and machine learning stages.

---

# 11. Iterative Prompting

The first generated version of the script was reviewed instead of being accepted blindly.

The script was checked for:

* Data realism
* Relationships between datasets
* Machine learning suitability
* Validation logic
* Dataset size
* Code organization
* Computational efficiency

Based on the review, corrections were requested from the LLM.

The dataset size was subsequently reduced because the original 50,000-order dataset was considered unnecessarily large for the planned machine learning experiments.

The final configuration uses approximately:

```text
Customers:    1,500
Restaurants:    200
Drivers:        300
Orders:      10,000
Reviews:      7,500
```

This provides enough observations for analysis while keeping model training computationally manageable.

---

# 12. Exact Prompt Used

The following is the exact prompt used to generate the Python data-generation script:

```text
Act as an experienced Python Data Engineer and Data Analyst specializing in synthetic data generation, marketplace analytics, and machine learning datasets.

I am working on a 7-day Trainee Data Analyst – ML Focus project.

Project:
Build an end-to-end Uber Eats Operational & Customer Intelligence System.

Domain:
Food Delivery / Marketplace Analytics.

The project will eventually perform:

1. Customer segmentation
2. Restaurant segmentation
3. Customer sentiment analysis
4. Delivery time prediction or tip amount prediction
5. Hourly order demand forecasting
6. Business interpretation and recommendations

I need you to create a complete Python script that generates realistic synthetic data for this project.

Use Python, Pandas, NumPy, and Faker.

The script should generate seven related CSV datasets:

1. Customers
2. Restaurants
3. Orders
4. Deliveries
5. Drivers
6. Reviews
7. Payments

The datasets must have realistic relationships and valid primary-key and foreign-key relationships.

CUSTOMERS

Create a customer dataset containing:

- customer_id
- age
- gender
- city
- signup_date
- membership_type

Use realistic Indian cities and realistic customer demographics.

RESTAURANTS

Create a restaurant dataset containing:

- restaurant_id
- restaurant_name
- city
- cuisine
- restaurant_category
- restaurant_rating
- average_price

Use realistic cuisine categories and restaurant categories such as Budget, Mid-range, and Premium.

Premium restaurants should generally have higher average prices.

DRIVERS

Create a driver dataset containing:

- driver_id
- age
- gender
- vehicle_type
- experience_years
- driver_rating

Driver experience must be logically related to driver age.

ORDERS

Create an orders dataset containing:

- order_id
- customer_id
- restaurant_id
- order_timestamp
- order_status
- order_amount
- tip_amount
- items_count
- payment_method
- weather
- traffic_condition

Use realistic order statuses such as:

- Delivered
- Cancelled
- Failed

Use realistic weather conditions:

- Clear
- Cloudy
- Rain
- Heavy Rain

Use realistic traffic conditions:

- Low
- Medium
- High
- Severe

Order amounts should depend on restaurant category, restaurant pricing, number of items, and customer membership.

Tips should be more realistic than completely random values and should be related to order value and delivery conditions.

DELIVERIES

Generate delivery records only for delivered orders.

Include:

- delivery_id
- order_id
- driver_id
- delivery_distance_km
- preparation_time_min
- estimated_delivery_time_min
- actual_delivery_time_min

Actual delivery time should depend on:

- Delivery distance
- Preparation time
- Traffic condition
- Weather
- Driver experience

Higher traffic and worse weather should generally increase delivery time.

More experienced drivers should generally have slightly better delivery performance.

REVIEWS

Generate reviews only for delivered orders.

Include:

- review_id
- order_id
- customer_id
- restaurant_id
- review_rating
- review_text
- sentiment

Sentiment should contain:

- Positive
- Neutral
- Negative

Review ratings and sentiment should have a logical relationship.

Reviews should contain realistic short food-delivery comments.

Negative reviews should be more likely when delivery performance is poor.

PAYMENTS

Generate one payment record per order.

Include:

- payment_id
- order_id
- payment_method
- payment_status
- transaction_amount

Payment transaction amount should correspond to the order amount.

Use payment statuses such as:

- Successful
- Failed
- Refunded

DATA RELATIONSHIPS

Ensure that:

- Every order references a valid customer.
- Every order references a valid restaurant.
- Every delivery references a valid order.
- Every delivery references a valid driver.
- Every payment references a valid order.
- Every review references a valid order.
- Every review references the correct customer and restaurant.
- Delivered orders have delivery records.
- Cancelled and failed orders do not have delivery records.
- Reviews only reference delivered orders.

REALISM

Do not generate every field independently using completely random values.

Create logical relationships between variables so the dataset can be used for machine learning.

Examples:

- Premium restaurants should generally have higher prices.
- Higher item counts should generally result in higher order amounts.
- Membership type can influence customer ordering behavior.
- Longer delivery distances should generally increase delivery time.
- Higher traffic should generally increase delivery time.
- Rain and heavy rain should generally increase delivery time.
- Driver experience can slightly affect delivery time.
- Larger orders can have higher tips.
- Delivery delays can negatively affect review ratings.

REPRODUCIBILITY

Use a fixed random seed:

SEED = 42

Also seed Faker.

DATA SIZE

Use approximately:

- 1,500 customers
- 200 restaurants
- 300 drivers
- 10,000 orders
- 7,500 reviews

The number of deliveries should depend on the number of delivered orders.

CODE STRUCTURE

Organize the Python script into clearly commented sections:

1. Imports
2. Configuration
3. Random seed
4. Output directory
5. Reference categories
6. Customer generation
7. Restaurant generation
8. Driver generation
9. Helper functions
10. Order generation
11. Delivery generation
12. Payment generation
13. Review generation
14. Data validation
15. CSV export
16. Main execution

Create separate functions for each dataset.

Create a main() function that executes the entire pipeline.

DATA VALIDATION

Before exporting the datasets, validate:

- Primary key uniqueness
- Missing primary keys
- Foreign key validity
- Valid age ranges
- Valid ratings
- Positive order amounts
- Non-negative tips
- Positive delivery distances
- Positive preparation times
- Positive delivery times
- Valid review ratings
- Customer signup dates before orders
- Delivered orders having deliveries
- Cancelled/failed orders having no deliveries
- Reviews belonging to delivered orders
- Payment transaction amounts matching order amounts

If validation fails, raise an informative error.

CSV EXPORT

Save all generated datasets as CSV files inside:

data/raw/

The script should create the directory if it does not already exist.

The output files should be:

customers.csv
restaurants.csv
orders.csv
deliveries.csv
drivers.csv
reviews.csv
payments.csv

At the end of execution, print a summary showing:

- Dataset name
- Number of rows
- Output directory

OUTPUT REQUIREMENT

Return only the complete Python code for:

src/generate_data.py

The code should be clean, modular, reproducible, commented, and directly executable.
```

---

# 13. Prompt Review

The generated script was treated as a starting point rather than a final production-ready solution.

The output was reviewed against the project requirements and then modified where necessary.

This iterative process demonstrates the use of prompt engineering as part of the development workflow:

```text
Define Requirements
        ↓
Create Structured Prompt
        ↓
Generate Code
        ↓
Review Generated Code
        ↓
Identify Issues
        ↓
Improve Prompt
        ↓
Regenerate / Modify Code
        ↓
Validate Output
        ↓
Use Final Script
```

---

# 14. Key Learning

The main lesson from the prompt-engineering stage is that good synthetic data generation requires more than asking an LLM to "generate fake data."

The prompt must clearly specify:

* The role of the model
* The business context
* The exact task
* The required schema
* Relationships between datasets
* Realism constraints
* Data size
* Validation requirements
* Output format
* Reproducibility requirements

The quality of the generated code depends heavily on the quality and specificity of the instructions provided to the LLM.

```
```
