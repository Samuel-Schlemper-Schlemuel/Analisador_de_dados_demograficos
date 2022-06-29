import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')
    race_count = df['race'].value_counts()
    average_age_men = round(df.groupby('sex')['age'].agg(['mean']).query('sex == "Male"').loc['Male'][0], 1)
    percentage_bachelors = round(df[df.education == "Bachelors"].shape[0] / df.shape[0] * 100, 1)
    higher_education = df[(df.education == 'Bachelors') | (df.education == 'Masters') | (df.education == 'Doctorate')]
    lower_education = df[(df.education != 'Bachelors') & (df.education != 'Masters') & (df.education != 'Doctorate')]
    higher_education_rich = round(higher_education[df.salary == '>50K'].shape[0] / higher_education.shape[0] * 100, 1)
    lower_education_rich = round(lower_education[df.salary == '>50K'].shape[0] / lower_education.shape[0] * 100, 1)
    min_work_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_work_hours][df.salary == '>50K'].shape[0]
    rich_percentage = round(df[df.salary == '>50K'].shape[0] / df.shape[0] * 100, 1)
    country_table = df.groupby(['native-country']).size()
    country_table_50K = df[df.salary == '>50K'].groupby(['native-country']).size()
    country_percentage = (country_table_50K / country_table)
    highest_earning_country = country_percentage.index[country_percentage == country_percentage.max()][0]
    highest_earning_country_percentage = round(country_percentage.max() * 100, 1)
    top_IN_occupation = df[(df.salary == '>50K') & (df['native-country'] == 'India')].groupby(['occupation']).size()
    top_IN_occupation = top_IN_occupation.index[top_IN_occupation == top_IN_occupation.max()][0]

    # DO NOT MODIFY BELOW THIS LINE

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
