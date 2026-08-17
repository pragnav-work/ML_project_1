# ============================================================
# Uber Eats Operational & Customer Intelligence System
# Synthetic Data Generation Script
# ============================================================
#
# Purpose:
# Generate realistic synthetic datasets for a food-delivery
# marketplace analytics project.
#
# Datasets generated:
# 1. Customers
# 2. Restaurants
# 3. Drivers
# 4. Orders
# 5. Deliveries
# 6. Payments
# 7. Reviews
#
# The generated data will later be used for:
# - EDA
# - ETL
# - Customer segmentation
# - Restaurant segmentation
# - Sentiment analysis
# - Delivery-time prediction
# - Tip prediction
# - Demand forecasting
# - Business recommendations
# ============================================================


# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

# Path is used to create and manage file-system paths.
from pathlib import Path

# NumPy is used for random number generation and numerical
# calculations.
import numpy as np

# Pandas is used to create and manipulate DataFrames.
import pandas as pd

# Faker is used to generate realistic-looking names.
from faker import Faker


# ============================================================
# 2. Configuration
# ============================================================

# Random seed ensures that the same synthetic dataset
# can be reproduced every time the script is executed.
SEED = 42


# ------------------------------------------------------------
# Dataset sizes
# ------------------------------------------------------------

# Number of unique customers.
N_CUSTOMERS = 1_500

# Number of unique restaurants.
N_RESTAURANTS = 200

# Number of unique delivery drivers.
N_DRIVERS = 300

# Total number of orders generated.
N_ORDERS = 10_000

# Number of customer reviews.
# We keep this below the number of delivered orders.
N_REVIEWS = 7_500


# ------------------------------------------------------------
# Order date range
# ------------------------------------------------------------

# Start date for the synthetic order history.
START_DATE = pd.Timestamp('2025-01-01')

# End date for the synthetic order history.
END_DATE = pd.Timestamp('2025-06-30')


# ------------------------------------------------------------
# Output location
# ------------------------------------------------------------

# All generated CSV files will be saved inside data/raw/.
OUTPUT_DIR = Path('data/raw')

# ============================================================
# 3. RANDOM SEED AND FAKER CONFIGURATION
# ============================================================

# Set NumPy random seed so random values are reproducible.
np.random.seed(SEED)

# Create a Faker object using Indian-style data generation.
fake = Faker('en_IN')

# Set Faker seed so generated names are also reproducible.
fake.seed_instance(SEED)


# ============================================================
# 4. REFERENCE DATA
# ============================================================

# ------------------------------------------------------------
# Cities
# ------------------------------------------------------------

# Cities available in the synthetic marketplace.
CITIES = [
    'Bengaluru',
    'Chennai',
    'Hyderabad',
    'Mumbai',
    'Delhi',
    'Pune',
    'Kolkata',
    'Ahmedabad',
    'Jaipur',
    'Kochi',
]


# Probability of an entity belonging to each city.
# This creates an uneven but realistic city distribution.
CITY_WEIGHTS = np.array([
    0.17,
    0.14,
    0.13,
    0.13,
    0.12,
    0.10,
    0.07,
    0.05,
    0.05,
    0.04,
])


# Normalize weights so they sum exactly to 1.
CITY_WEIGHTS = CITY_WEIGHTS / CITY_WEIGHTS.sum()


# ------------------------------------------------------------
# Cuisine types
# ------------------------------------------------------------

CUISINES = [
    'North Indian',
    'South Indian',
    'Chinese',
    'Italian',
    'Mexican',
    'Fast Food',
    'Biryani',
    'Desserts',
    'Cafe',
    'Bakery',
]


# Probability distribution for restaurant cuisines.
CUISINE_WEIGHTS = np.array([
    0.17,
    0.15,
    0.13,
    0.08,
    0.05,
    0.14,
    0.10,
    0.06,
    0.07,
    0.05,
])


# Normalize cuisine probabilities.
CUISINE_WEIGHTS = (
    CUISINE_WEIGHTS / CUISINE_WEIGHTS.sum()
)


# ------------------------------------------------------------
# Restaurant categories
# ------------------------------------------------------------

RESTAURANT_CATEGORIES = [
    'Budget',
    'Mid-range',
    'Premium',
]


RESTAURANT_CATEGORY_WEIGHTS = [
    0.40,
    0.45,
    0.15,
]


# ------------------------------------------------------------
# Customer membership types
# ------------------------------------------------------------

MEMBERSHIP_TYPES = [
    'Basic',
    'Plus',
    'Premium',
]


MEMBERSHIP_WEIGHTS = [
    0.55,
    0.30,
    0.15,
]


# ------------------------------------------------------------
# Gender distribution
# ------------------------------------------------------------

GENDERS = [
    'Male',
    'Female',
    'Other',
]


GENDER_WEIGHTS = [
    0.49,
    0.49,
    0.02,
]


# ------------------------------------------------------------
# Driver vehicle types
# ------------------------------------------------------------

VEHICLE_TYPES = [
    'Bike',
    'Scooter',
    'Car',
]


VEHICLE_WEIGHTS = [
    0.48,
    0.42,
    0.10,
]


# ------------------------------------------------------------
# Order statuses
# ------------------------------------------------------------

ORDER_STATUSES = [
    'Delivered',
    'Cancelled',
    'Failed',
]


ORDER_STATUS_WEIGHTS = [
    0.92,
    0.06,
    0.02,
]


# ------------------------------------------------------------
# Payment methods
# ------------------------------------------------------------

PAYMENT_METHODS = [
    'UPI',
    'Credit Card',
    'Debit Card',
    'Wallet',
    'Cash',
]


PAYMENT_METHOD_WEIGHTS = [
    0.55,
    0.16,
    0.14,
    0.10,
    0.05,
]


# ------------------------------------------------------------
# Weather conditions
# ------------------------------------------------------------

WEATHER_TYPES = [
    'Clear',
    'Cloudy',
    'Rain',
    'Heavy Rain',
]


WEATHER_WEIGHTS = [
    0.55,
    0.25,
    0.16,
    0.04,
]


# ------------------------------------------------------------
# Traffic conditions
# ------------------------------------------------------------

# Traffic is generated separately because traffic probability
# will depend partly on weather.
TRAFFIC_TYPES = [
    'Low',
    'Medium',
    'High',
    'Severe',
]


# ------------------------------------------------------------
# Payment statuses
# ------------------------------------------------------------

PAYMENT_STATUSES = [
    'Successful',
    'Failed',
    'Refunded',
]


