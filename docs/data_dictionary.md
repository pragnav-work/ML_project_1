# Uber Eats Synthetic Dataset — Data Dictionary

## 1. Customers

| Column | Data Type | Description |
|---|---|---|
| customer_id | string | Unique customer identifier |
| age | integer | Customer age |
| gender | string | Customer gender |
| city | string | Customer city |
| signup_date | date | Date customer registered |
| membership_type | string | Customer membership tier |

## 2. Restaurants

| Column | Data Type | Description |
|---|---|---|
| restaurant_id | string | Unique restaurant identifier |
| restaurant_name | string | Restaurant name |
| city | string | Restaurant city |
| cuisine | string | Primary cuisine type |
| restaurant_category | string | Budget, Mid-range, or Premium |
| restaurant_rating | float | Restaurant rating from 1 to 5 |
| average_price | float | Average order price |

## 3. Orders

| Column | Data Type | Description |
|---|---|---|
| order_id | string | Unique order identifier |
| customer_id | string | Customer placing the order |
| restaurant_id | string | Restaurant receiving the order |
| order_timestamp | datetime | Date and time of order |
| order_status | string | Status of the order |
| order_amount | float | Total order amount before tip |
| tip_amount | float | Customer tip amount |
| items_count | integer | Number of items ordered |
| payment_method | string | Payment method used |
| weather | string | Weather condition during order |
| traffic_condition | string | Traffic condition during order |

## 4. Deliveries

| Column | Data Type | Description |
|---|---|---|
| delivery_id | string | Unique delivery identifier |
| order_id | string | Associated order |
| driver_id | string | Driver assigned to delivery |
| delivery_distance_km | float | Delivery distance in kilometers |
| preparation_time_min | integer | Restaurant preparation time |
| estimated_delivery_time_min | integer | Estimated delivery duration |
| actual_delivery_time_min | integer | Actual delivery duration |

## 5. Drivers

| Column | Data Type | Description |
|---|---|---|
| driver_id | string | Unique driver identifier |
| age | integer | Driver age |
| gender | string | Driver gender |
| vehicle_type | string | Bike, Scooter, or Car |
| experience_years | integer | Years of delivery experience |
| driver_rating | float | Driver rating from 1 to 5 |

## 6. Reviews

| Column | Data Type | Description |
|---|---|---|
| review_id | string | Unique review identifier |
| order_id | string | Associated order |
| customer_id | string | Customer writing review |
| restaurant_id | string | Restaurant being reviewed |
| review_rating | integer | Rating from 1 to 5 |
| review_text | string | Customer review |
| sentiment | string | Positive, Neutral, or Negative |

## 7. Payments

| Column | Data Type | Description |
|---|---|---|
| payment_id | string | Unique payment identifier |
| order_id | string | Associated order |
| payment_method | string | Payment method used |
| payment_status | string | Payment outcome |
| transaction_amount | float | Amount processed |

---

# Dataset Relationships

The datasets are connected using primary and foreign keys.

- `customers.customer_id` → `orders.customer_id`
- `restaurants.restaurant_id` → `orders.restaurant_id`
- `orders.order_id` → `deliveries.order_id`
- `drivers.driver_id` → `deliveries.driver_id`
- `orders.order_id` → `payments.order_id`
- `orders.order_id` → `reviews.order_id`
- `customers.customer_id` → `reviews.customer_id`
- `restaurants.restaurant_id` → `reviews.restaurant_id`

# Planned Dataset Sizes

| Dataset | Target Rows |
|---|---:|
| Customers | 5,000 |
| Restaurants | 500 |
| Drivers | 1,000 |
| Orders | 50,000 |
| Deliveries | 50,000 |
| Payments | 50,000 |
| Reviews | ~35,000–40,000 |

# Synthetic Data Relationships

The generator should create realistic relationships between variables.

### Delivery Time

Delivery time should generally increase with:

- Delivery distance
- Traffic congestion
- Restaurant preparation time
- Poor weather

Driver experience can have a small negative relationship with delivery time.

### Tip Amount

Tip amount should generally increase with:

- Order amount
- Better delivery experience
- Higher customer spending

### Review Sentiment

Review sentiment should generally correlate with:

- Review rating
- Delivery performance
- Restaurant experience

### Order Demand

Order volume should vary based on:

- Hour of day
- Day of week
- Weekends
- Lunch periods
- Dinner periods
- Weather

Orders should span multiple months so that the data can later be used for demand forecasting.

