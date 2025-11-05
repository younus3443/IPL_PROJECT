#Foreign umpire analysis

import csv
import matplotlib.pyplot as plt

UMPIRE = "umpire"
COUNTRY = "country"


def calculate_umpires_data(file_path):
    foreign_umpires = {}

    with open(file_path, encoding="utf-8") as csv_file:
        umpires_reader = csv.DictReader(csv_file)

        for umpire_record in umpires_reader:
            if umpire_record[COUNTRY] != "India":
                umpire = umpire_record[UMPIRE]
                country = umpire_record[COUNTRY]

                foreign_umpires[country] = foreign_umpires.get(country, 0) + 1
    return foreign_umpires


a = calculate_umpires_data("ipl_project/data/umpires.csv")


def plot_umpires_data(foreign_umpires):

    country = list(foreign_umpires.keys())
    umpires = list(foreign_umpires.values())

    plt.figure(figsize=(10, 6))
    plt.bar(country, umpires)
    plt.title("Foreign umpire analysis")
    plt.xlabel("Country")
    plt.ylabel("Umpires")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.savefig("ipl_project/outputs/problem3")
    plt.show()


def execute():
    foreign_umpires = calculate_umpires_data("ipl_project/data/umpires.csv")
    plot_umpires_data(foreign_umpires)


execute()

if __name__ == "__main__":
    execute()