PAYMENT_STATUS_WEIGHTS = [
    0.94,
    0.04,
    0.02,
]


# ============================================================
# 5. REVIEW TEXT COMPONENTS
# ============================================================
#
# Instead of having only a few fixed review sentences, we create
# multiple sentence components and randomly combine them.
#
# This gives us more variety in the synthetic text dataset and
# makes it more suitable for future NLP/sentiment analysis.
# ============================================================


# ------------------------------------------------------------
# Positive review components
# ------------------------------------------------------------

POSITIVE_OPENINGS = [
    'Really enjoyed the meal.',
    'The food was delicious.',
    'Great food and service.',
    'Very happy with the order.',
    'The meal was excellent.',
    'Loved the overall experience.',
    'Really good experience.',
    'Very satisfied with the order.',
]


POSITIVE_FOOD = [
    'The food was fresh and tasty.',
    'Everything tasted great.',
    'The food arrived hot and fresh.',
    'The portion size was good.',
    'The meal was flavorful and satisfying.',
    'The food quality was excellent.',
    'Everything tasted fresh.',
    'The food was prepared really well.',
]


POSITIVE_DELIVERY = [
    'Delivery was quick.',
    'The order arrived on time.',
    'The delivery was smooth.',
    'The driver delivered the order quickly.',
    'Everything arrived in good condition.',
    'The delivery was faster than expected.',
    'The order arrived without any issues.',
]


POSITIVE_PACKAGING = [
    'The packaging was neat.',
    'The packaging was good.',
    'Everything was packed properly.',
    'The packaging kept the food fresh.',
]


# ------------------------------------------------------------
# Neutral review components
# ------------------------------------------------------------

NEUTRAL_OPENINGS = [
    'The experience was average.',
    'The food was okay overall.',
    'It was a decent experience.',
    'Nothing particularly stood out.',
    'The order was satisfactory.',
    'The experience was acceptable.',
    'It was an average order.',
]


NEUTRAL_FOOD = [
    'The food was acceptable.',
    'The taste was decent.',
    'The portion size was reasonable.',
    'The food quality was average.',
    'The meal was fine.',
    'The food was neither great nor bad.',
]


NEUTRAL_DELIVERY = [
    'Delivery was neither fast nor slow.',
    'The order arrived around the expected time.',
    'Delivery was acceptable.',
    'The delivery experience was average.',
    'The delivery was okay.',
]


NEUTRAL_PACKAGING = [
    'The packaging was fine.',
    'Packaging was acceptable.',
    'The order was packed reasonably well.',
    'The packaging was average.',
]


# ------------------------------------------------------------
# Negative review components
# ------------------------------------------------------------

NEGATIVE_OPENINGS = [
    'I was disappointed with the order.',
    'Not happy with the experience.',
    'The order could have been much better.',
    'Unfortunately, the experience was poor.',
    'I was not satisfied with the order.',
    'The overall experience was disappointing.',
]


NEGATIVE_FOOD = [
    'The food arrived cold.',
    'The food was not fresh.',
    'The taste was disappointing.',
    'The food quality needs improvement.',
    'The portion size was disappointing.',
    'The meal did not taste fresh.',
    'The food was below expectations.',
]


NEGATIVE_DELIVERY = [
    'The delivery was very late.',
    'The order took much longer than expected.',
    'The delivery experience was poor.',
    'The order arrived much later than expected.',
    'Delivery was extremely slow.',
    'The delivery was delayed significantly.',
]


NEGATIVE_PACKAGING = [
    'The packaging was poor.',
    'The packaging was damaged.',
    'The order was not packed properly.',
    'The packaging could be improved.',
]


# ============================================================
# 6. CUSTOMER GENERATION
# ============================================================

def generate_customers():
    """
    Generate the customer master dataset.

    Each customer receives:
    - Unique customer ID
    - Age
    - Gender
    - City
    - Signup date
    - Membership type
    """

    # Randomly assign membership types according to the
    # predefined probabilities.
    membership = np.random.choice(
        MEMBERSHIP_TYPES,
        size=N_CUSTOMERS,
        p=MEMBERSHIP_WEIGHTS
    )

    # Define possible signup date range.
    signup_start = pd.Timestamp('2024-07-01')

    signup_end = pd.Timestamp('2025-03-31')

    # Generate random number of days from signup_start.
    signup_days = np.random.randint(
        0,
        (signup_end - signup_start).days + 1,
        size=N_CUSTOMERS
    )

    # Create the customer DataFrame.
    customers = pd.DataFrame({

        # Generate IDs such as CUST_00001.
        'customer_id': [
            f'CUST_{i:05d}'
            for i in range(1, N_CUSTOMERS + 1)
        ],

        # Generate realistic ages between 18 and 65.
        'age': np.clip(
            np.round(
                np.random.normal(
                    31,
                    8,
                    N_CUSTOMERS
                )
            ),
            18,
            65
        ).astype(int),

        # Generate gender according to predefined probabilities.
        'gender': np.random.choice(
            GENDERS,
            size=N_CUSTOMERS,
            p=GENDER_WEIGHTS
        ),

        # Assign customers to cities.
        'city': np.random.choice(
            CITIES,
            size=N_CUSTOMERS,
            p=CITY_WEIGHTS
        ),

        # Generate signup dates.
        'signup_date': (
            signup_start
            + pd.to_timedelta(
                signup_days,
                unit='D'
            )
        ),

        # Assign membership type.
        'membership_type': membership,
    })

    return customers


# ============================================================
# 7. RESTAURANT GENERATION
# ============================================================

