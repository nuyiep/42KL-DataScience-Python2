
import pandas as pd


def load(path: str):
    '''Read csv file into a panda dataframe'''
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions ", end='')
        print(df.shape)
        # or
        # print(f"Loading dataset of dimensions {data.shape}")
        return (df)
    except FileNotFoundError:
        print("The file does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty")
        return None
    except pd.errors.ParserError as e:
        print(f"Error parsing the CSV file: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
