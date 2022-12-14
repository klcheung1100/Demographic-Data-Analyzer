import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = (((df.groupby("sex").get_group("Male"))["age"]).mean()).round(decimals = 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = ((((df["education"] == "Bachelors").value_counts(normalize=True).mul(100).round(1)))[True])

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[df["education"].isin(["HS-grad", "Some-college", "Assoc-voc", "11th", "Assoc-acdm", "10th", "7th-8th", "Prof-school", "9th", "12th", "5th-6th", "1st-4th", "Preschool" ])]

    # percentage with salary >50K
    higher_education_rich = ((((higher_education["salary"] == ">50K").value_counts(normalize=True).mul(100).round(1)))[True])
    lower_education_rich = ((((lower_education["salary"] == ">50K").value_counts(normalize=True).mul(100).round(1)))[True])

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = ((df["hours-per-week"] == min_work_hours).value_counts()[True])

    rich_percentage = ((((df.groupby("hours-per-week").get_group(min_work_hours)["salary"] == ">50K").value_counts(normalize=True).mul(100).round(1)))[True])

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = list(((((df.groupby('native-country')['salary'].value_counts(normalize=True)).mul(100).round(1))).groupby("salary").get_group(">50K")).idxmax())[0]
    highest_earning_country_percentage = (((df.groupby('native-country')['salary'].value_counts(normalize=True)).mul(100).round(1)).groupby("salary").get_group(">50K")).max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (((df.loc[((df["native-country"] == "India") & (df["salary"] == ">50K")), ["occupation"]])).mode())['occupation'].iloc[0]

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