def generate_restaurants():
    """
    Generate the restaurant master dataset.

    Each restaurant receives:
    - Unique restaurant ID
    - Restaurant name
    - City
    - Cuisine
    - Restaurant category
    - Rating
    - Average price
    """

    # Assign restaurant category.
    restaurant_category = np.random.choice(
        RESTAURANT_CATEGORIES,
        size=N_RESTAURANTS,
        p=RESTAURANT_CATEGORY_WEIGHTS
    )

    # Define realistic average price ranges by restaurant category.
    price_ranges = {
        'Budget': (120, 300),
        'Mid-range': (280, 650),
        'Premium': (600, 1600),
    }

    # Store generated average prices.
    average_prices = []

    # Generate price based on restaurant category.
    for category in restaurant_category:

        low, high = price_ranges[category]

        average_prices.append(
            np.random.uniform(
                low,
                high
            )
        )

    # Generate restaurant ratings between 1 and 5.
    ratings = np.clip(
        np.random.normal(
            4.1,
            0.45,
            N_RESTAURANTS
        ),
        1.0,
        5.0
    ).round(1)

    # Create restaurant DataFrame.
    restaurants = pd.DataFrame({

        # Generate restaurant IDs.
        'restaurant_id': [
            f'REST_{i:04d}'
            for i in range(1, N_RESTAURANTS + 1)
        ],

        # Generate synthetic restaurant names.
        'restaurant_name': [
            f'{fake.company()} Kitchen'
            for _ in range(N_RESTAURANTS)
        ],

        # Assign restaurant city.
        'city': np.random.choice(
            CITIES,
            size=N_RESTAURANTS,
            p=CITY_WEIGHTS
        ),

        # Assign cuisine.
        'cuisine': np.random.choice(
            CUISINES,
            size=N_RESTAURANTS,
            p=CUISINE_WEIGHTS
        ),

        # Assign restaurant category.
        'restaurant_category': restaurant_category,

        # Assign restaurant rating.
        'restaurant_rating': ratings,

        # Assign average price.
        'average_price': np.round(
            average_prices,
            2
        ),
    })

    return restaurants


# ============================================================
# 8. DRIVER GENERATION
# ============================================================

def generate_drivers():
    """
    Generate the driver master dataset.

    Each driver receives:
    - Driver ID
    - Age
    - Gender
    - Vehicle type
    - Experience
    - Driver rating
    """

    # Generate driver ages between 21 and 60.
    ages = np.clip(
        np.round(
            np.random.normal(
                33,
                7,
                N_DRIVERS
            )
        ),
        21,
        60
    ).astype(int)

    # Maximum possible experience is based on age.
    max_experience = np.maximum(
        0,
        ages - 18
    )

    # Generate experience years.
    experience = np.array([

        np.random.uniform(
            0,
            max_exp
        )

        if max_exp > 0

        else 0

        for max_exp in max_experience
    ])

    # Create driver DataFrame.
    drivers = pd.DataFrame({

        # Generate driver IDs.
        'driver_id': [
            f'DRV_{i:04d}'
            for i in range(1, N_DRIVERS + 1)
        ],

        # Driver age.
        'age': ages,

        # Driver gender.
        'gender': np.random.choice(
            GENDERS,
            size=N_DRIVERS,
            p=GENDER_WEIGHTS
        ),

        # Driver vehicle.
        'vehicle_type': np.random.choice(
            VEHICLE_TYPES,
            size=N_DRIVERS,
            p=VEHICLE_WEIGHTS
        ),

        # Driver experience.
        'experience_years': np.round(
            experience,
            1
        ),

        # Driver rating.
        'driver_rating': np.clip(
            np.random.normal(
                4.2,
                0.4,
                N_DRIVERS
            ),
            1.0,
            5.0
        ).round(1),
    })

    return drivers


# ============================================================
# 9. TIME GENERATION HELPERS
# ============================================================

def weighted_hour():
    """
    Generate an order hour using realistic food-delivery
    demand patterns.

    Lunch and dinner receive higher probabilities.
    """

    # Represent the 24 hours of a day.
    hours = np.arange(24)

    # Start with a low baseline probability.
    weights = np.ones(24) * 0.35

    # Morning demand.
    weights[7:11] = 0.65

    # Lunch peak.
    weights[11:15] = 2.2

    # Afternoon low-demand period.
    weights[15:18] = 0.65

    # Dinner peak.
    weights[18:23] = 2.7

    # Late-night demand.
    weights[23] = 0.25

    # Very low overnight demand.
    weights[0:7] = 0.12

    # Convert weights into probabilities.
    probabilities = (
        weights
        / weights.sum()
    )

    # Select an hour according to those probabilities.
    return np.random.choice(
        hours,
        p=probabilities
    )


def generate_order_timestamps(n):
    """
    Generate realistic order timestamps between START_DATE
    and END_DATE.
    """

    # Calculate number of days in the period.
    total_days = (
        END_DATE - START_DATE
    ).days

    # Store timestamps.
    timestamps = []

    # Generate one timestamp for every order.
    for _ in range(n):

        # Select a random date.
        day_offset = np.random.randint(
            0,
            total_days + 1
        )

        date = (
            START_DATE
            + pd.Timedelta(
                days=int(day_offset)
            )
        )

        # Select an hour based on food-delivery demand.
        hour = weighted_hour()

        # Random minute.
        minute = np.random.randint(
            0,
            60
        )

        # Random second.
        second = np.random.randint(
            0,
            60
        )

        # Combine date and time.
        timestamps.append(
            date
            + pd.Timedelta(
                hours=int(hour)
            )
            + pd.Timedelta(
                minutes=int(minute)
            )
            + pd.Timedelta(
                seconds=int(second)
            )
        )

    return pd.Series(timestamps)


# ============================================================
# 10. CUSTOMER SELECTION HELPER
# ============================================================

def choose_customer(customers):
    """
    Select a customer for an order.

    Premium customers receive a slightly higher probability
    of placing orders than Basic customers.
    """

    # Assign order-frequency multipliers by membership.
    membership_factor = {
        'Basic': 1.0,
        'Plus': 1.25,
        'Premium': 1.60,
    }

    # Convert membership type into numerical weights.
    weights = (
        customers['membership_type']
        .map(membership_factor)
        .astype(float)
        .values
    )

    # Normalize weights to probabilities.
    weights = (
        weights
        / weights.sum()
    )

    # Select one customer.
    return np.random.choice(
        customers['customer_id'].values,
        p=weights
    )


# ============================================================
# 11. ORDER GENERATION
# ============================================================

