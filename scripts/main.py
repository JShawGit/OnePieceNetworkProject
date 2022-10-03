from termcolor import colored
import pandas as pd
import json

data_path = "../data/data.json"
output_path = "../data/data.csv"


def read_json(path):
    with open(path) as fp:
        data = json.load(fp)
    return data


def read_character_data(data):
    # Store data attributes in a single dictionary
    name = list(data.keys())[0]
    statistics = data[name]['Statistics']
    row = {'Name': name}
    attr_list = [
        "Japanese Name",
        "Romanized Name",
        "Official English Name",
        "Debut",
        "Affiliations",
        "Occupations",
        "Status",
        "Birthday"
    ]
    for attr in attr_list:
        if attr in statistics: row[attr] = statistics[attr]
        else: row[attr] = None
    return pd.DataFrame([row])


def get_data(path):
    # Read the data in
    data = read_json(path)

    # Create a dataframe of data
    df = pd.DataFrame()

    # For each character in the data, get their attributes
    for character in data:
        row = read_character_data(character)
        df = pd.concat((df, row))
    return df


def main():
    df = get_data(data_path)
    df.to_csv(output_path, index=False)
    print(df)


if __name__ == "__main__":
    main()
