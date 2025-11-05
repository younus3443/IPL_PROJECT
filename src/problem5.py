#Number of matches played per year for all the years in IPL.

import csv
import matplotlib.pyplot as plt

SEASON = "season"


def calculate_match_per_year_all_years(file_path):

    matches_per_year = {}
    with open(file_path, encoding="utf-8")as csv_file:
        match_reader = csv.DictReader(csv_file)
        for match_record in match_reader:
            season = match_record[SEASON]

            matches_per_year[season] = matches_per_year.get(season, 0) + 1
    return matches_per_year


def plot_match_per_year_all_years(matches_per_year):
    seasons = sorted((matches_per_year.keys()))
    matches = list(matches_per_year.values())

    plt.figure(figsize=(10, 6))
    plt.bar(seasons, matches)
    plt.title("Matches Played per Year for all the Years in IPL.")
    plt.xlabel("Seasons")
    plt.ylabel("Matches")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.savefig("ipl_project/outputs/proble5")
    plt.show()


def execute():
    matches = calculate_match_per_year_all_years(
        "ipl_project/data/matches.csv")
    plot_match_per_year_all_years(matches)


execute()

if __name__ == "__main__":
    execute()