def generate_orders(
    customers,
    restaurants
):
    """
    Generate the main order transaction dataset.

    Important relationships:
    - Customer city influences restaurant city.
    - Restaurant category influences order value.
    - Membership influences order value.
    - Weather influences traffic.
    - Weather and traffic influence tips.
    """

    # --------------------------------------------------------
    # Select customers for every order.
    # --------------------------------------------------------

    customer_ids = [

        choose_customer(
            customers
        )

        for _ in range(
            N_ORDERS
        )
    ]

    # Create a customer lookup table for efficient mapping.
    customer_lookup = customers.set_index(
        'customer_id'
    )

    # Get the city of each selected customer.
    customer_cities = customer_lookup.loc[
        customer_ids,
        'city'
    ].values

    # Get the membership of each selected customer.
    memberships = customer_lookup.loc[
        customer_ids,
        'membership_type'
    ].values

    # --------------------------------------------------------
    # Generate order timestamps.
    # --------------------------------------------------------

    timestamps = generate_order_timestamps(
        N_ORDERS
    )

    # --------------------------------------------------------
    # Select restaurants from the customer's city.
    #
    # This prevents unrealistic situations where a customer
    # from Chennai constantly orders from a restaurant in Delhi.
    # --------------------------------------------------------

    restaurant_city_map = (
        restaurants
        .groupby(
            'city'
        )[
            'restaurant_id'
        ]
        .apply(list)
        .to_dict()
    )

    # Store restaurant IDs for every order.
    restaurant_ids = []

    # Select a restaurant from the customer's city.
    for customer_city in customer_cities:

        city_restaurants = (
            restaurant_city_map[
                customer_city
            ]
        )

        restaurant_ids.append(
            np.random.choice(
                city_restaurants
            )
        )

    # Convert list to NumPy array.
    restaurant_ids = np.array(
        restaurant_ids
    )

    # Create restaurant lookup table.
    restaurant_lookup = restaurants.set_index(
        'restaurant_id'
    )

    # Get restaurant category for each order.
    categories = restaurant_lookup.loc[
        restaurant_ids,
        'restaurant_category'
    ].values

    # Get restaurant average price for each order.
    avg_prices = restaurant_lookup.loc[
        restaurant_ids,
        'average_price'
    ].values

    # --------------------------------------------------------
    # Generate number of items per order.
    # --------------------------------------------------------

    items_count = np.clip(
        np.random.poisson(
            2.2,
            N_ORDERS
        ) + 1,
        1,
        8
    )

    # --------------------------------------------------------
    # Restaurant category impact on order value.
    # --------------------------------------------------------

    category_factor = pd.Series(
        categories
    ).map({

        'Budget': 0.85,

        'Mid-range': 1.00,

        'Premium': 1.25,

    }).values

    # --------------------------------------------------------
    # Customer membership impact on order value.
    # --------------------------------------------------------

    membership_factor = pd.Series(
        memberships
    ).map({

        'Basic': 0.95,

        'Plus': 1.08,

        'Premium': 1.20,

    }).values

    # --------------------------------------------------------
    # Calculate order amount.
    # --------------------------------------------------------

    order_amount = (

        avg_prices

        * (
            items_count
            / 2.2
        )

        * category_factor

        * membership_factor

        * np.random.normal(
            1.0,
            0.18,
            N_ORDERS
        )
    )

    # Prevent unrealistic values.
    order_amount = np.clip(
        order_amount,
        80,
        5000
    )

    # --------------------------------------------------------
    # Generate order status.
    # --------------------------------------------------------

    order_status = np.random.choice(
        ORDER_STATUSES,
        size=N_ORDERS,
        p=ORDER_STATUS_WEIGHTS
    )

    # --------------------------------------------------------
    # Generate weather.
    # --------------------------------------------------------

    weather = np.random.choice(
        WEATHER_TYPES,
        size=N_ORDERS,
        p=WEATHER_WEIGHTS
    )

    # --------------------------------------------------------
    # Generate traffic based partly on weather.
    #
    # Example:
    # Heavy Rain has a higher probability of High/Severe traffic.
    # Clear weather has a higher probability of Low/Medium traffic.
    # --------------------------------------------------------

    traffic_probabilities = {

        'Clear': [
            0.35,
            0.45,
            0.17,
            0.03,
        ],

        'Cloudy': [
            0.25,
            0.45,
            0.25,
            0.05,
        ],

        'Rain': [
            0.12,
            0.38,
            0.38,
            0.12,
        ],

        'Heavy Rain': [
            0.05,
            0.20,
            0.45,
            0.30,
        ],
    }

    # Store generated traffic conditions.
    traffic = []

    # Generate traffic for each order.
    for weather_condition in weather:

        traffic.append(
            np.random.choice(

                TRAFFIC_TYPES,

                p=traffic_probabilities[
                    weather_condition
                ]
            )
        )

    # Convert to NumPy array.
    traffic = np.array(
        traffic
    )

    # --------------------------------------------------------
    # Generate payment method.
    # --------------------------------------------------------

    payment_method = np.random.choice(
        PAYMENT_METHODS,
        size=N_ORDERS,
        p=PAYMENT_METHOD_WEIGHTS
    )

    # --------------------------------------------------------
    # Generate tip amount.
    # --------------------------------------------------------

    # Beta distribution produces mostly small tips with
    # occasional larger tips.
    base_tip_rate = np.random.beta(
        2.0,
        15.0,
        N_ORDERS
    )

    # Identify orders with relatively good conditions.
    good_conditions = (

        np.isin(
            traffic,
            ['Low', 'Medium']
        )

        & np.isin(
            weather,
            ['Clear', 'Cloudy']
        )
    )

    # Increase tips slightly under good conditions and decrease
    # them under poor conditions.
    tip_rate = np.where(

        good_conditions,

        base_tip_rate * 1.25,

        base_tip_rate * 0.75
    )

    # Calculate tip amount.
    tip_amount = (
        order_amount
        * tip_rate
    )

    # Cancelled/failed orders do not receive tips.
    tip_amount = np.where(

        order_status == 'Delivered',

        tip_amount,

        0
    )

    # Limit extremely large synthetic tips.
    tip_amount = np.clip(
        tip_amount,
        0,
        1000
    )

    # --------------------------------------------------------
    # Create order DataFrame.
    # --------------------------------------------------------

    orders = pd.DataFrame({

        # Unique order ID.
        'order_id': [
            f'ORD_{i:06d}'
            for i in range(
                1,
                N_ORDERS + 1
            )
        ],

        # Customer who placed the order.
        'customer_id': customer_ids,

        # Restaurant receiving the order.
        'restaurant_id': restaurant_ids,

        # Timestamp of the order.
        'order_timestamp': timestamps,

        # Order status.
        'order_status': order_status,

        # Total order value.
        'order_amount': np.round(
            order_amount,
            2
        ),

        # Tip value.
        'tip_amount': np.round(
            tip_amount,
            2
        ),

        # Number of items.
        'items_count': items_count,

        # Payment method.
        'payment_method': payment_method,

        # Weather at order time.
        'weather': weather,

        # Traffic condition at order time.
        'traffic_condition': traffic,
    })

    # --------------------------------------------------------
    # Ensure customer signed up before placing the order.
    # --------------------------------------------------------

    signup_lookup = customers.set_index(
        'customer_id'
    )['signup_date']

    # Find orders where signup date is not before order date.
    invalid = (

        orders[
            'order_timestamp'
        ].dt.normalize()

        <= orders[
            'customer_id'
        ].map(
            signup_lookup
        )
    )

    # Count invalid records.
    invalid_count = int(
        invalid.sum()
    )

    # Correct invalid timestamps if necessary.
    if invalid_count > 0:

        # Get the signup date for invalid orders.
        valid_signup_dates = orders.loc[
            invalid,
            'customer_id'
        ].map(
            signup_lookup
        )

        # Add at least one day after signup.
        offsets = np.random.randint(
            1,
            30,
            invalid_count
        )

        # Generate corrected timestamps.
        new_timestamps = (

            valid_signup_dates.reset_index(
                drop=True
            )

            + pd.to_timedelta(
                offsets,
                unit='D'
            )

            + pd.to_timedelta(
                np.random.randint(
                    8 * 60,
                    23 * 60,
                    invalid_count
                ),
                unit='m'
            )
        )

        # Replace invalid timestamps.
        orders.loc[
            invalid,
            'order_timestamp'
        ] = new_timestamps.values

    return orders


