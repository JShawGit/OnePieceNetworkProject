from termcolor import colored
import pandas as pd
import json
import csv

data_path = "../data/data.json"
attr_path = "../data/attributes.csv"
output_path = "../data/data.csv"


def read_json(path):
    """ Read a JSON file. """
    with open(path) as fp:
        data = json.load(fp)
    return data


def read_character_data(data):
    """ Store data attributes from a JSON-item into a single dictionary. """
    name = list(data.keys())[0]
    statistics = data[name]['Statistics']
    row = {'Name': name}
    with open(attr_path) as fp:
        attr_list = [i for s in list(csv.reader(fp, delimiter="\n")) for i in s]
    for attr in attr_list:
        if attr in statistics: row[attr] = statistics[attr]
        else: row[attr] = None
    return pd.DataFrame([row])


def get_data(path):
    """ Interpret the wiki-crawler results. """
    # Read the data in
    data = read_json(path)

    # For each character in the data, get their attributes
    df = pd.DataFrame()
    for character in data:
        row = read_character_data(character)
        df = pd.concat((df, row))
    return df


def main():
    """ Get a CSV of the character data. """
    df = get_data(data_path).sort_values("Name")
    df.to_csv(output_path, index=False)
    print(colored("Finished translating web-crawler data.", 'cyan'))


if __name__ == "__main__":
    main()
