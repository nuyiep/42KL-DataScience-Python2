
import matplotlib.pyplot as plt
from load_csv import load
from matplotlib.ticker import FuncFormatter


def format_population(value, _):
    '''Format population at y-axis in million unit'''
    if value >= 1e6:
        return f'{int(value / 1e6)}M'
    else:
        return f'{int(value)}'


def get_data(df):
    '''Get data after zipped'''
    years = df.columns[1:].astype(int)
    pop = df.values[0, 1:]
    new_years = []
    new_pop = []
    zipped_data = zip(years, pop)
    for (a, b) in zipped_data:
        if (a <= 2050):
            new_years.append(a)
            new_pop.append(b)
    return (new_years, new_pop)


def expand_numbers(new_pop):
    '''Expand k, M and B'''
    # list comprehension
    # msia_pop = [pop.rstrip('k') if 'k' in pop else pop for pop in msia_pop]
    # # create an empty list to store the stripped population values
    stripped_pop = []
    for i in new_pop:
        if 'k' in i:
            stripped_pop.append((float(i.rstrip("k")) * 1000))
        elif 'M' in i:
            stripped_pop.append((float(i.rstrip("M")) * 1000000))
        elif 'B' in i:
            stripped_pop.append((float(i.rstrip("B")) * 1000000000))
        else:
            stripped_pop.append(i)
    return stripped_pop


def display_info(df):
    '''Display graph'''
    try:
        country_a = df[df["country"] == 'France']
        country_b = df[df["country"] == 'Belgium']
        a_new_years, a_new_pop = get_data(country_a)
        b_new_years, b_new_pop = get_data(country_b)
        a_stripped_pop = expand_numbers(a_new_pop)
        b_stripped_pop = expand_numbers(b_new_pop)
        plt.plot(a_new_years, a_stripped_pop, label="France")
        plt.plot(b_new_years, b_stripped_pop, label="Belgium")
        ax = plt.gca()  # display
        ax.yaxis.set_major_formatter(FuncFormatter(format_population))
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population Projections")
        plt.legend()
        plt.show()
    except Exception as error:
        print(error)
    except KeyboardInterrupt:
        print("Program interrupted by the user")


def main():
    '''Main'''
    df = load("../population_total.csv")
    display_info(df)


if __name__ == "__main__":
    main()