# ============================================================
# 12. DELIVERY GENERATION
# ============================================================

def generate_deliveries(
    orders,
    drivers
):
    """
    Generate delivery records only for successfully delivered
    orders.
    """

    # Keep only delivered orders.
    delivered_orders = orders[
        orders[
            'order_status'
        ] == 'Delivered'
    ].copy()

    # Number of delivery records required.
    n = len(
        delivered_orders
    )

    # Assign drivers randomly.
    driver_ids = np.random.choice(
        drivers[
            'driver_id'
        ].values,
        size=n
    )

    # --------------------------------------------------------
    # Delivery distance.
    # --------------------------------------------------------

    # Gamma distribution creates many short trips and fewer
    # long trips.
    distance = np.clip(

        np.random.gamma(
            shape=2.4,
            scale=2.5,
            size=n
        ),

        0.5,

        20
    )

    # --------------------------------------------------------
    # Restaurant preparation time.
    # --------------------------------------------------------

    preparation_time = np.clip(

        np.random.normal(
            22,
            7,
            n
        ),

        5,

        45
    )

    # --------------------------------------------------------
    # Traffic impact.
    # --------------------------------------------------------

    traffic_factor = (

        delivered_orders[
            'traffic_condition'
        ]

        .map({

            'Low': 1.00,

            'Medium': 1.15,

            'High': 1.35,

            'Severe': 1.65,

        })

        .values
    )

    # --------------------------------------------------------
    # Weather impact.
    # --------------------------------------------------------

    weather_factor = (

        delivered_orders[
            'weather'
        ]

        .map({

            'Clear': 1.00,

            'Cloudy': 1.03,

            'Rain': 1.18,

            'Heavy Rain': 1.40,

        })

        .values
    )

    # Create driver lookup.
    driver_lookup = drivers.set_index(
        'driver_id'
    )

    # Get driver experience.
    experience = driver_lookup.loc[
        driver_ids,
        'experience_years'
    ].values

    # Experienced drivers are slightly more efficient.
    driver_factor = np.clip(

        1.0
        - (
            (experience - 2)
            * 0.015
        ),

        0.88,

        1.08
    )

    # --------------------------------------------------------
    # Calculate travel time.
    # --------------------------------------------------------

    travel_time = (

        distance

        * np.random.normal(
            4.0,
            0.45,
            n
        )

        * traffic_factor

        * weather_factor

        * driver_factor
    )

    # --------------------------------------------------------
    # Calculate actual delivery time.
    # --------------------------------------------------------

    actual_time = (

        preparation_time

        + travel_time

        + np.random.normal(
            0,
            4,
            n
        )
    )

    # Keep delivery time within realistic limits.
    actual_time = np.clip(
        actual_time,
        8,
        150
    )

    # --------------------------------------------------------
    # Calculate estimated delivery time.
    # --------------------------------------------------------

    estimated_time = (

        actual_time

        * np.random.normal(
            0.98,
            0.10,
            n
        )
    )

    # Prevent unrealistic estimates.
    estimated_time = np.clip(
        estimated_time,
        8,
        160
    )

    # --------------------------------------------------------
    # Create delivery DataFrame.
    # --------------------------------------------------------

    deliveries = pd.DataFrame({

        # Delivery ID.
        'delivery_id': [
            f'DEL_{i:06d}'
            for i in range(
                1,
                n + 1
            )
        ],

        # Related order ID.
        'order_id': delivered_orders[
            'order_id'
        ].values,

        # Assigned driver.
        'driver_id': driver_ids,

        # Delivery distance.
        'delivery_distance_km': np.round(
            distance,
            2
        ),

        # Restaurant preparation time.
        'preparation_time_min': np.round(
            preparation_time,
            1
        ),

        # Estimated delivery time.
        'estimated_delivery_time_min': np.round(
            estimated_time,
            1
        ),

        # Actual delivery time.
        'actual_delivery_time_min': np.round(
            actual_time,
            1
        ),
    })

    return deliveries


# ============================================================
# 13. PAYMENT GENERATION
# ============================================================

def generate_payments(orders):
    """
    Generate one payment transaction record per order.

    Payment status depends partly on order status.
    """

    # Number of payments equals number of orders.
    n = len(
        orders
    )

    # Store generated payment statuses.
    payment_status = []

    # Generate payment status for every order.
    for order_status in orders[
        'order_status'
    ]:

        # Delivered orders are usually successful.
        if order_status == 'Delivered':

            status = np.random.choice(

                PAYMENT_STATUSES,

                p=[
                    0.96,
                    0.025,
                    0.015,
                ]
            )

        # Cancelled orders have a higher chance of being refunded.
        elif order_status == 'Cancelled':

            status = np.random.choice(

                PAYMENT_STATUSES,

                p=[
                    0.60,
                    0.05,
                    0.35,
                ]
            )

        # Failed orders have a higher chance of payment failure.
        else:

            status = np.random.choice(

                PAYMENT_STATUSES,

                p=[
                    0.15,
                    0.80,
                    0.05,
                ]
            )

        payment_status.append(
            status
        )

    # --------------------------------------------------------
    # Create payment DataFrame.
    # --------------------------------------------------------

    payments = pd.DataFrame({

        # Payment ID.
        'payment_id': [
            f'PAY_{i:06d}'
            for i in range(
                1,
                n + 1
            )
        ],

        # Related order.
        'order_id': orders[
            'order_id'
        ].values,

        # Payment method used for the order.
        'payment_method': orders[
            'payment_method'
        ].values,

        # Payment status.
        'payment_status': payment_status,

        # Transaction amount.
        'transaction_amount': np.round(
            orders[
                'order_amount'
            ].values,
            2
        ),
    })

    return payments


