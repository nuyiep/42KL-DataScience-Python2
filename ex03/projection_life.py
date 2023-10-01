
import matplotlib.pyplot as plt
from load_csv import load


def get_data(df_data, year):
    '''Get data for year 1900'''
    try:
        year = int(year)
        x_data = df_data[str(year)].tolist()
    except Exception as err:
        print(err)
    return (x_data)


def display_info(df_income, df_le):
    '''Generate scatter plot'''
    try:
        income = get_data(df_income, 1900)
        le = get_data(df_le, 1900)
        plt.scatter(income, le)
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expectancy")
        plt.title("1900")
        plt.xscale("log")  # change the scale to logar
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.show()
    except Exception as err:
        print(err)
    except KeyboardInterrupt:
        print("Program is interrupted by the user")


def main():
    '''Main'''
    df_income = load(
        "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_le = load("../life_expectancy_years.csv")
    display_info(df_income, df_le)


if __name__ == "__main__":
    main()
