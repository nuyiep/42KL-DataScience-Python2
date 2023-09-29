
import matplotlib.pyplot as plt
from load_csv import load


# Access data- https://www.youtube.com/watch?v=AzikJWKU77w&ab_channel=JonathanPerry
def aff_life(df):
	'''Draw life expectancy graph'''
	try:
		malaysia_data = df[df['country'] == 'Malaysia']
		years = malaysia_data.columns[1:].astype(int)
		life_expectancy = malaysia_data.values[0, 1:].astype(float) 
		# .values- returns a NumPy array representing the data in the DataFrame
		plt.plot(years, life_expectancy)
		plt.xlabel("Year")
		plt.ylabel("Life expectancy")
		plt.title("Malaysia Life expectancy Projections")
		plt.show()
	except Exception as err:
		print(err)
	except KeyboardInterrupt:
		print("Program interrupted by the user")


def main():
	'''Main'''
	df = load("../life_expectancy_years.csv")
	aff_life(df)


if __name__ == "__main__":
	main()