# ============================================================
# 14. REVIEW GENERATION
# ============================================================

def generate_reviews(
    orders,
    deliveries
):
    """
    Generate customer reviews for delivered orders.

    Review rating depends partly on delivery performance.
    Review text is generated from multiple combinations.
    """

    # Only delivered orders can receive reviews.
    delivered_orders = orders[
        orders[
            'order_status'
        ] == 'Delivered'
    ].copy()

    # Create delivery lookup table.
    delivery_lookup = deliveries.set_index(
        'order_id'
    )

    # Do not generate more reviews than delivered orders.
    eligible_count = min(
        N_REVIEWS,
        len(
            delivered_orders
        )
    )

    # Randomly select orders that will receive reviews.
    selected = delivered_orders.sample(
        n=eligible_count,
        random_state=SEED
    ).copy()

    # Get actual delivery time.
    actual_time = selected[
        'order_id'
    ].map(
        delivery_lookup[
            'actual_delivery_time_min'
        ]
    )

    # Get estimated delivery time.
    estimated_time = selected[
        'order_id'
    ].map(
        delivery_lookup[
            'estimated_delivery_time_min'
        ]
    )

    # Calculate delivery delay.
    delay = (
        actual_time
        - estimated_time
    )

    # --------------------------------------------------------
    # Generate rating.
    # --------------------------------------------------------

    # Start with an average rating around 4.2.
    #
    # Larger positive delivery delays reduce the rating.
    # Random noise makes the relationship imperfect.
    rating_score = (

        4.2

        - (
            delay.clip(
                lower=0
            )
            * 0.055
        )

        + np.random.normal(
            0,
            0.65,
            eligible_count
        )
    )

    # Round to nearest whole-number rating between 1 and 5.
    ratings = np.clip(

        np.rint(
            rating_score
        ),

        1,

        5

    ).astype(int)

    # Store generated review text.
    review_texts = []

    # Store sentiment labels.
    sentiments = []

    # --------------------------------------------------------
    # Generate review text.
    # --------------------------------------------------------

    for rating in ratings:

        # Determine sentiment from rating.
        if rating >= 4:

            sentiment = 'Positive'

        elif rating == 3:

            sentiment = 'Neutral'

        else:

            sentiment = 'Negative'

        # Save sentiment.
        sentiments.append(
            sentiment
        )

        # ----------------------------------------------------
        # Positive review
        # ----------------------------------------------------

        if sentiment == 'Positive':

            # Select random components.
            opening = np.random.choice(
                POSITIVE_OPENINGS
            )

            food_comment = np.random.choice(
                POSITIVE_FOOD
            )

            delivery_comment = np.random.choice(
                POSITIVE_DELIVERY
            )

            packaging_comment = np.random.choice(
                POSITIVE_PACKAGING
            )

            # Randomly choose review structure.
            review_style = np.random.choice(

                [
                    'full',
                    'food_delivery',
                    'short',
                    'food_packaging',
                ],

                p=[
                    0.40,
                    0.30,
                    0.15,
                    0.15,
                ]
            )

            # Construct review based on selected structure.
            if review_style == 'full':

                text = (
                    f'{opening} '
                    f'{food_comment} '
                    f'{delivery_comment}'
                )

            elif review_style == 'food_delivery':

                text = (
                    f'{food_comment} '
                    f'{delivery_comment}'
                )

            elif review_style == 'food_packaging':

                text = (
                    f'{food_comment} '
                    f'{packaging_comment}'
                )

            else:

                text = opening

        # ----------------------------------------------------
        # Neutral review
        # ----------------------------------------------------

        elif sentiment == 'Neutral':

            opening = np.random.choice(
                NEUTRAL_OPENINGS
            )

            food_comment = np.random.choice(
                NEUTRAL_FOOD
            )

            delivery_comment = np.random.choice(
                NEUTRAL_DELIVERY
            )

            packaging_comment = np.random.choice(
                NEUTRAL_PACKAGING
            )

            review_style = np.random.choice(

                [
                    'full',
                    'food_delivery',
                    'short',
                    'food_packaging',
                ],

                p=[
                    0.40,
                    0.30,
                    0.15,
                    0.15,
                ]
            )

            if review_style == 'full':

                text = (
                    f'{opening} '
                    f'{food_comment} '
                    f'{delivery_comment}'
                )

            elif review_style == 'food_delivery':

                text = (
                    f'{food_comment} '
                    f'{delivery_comment}'
                )

            elif review_style == 'food_packaging':

                text = (
                    f'{food_comment} '
                    f'{packaging_comment}'
                )

            else:

                text = opening

        # ----------------------------------------------------
        # Negative review
        # ----------------------------------------------------

        else:

            opening = np.random.choice(
                NEGATIVE_OPENINGS
            )

            food_comment = np.random.choice(
                NEGATIVE_FOOD
            )

            delivery_comment = np.random.choice(
                NEGATIVE_DELIVERY
            )

            packaging_comment = np.random.choice(
                NEGATIVE_PACKAGING
            )

            review_style = np.random.choice(

                [
                    'full',
                    'food_delivery',
                    'short',
                    'food_packaging',
                ],

                p=[
                    0.40,
                    0.30,
                    0.15,
                    0.15,
                ]
            )

            if review_style == 'full':

                text = (
                    f'{opening} '
                    f'{food_comment} '
                    f'{delivery_comment}'
                )

            elif review_style == 'food_delivery':

                text = (
                    f'{food_comment} '
                    f'{delivery_comment}'
                )

            elif review_style == 'food_packaging':

                text = (
                    f'{food_comment} '
                    f'{packaging_comment}'
                )

            else:

                text = opening

        # Store generated review.
        review_texts.append(
            text
        )

    # --------------------------------------------------------
    # Create reviews DataFrame.
    # --------------------------------------------------------

    reviews = pd.DataFrame({

        # Review ID.
        'review_id': [
            f'REV_{i:06d}'
            for i in range(
                1,
                eligible_count + 1
            )
        ],

        # Related order.
        'order_id': selected[
            'order_id'
        ].values,

        # Customer who wrote the review.
        'customer_id': selected[
            'customer_id'
        ].values,

        # Restaurant being reviewed.
        'restaurant_id': selected[
            'restaurant_id'
        ].values,

        # Review rating.
        'review_rating': ratings,

        # Review text.
        'review_text': review_texts,

        # Sentiment label.
        'sentiment': sentiments,
    })

    return reviews


