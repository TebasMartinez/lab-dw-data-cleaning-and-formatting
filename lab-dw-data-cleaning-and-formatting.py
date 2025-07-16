import pandas as pd

def main():
    car_df = open_doc("https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv")
    car_df.columns = clean_columns(car_df)
    car_df["gender"] = standardize_gender(car_df)
    car_df.state = standardize_states(car_df)
    car_df.education = standardize_education(car_df)
    car_df.customer_lifetime_value = standardize_customer_lifetime_value(car_df)
    car_df.vehicle_class = standardize_vehicle_class(car_df)
    car_df.number_open_complaints = format_complaints(car_df)
    car_df = clean_nulls(car_df)
    car_df[car_df.select_dtypes(include='number').columns] = make_numerics_nums(car_df)
    print(car_df.head())


def open_doc(url):
    return pd.read_csv(url)

def clean_columns(car_df):
     return ['customer', 'state', 'gender', 'education', 'customer_lifetime_value',
       'income', 'monthly_premium', 'number_open_complaints',
       'policy_type', 'vehicle_class', 'total_claim_amount']

def standardize_gender(car_df):
    return car_df["gender"].apply(lambda x: "F" if x == "F" or x == "Femal" or x == "female" else "M")

def standardize_states(car_df):
    states_mapping = {
    "Washington" : "Washington",
    "Arizona" : "Arizona",
    "Nevada" : "Nevada",
    "California" : "California",
    "Oregon" : "Oregon",
    "Cali" : "California",
    "AZ" : "Arizona",
    "WA" : "Washington"
    }
    return car_df.state.map(states_mapping)

def standardize_education(car_df):
     return car_df.education.apply(lambda x: "Bachelor" if x == "Bachelors" else x)

def standardize_customer_lifetime_value(car_df):
    car_df.customer_lifetime_value = car_df.customer_lifetime_value.apply(lambda x: float(str(x).replace("%","")))
    car_df.customer_lifetime_value = car_df.customer_lifetime_value.apply(lambda x: float(x))
    return car_df.customer_lifetime_value

def standardize_vehicle_class(car_df):
    luxury_mapping = {
    "Sports Car" : "Luxury",
    "Luxury SUV" : "Luxury",
    "Luxury Car" : "Luxury",
    "Four-Door Car" : "Four-Door Car",
    "Two-Door Car" : "Two-Door Car",
    "SUV" : "SUV"
    }
    return car_df.vehicle_class.map(luxury_mapping)

def format_complaints(car_df):
    return car_df.number_open_complaints.apply(lambda x: int((format(x).split("/"))[1]) if isinstance(x,str) else x)

def clean_nulls(car_df):
    car_df.dropna(thresh=2, inplace=True)
    car_df.customer_lifetime_value.fillna(car_df.customer_lifetime_value.mean(), inplace=True)
    return car_df

def make_numerics_nums(car_df):
    return car_df.select_dtypes(include='number').astype(int)

main()