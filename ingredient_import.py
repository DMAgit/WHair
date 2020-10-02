import pandas as pd
import os


def ingredient_import(path, filename):
    """
    takes in a csv file that looks like:

    name        0           1               2               3
    ingredient  good/NaN    acceptable/NaN  caution/NaN     avoid/NaN

    goal is to format it to look like:

    name          status
    ingredient    0/1/2/3        - 0: good
                                 - 1: acceptable
                                 - 2: caution
                                 - 3: avoid

    :param path: working directory path
    :param filename: name of .csv file to be processed
    :return df: reformatted dataframe
    """

    os.chdir(path)

    df = pd.read_csv(filename)
    df = df.dropna(how="all")  # drop all rows that don't contain any data
    df.columns = ["name", "0", "1", "2", "3"]

    df["status"] = df["0"].fillna("") + df["1"].fillna("") + df["2"].fillna("") + df["3"].fillna("")  # combine columns
                                                                                                      # into status column
    df = df.drop(["0", "1", "2", "3"], axis=1)  # drop old columns
    df["status"] = df["status"].str.replace("Good", "0")  # replace words with categorical data
    df["status"] = df["status"].str.replace("Okay", "1")
    df["status"] = df["status"].str.replace("Caution", "2")
    df["status"] = df["status"].str.replace("Avoid", "3")
    return df