# ============================================================
# 15. DATA VALIDATION
# ============================================================

def validate_data(
    customers,
    restaurants,
    drivers,
    orders,
    deliveries,
    payments,
    reviews
):
    """
    Validate the generated datasets.

    Checks include:
    - Primary keys
    - Foreign keys
    - Numeric ranges
    - Date relationships
    - Delivery relationships
    - Review relationships
    - Payment amounts
    """

    # Store validation errors.
    errors = []

    # --------------------------------------------------------
    # Primary key validation.
    # --------------------------------------------------------

    primary_keys = {

        'customers': (
            'customer_id',
            customers
        ),

        'restaurants': (
            'restaurant_id',
            restaurants
        ),

        'drivers': (
            'driver_id',
            drivers
        ),

        'orders': (
            'order_id',
            orders
        ),

        'deliveries': (
            'delivery_id',
            deliveries
        ),

        'payments': (
            'payment_id',
            payments
        ),

        'reviews': (
            'review_id',
            reviews
        ),
    }

    # Check every primary key.
    for name, (
        column,
        dataframe
    ) in primary_keys.items():

        # Primary keys must be unique.
        if not dataframe[
            column
        ].is_unique:

            errors.append(
                f'{name}.{column} '
                f'contains duplicate values.'
            )

        # Primary keys cannot contain nulls.
        if dataframe[
            column
        ].isna().any():

            errors.append(
                f'{name}.{column} '
                f'contains missing values.'
            )

    # --------------------------------------------------------
    # Foreign key validation.
    # --------------------------------------------------------

    # Check customer IDs in orders.
    if not orders[
        'customer_id'
    ].isin(
        customers[
            'customer_id'
        ]
    ).all():

        errors.append(
            'Orders contain invalid customer_id values.'
        )

    # Check restaurant IDs in orders.
    if not orders[
        'restaurant_id'
    ].isin(
        restaurants[
            'restaurant_id'
        ]
    ).all():

        errors.append(
            'Orders contain invalid restaurant_id values.'
        )

    # Check order IDs in deliveries.
    if not deliveries[
        'order_id'
    ].isin(
        orders[
            'order_id'
        ]
    ).all():

        errors.append(
            'Deliveries contain invalid order_id values.'
        )

    # Check driver IDs in deliveries.
    if not deliveries[
        'driver_id'
    ].isin(
        drivers[
            'driver_id'
        ]
    ).all():

        errors.append(
            'Deliveries contain invalid driver_id values.'
        )

    # Check order IDs in payments.
    if not payments[
        'order_id'
    ].isin(
        orders[
            'order_id'
        ]
    ).all():

        errors.append(
            'Payments contain invalid order_id values.'
        )

    # Check order IDs in reviews.
    if not reviews[
        'order_id'
    ].isin(
        orders[
            'order_id'
        ]
    ).all():

        errors.append(
            'Reviews contain invalid order_id values.'
        )

    # Check customer IDs in reviews.
    if not reviews[
        'customer_id'
    ].isin(
        customers[
            'customer_id'
        ]
    ).all():

        errors.append(
            'Reviews contain invalid customer_id values.'
        )

    # Check restaurant IDs in reviews.
    if not reviews[
        'restaurant_id'
    ].isin(
        restaurants[
            'restaurant_id'
        ]
    ).all():

        errors.append(
            'Reviews contain invalid restaurant_id values.'
        )

    # --------------------------------------------------------
    # Numeric validation.
    # --------------------------------------------------------

    # Customer ages must be between 18 and 65.
    if not customers[
        'age'
    ].between(
        18,
        65
    ).all():

        errors.append(
            'Customer ages outside 18-65.'
        )

    # Restaurant ratings must be between 1 and 5.
    if not restaurants[
        'restaurant_rating'
    ].between(
        1.0,
        5.0
    ).all():

        errors.append(
            'Restaurant ratings outside 1-5.'
        )

    # Driver ratings must be between 1 and 5.
    if not drivers[
        'driver_rating'
    ].between(
        1.0,
        5.0
    ).all():

        errors.append(
            'Driver ratings outside 1-5.'
        )

    # Driver experience cannot be negative.
    if (
        drivers[
            'experience_years'
        ] < 0
    ).any():

        errors.append(
            'Negative driver experience.'
        )

    # Driver experience cannot exceed possible working age.
    if (
        drivers[
            'experience_years'
        ]
        > (
            drivers[
                'age'
            ]
            - 18
        )
    ).any():

        errors.append(
            'Driver experience exceeds possible working age.'
        )

    # Restaurant prices must be positive.
    if (
        restaurants[
            'average_price'
        ] <= 0
    ).any():

        errors.append(
            'Restaurant prices must be positive.'
        )

    # Order amounts must be positive.
    if (
        orders[
            'order_amount'
        ] <= 0
    ).any():

        errors.append(
            'Order amounts must be positive.'
        )

    # Tips cannot be negative.
    if (
        orders[
            'tip_amount'
        ] < 0
    ).any():

        errors.append(
            'Tip amounts cannot be negative.'
        )

    # Delivery distance must be positive.
    if (
        deliveries[
            'delivery_distance_km'
        ] <= 0
    ).any():

        errors.append(
            'Delivery distances must be positive.'
        )

    # Preparation time must be positive.
    if (
        deliveries[
            'preparation_time_min'
        ] <= 0
    ).any():

        errors.append(
            'Preparation times must be positive.'
        )

    # Estimated delivery time must be positive.
    if (
        deliveries[
            'estimated_delivery_time_min'
        ] <= 0
    ).any():

        errors.append(
            'Estimated delivery times must be positive.'
        )

    # Actual delivery time must be positive.
    if (
        deliveries[
            'actual_delivery_time_min'
        ] <= 0
    ).any():

        errors.append(
            'Actual delivery times must be positive.'
        )

    # Payment amounts cannot be negative.
    if (
        payments[
            'transaction_amount'
        ] < 0
    ).any():

        errors.append(
            'Payment transaction amounts cannot be negative.'
        )

    # Review ratings must be between 1 and 5.
    if not reviews[
        'review_rating'
    ].between(
        1,
        5
    ).all():

        errors.append(
            'Review ratings outside 1-5.'
        )

    # --------------------------------------------------------
    # Signup date validation.
    # --------------------------------------------------------

    # Create lookup from customer ID to signup date.
    signup_lookup = customers.set_index(
        'customer_id'
    )[
        'signup_date'
    ]

    # Map signup dates to every order.
    mapped_signup = orders[
        'customer_id'
    ].map(
        signup_lookup
    )

    # Signup must happen before the order.
    if (
        mapped_signup
        >= orders[
            'order_timestamp'
        ].dt.normalize()
    ).any():

        errors.append(
            'Some customer signup dates '
            'are not before order dates.'
        )

    # --------------------------------------------------------
    # Delivered order validation.
    # --------------------------------------------------------

    # Get all delivered order IDs.
    delivered_ids = set(
        orders.loc[
            orders[
                'order_status'
            ] == 'Delivered',
            'order_id'
        ]
    )

    # Get order IDs that have delivery records.
    delivery_ids = set(
        deliveries[
            'order_id'
        ]
    )

    # Every delivered order must have a delivery record.
    if delivered_ids != delivery_ids:

        missing_deliveries = (
            delivered_ids
            - delivery_ids
        )

        if missing_deliveries:

            errors.append(
                'Some delivered orders '
                'have no delivery record.'
            )

    # --------------------------------------------------------
    # Cancelled/failed order validation.
    # --------------------------------------------------------

    # Get cancelled and failed orders.
    invalid_delivery_orders = (

        set(

            orders.loc[

                orders[
                    'order_status'
                ].isin(
                    [
                        'Cancelled',
                        'Failed'
                    ]
                ),

                'order_id'
            ]
        )

        & delivery_ids
    )

    # Cancelled and failed orders should not have deliveries.
    if invalid_delivery_orders:

        errors.append(
            'Cancelled/failed orders '
            'have delivery records.'
        )

    # --------------------------------------------------------
    # Review validation.
    # --------------------------------------------------------

    # Get order IDs referenced by reviews.
    review_order_ids = set(
        reviews[
            'order_id'
        ]
    )

    # Reviews must only belong to delivered orders.
    if not review_order_ids.issubset(
        delivered_ids
    ):

        errors.append(
            'Reviews contain non-delivered orders.'
        )

    # --------------------------------------------------------
    # Payment validation.
    # --------------------------------------------------------

    # Create order amount lookup.
    order_amount_lookup = orders.set_index(
        'order_id'
    )[
        'order_amount'
    ]

    # Get expected order amount for every payment.
    payment_order_amounts = payments[
        'order_id'
    ].map(
        order_amount_lookup
    )

    # Compare payment amount with order amount.
    if not np.allclose(

        payments[
            'transaction_amount'
        ].values,

        payment_order_amounts.values,

        rtol=0,

        atol=0.01
    ):

        errors.append(
            'Payment transaction amounts '
            'do not match order amounts.'
        )

    # --------------------------------------------------------
    # Final validation result.
    # --------------------------------------------------------

    # If any errors exist, stop execution and display them.
    if errors:

        raise ValueError(

            'Validation failed:\n- '

            + '\n- '.join(
                errors
            )
        )

    # If no errors exist, print success message.
    print(
        'Validation passed successfully.'
    )


