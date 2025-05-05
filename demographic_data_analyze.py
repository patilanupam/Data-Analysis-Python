import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    # 1) How many of each race?
    race_count = df['race'].value_counts()

    # 2) Average age of women
    avg_age_women = round(df[df['sex'] == 'Female']['age'].mean(), 1)

    # 3) % with Bachelor's degree
    pct_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4+5) % with/without advanced education earning >50K
    high_ed = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    low_ed  = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    high_ed_rich = round((high_ed['salary'] == '>50K').mean() * 100, 1)
    low_ed_rich  = round((low_ed['salary'] == '>50K').mean() * 100, 1)

    # 6) Min hours worked per week
    min_hours = df['hours-per-week'].min()

    # 7) % rich among those who work min hours
    min_workers = df[df['hours-per-week'] == min_hours]
    rich_min_workers_pct = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8) Country with highest % of >50K earners
    country_counts = df['native-country'].value_counts()
    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_pct = (rich_by_country / country_counts * 100).fillna(0)
    top_country = country_pct.idxmax()
    top_country_pct = round(country_pct.max(), 1)

    # 9) % of >50K earners in India
    india_pct = round(country_pct.get('India', 0), 1)

    if print_data:
        print("Race count:\n", race_count, "\n")
        print("Average age of women:", avg_age_women)
        print("% with Bachelor's:", pct_bachelors)
        print("% rich with higher education:", high_ed_rich)
        print("% rich without higher education:", low_ed_rich)
        print("Min work hours:", min_hours)
        print("% rich among min workers:", rich_min_workers_pct)
        print("Top earning country:", top_country, top_country_pct)
        print("% rich in India:", india_pct)

    return {
        'race_count': race_count.to_dict(),
        'average_age_women': avg_age_women,
        'percentage_bachelors': pct_bachelors,
        'higher_education_rich': high_ed_rich,
        'lower_education_rich': low_ed_rich,
        'min_work_hours': min_hours,
        'rich_percentage_min_workers': rich_min_workers_pct,
        'highest_earning_country': top_country,
        'highest_earning_country_percentage': top_country_pct,
        'india_rich_percentage': india_pct
    }

if __name__ == '__main__':
    calculate_demographic_data()
