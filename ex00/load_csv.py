
import pandas as pd


def load(path: str):
    '''Read csv file into a pandas dataframe'''
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions ", end='')
        print(df.shape)
        # or
        # print(f"Loading dataset of dimensions {data.shape}")
        return (df)
    except FileNotFoundError:
        print("The file does not exist.")
    except pd.errors.EmptyDataError:
        print("The file is empty")
    except pd.errors.ParserError as e:
        print(f"Error parsing the CSV file: {e}")
        # return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # return None

# if except didn't return anything, it will automatically return None