# ============================================================
# 16. CSV EXPORT
# ============================================================

def export_data(
    customers,
    restaurants,
    orders,
    deliveries,
    drivers,
    reviews,
    payments
):
    """
    Export every generated DataFrame as a CSV file
    inside data/raw/.
    """

    # Store all datasets in one dictionary.
    datasets = {

        'customers.csv':
            customers,

        'restaurants.csv':
            restaurants,

        'orders.csv':
            orders,

        'deliveries.csv':
            deliveries,

        'drivers.csv':
            drivers,

        'reviews.csv':
            reviews,

        'payments.csv':
            payments,
    }

    # Export each DataFrame.
    for filename, dataframe in datasets.items():

        # Construct output path.
        path = (
            OUTPUT_DIR
            / filename
        )

        # Save CSV without the Pandas index.
        dataframe.to_csv(
            path,
            index=False
        )

    # --------------------------------------------------------
    # Display generation summary.
    # --------------------------------------------------------

    print(
        '\nGenerated datasets:'
    )

    print(
        '-' * 45
    )

    # Display dataset name and row count.
    for filename, dataframe in datasets.items():

        print(

            f'{filename:<20}'

            f'{len(dataframe):>8,} rows'
        )

    print(
        '-' * 45
    )

    # Display absolute output location.
    print(
        f'Output directory: '
        f'{OUTPUT_DIR.resolve()}'
    )


# ============================================================
# 17. MAIN EXECUTION
# ============================================================

def main():
    """
    Main execution pipeline.

    Order of operations:

    1. Generate customers
    2. Generate restaurants
    3. Generate drivers
    4. Generate orders
    5. Generate deliveries
    6. Generate payments
    7. Generate reviews
    8. Validate all datasets
    9. Export CSV files
    """

    # Display start message.
    print(
        'Generating synthetic food-delivery '
        'marketplace data...\n'
    )

    # --------------------------------------------------------
    # Generate master/reference datasets.
    # --------------------------------------------------------

    customers = generate_customers()

    restaurants = generate_restaurants()

    drivers = generate_drivers()

    # --------------------------------------------------------
    # Generate transactional datasets.
    # --------------------------------------------------------

    orders = generate_orders(
        customers,
        restaurants
    )

    deliveries = generate_deliveries(
        orders,
        drivers
    )

    payments = generate_payments(
        orders
    )

    reviews = generate_reviews(
        orders,
        deliveries
    )

    # --------------------------------------------------------
    # Validate generated data.
    # --------------------------------------------------------

    validate_data(

        customers,

        restaurants,

        drivers,

        orders,

        deliveries,

        payments,

        reviews
    )

    # --------------------------------------------------------
    # Export datasets to CSV.
    # --------------------------------------------------------

    export_data(

        customers,

        restaurants,

        orders,

        deliveries,

        drivers,

        reviews,

        payments
    )

    # Display completion message.
    print(
        '\nData generation completed successfully.'
    )


# ============================================================
# 18. SCRIPT ENTRY POINT
# ============================================================

# This ensures main() runs only when this file is executed
# directly, rather than when it is imported into another script.
if __name__ == '__main__':

    main()