# Uber Eats Operational & Customer Intelligence System

An end-to-end machine learning project analyzing a food-delivery marketplace — from raw synthetic data to customer segments, sentiment analysis, delivery time predictions, and demand forecasts.

Built as a 7-day self-guided project to practice the full data analyst / ML workflow: understanding a business problem, cleaning data, building models, evaluating them honestly, and translating results into decisions a business could actually act on.

---

## What This Project Does

Uber Eats (simulated, using synthetic data) generates data across customers, restaurants, orders, deliveries, drivers, payments, and reviews. This project uses that data to answer questions like:

- Which customers are most valuable, and which restaurants drive the most revenue?
- What's actually causing negative customer reviews?
- What drives delivery delays, and can delivery time be predicted?
- When does order demand peak, and can it be forecasted?

Each question is answered with an actual model and actual numbers — not assumptions.

---

## Tech Stack

- **Language:** Python
- **Data handling:** Pandas, NumPy
- **Visualization:** Matplotlib
- **Machine learning:** Scikit-learn (K-Means, DBSCAN, Random Forest, Ridge, Lasso, Linear Regression)
- **NLP:** TF-IDF, NLTK, VADER
- **Forecasting:** Statsmodels (ARIMA), Prophet
- **Environment:** Jupyter Notebook
- **Version control:** Git / GitHub

---

## Project Structure

```
.
├── data/
│   ├── raw/                    # Synthetic source data
│   └── processed/              # Cleaned data + model outputs
├── docs/
│   ├── data_dictionary.md      # Column-level definitions for every dataset
│   └── prompt_engineering.md   # How the synthetic data was generated
├── models/
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_segmentation.ipynb
│   ├── 03_nlp_sentiment_analysis.ipynb
│   ├── 04_delivery_prediction.ipynb
│   ├── 05_hourly_demand_forecasting.ipynb
│   └── 06_pipeline_and_business_insights.ipynb
├── outputs/
├── src/
│   └── generate_data.py        # Synthetic data generator
├── requirements.txt
└── README.md
```

---

## The Data

All data is **synthetic** — generated with Python and Faker, not real user data. This was a deliberate choice: it removes privacy concerns entirely and makes the dataset reproducible (fixed random seed) while still behaving like a realistic marketplace.

| Dataset | Rows | What it holds |
|---|---:|---|
| Customers | 1,500 | Demographics, signup date, membership tier |
| Restaurants | 200 | Cuisine, category, rating, pricing |
| Drivers | 300 | Vehicle type, experience, rating |
| Orders | 10,000 | Order amount, tip, timestamp, weather, traffic |
| Deliveries | ~9,200 | Distance, prep time, estimated vs actual delivery time |
| Reviews | 7,500 | Review text, rating, sentiment label |
| Payments | 10,000 | Payment method, status, amount |

Full column-level definitions are in [`docs/data_dictionary.md`](docs/data_dictionary.md).

Tables connect through standard foreign keys — every order links to a customer and restaurant, every delivery links to an order and driver, and so on. Before anything else, the cleaning notebook validates that these relationships actually hold (no orphaned foreign keys, no impossible values like negative delivery times).

---

## How the Project Is Organized (Notebook by Notebook)

### 1. Data Cleaning
Loads all seven raw datasets, checks for missing values, duplicates, invalid foreign keys, and out-of-range values (e.g. ratings outside 1–5), and exports cleaned versions to `data/processed/`.

### 2. Customer & Restaurant Segmentation
Groups customers and restaurants into behavioral segments using K-Means (with DBSCAN tested as a comparison).

- **Customers** split into two segments: *Frequent High-Value Customers* (41% of the base, ~2x the order frequency and total spend of the other group) and *Occasional Moderate-Value Customers*.
- **Restaurants** also split into two segments, but not by order volume or delivery performance — by transaction value. *High-Value Restaurants* (15% of restaurants) generate 40% of total revenue despite being a small minority.
- DBSCAN was tested on both but didn't reveal additional structure beyond what K-Means found — the data doesn't have strong natural density clusters.

### 3. Sentiment Analysis
Classifies review text as Positive, Neutral, or Negative using TF-IDF features and a Naive Bayes classifier, benchmarked against VADER (a rule-based sentiment tool) and SVM.

- Naive Bayes performed best (F1 ≈ 99.9%), well ahead of VADER (F1 ≈ 83.6%).
- Reviews are heavily imbalanced (80% positive, only 1.1% negative), which is disclosed as a limitation rather than papered over.
- Negative reviews cluster around two themes: **delivery delays** and **food arriving cold / not fresh** — both traceable back to delivery time.

### 4. Delivery Time Prediction
Predicts `actual_delivery_time_min` using Linear Regression, Random Forest, Ridge, and Lasso.

- **Random Forest performed best**: MAE 5.07 min, RMSE 6.87 min, R² 0.884 — confirmed with 5-fold cross-validation.
- **Delivery distance (78%) and prep time (13%)** account for over 90% of what drives delivery time. Traffic adds a small effect; everything else (order amount, restaurant rating, day of week) barely matters.

### 5. Hourly Demand Forecasting
Aggregates orders into an hourly time series, decomposes it into trend/seasonality/noise, confirms stationarity (ADF test), then forecasts using ARIMA and Prophet.

- **Prophet outperformed ARIMA** (MAE 1.04 vs 2.02) — it captured the daily double-peak pattern (midday + evening), while ARIMA flattened to a constant average.
- Demand shows almost no day-of-week variation — the pattern is driven by time of day, not day of week.

### 6. Pipeline & Business Insights
Brings everything above together into one place — no retraining, just integration — to answer business questions directly (most valuable segments, root causes of bad reviews, when to deploy delivery capacity) with recommendations backed by the actual numbers from notebooks 2–5.

---

## Key Findings, In Short

- A minority of customers and restaurants drive a disproportionate share of value — worth prioritizing for retention.
- Restaurant "value tier" has nothing to do with service quality (rating and sentiment are nearly identical across segments) — problems should be tackled restaurant-by-restaurant, not by segment.
- Delivery delays are structurally explained by distance and prep time, not randomness — and they're the leading cause of negative reviews.
- Demand is highly predictable by hour, with two daily peaks — capacity planning should follow time-of-day, not day-of-week.

---

## Limitations

- Cluster separation is moderate, not sharp (silhouette scores 0.25–0.42) — segments are useful directionally, not hard boundaries.
- Negative-review sentiment is based on very few examples (86 reviews) — treat with caution.
- No location/zone data exists, so demand spikes could only be analyzed by time, not by geography.
- Tip amount prediction and a couple of related questions were scoped out — noted rather than skipped silently.

---

## Running This Project

```bash
# install dependencies
pip install -r requirements.txt

# (optional) regenerate synthetic data
python src/generate_data.py

# then run the notebooks in order, 01 through 06
```

---

## Why Synthetic Data + Prompt Engineering

The data generator (`src/generate_data.py`) and its underlying prompts are documented in [`docs/prompt_engineering.md`](docs/prompt_engineering.md), including the structured prompting approach used to design a schema realistic enough to support meaningful analysis.
