# Module to find and plot the top 10 most economical bowlers in IPL 2015.

import csv
import matplotlib.pyplot as plt


BOWLER = "bowler"
TOTAL_RUNS = "total_runs"
ID = "id"
SEASON = "season"
IS_SUPER_OVER = "is_super_over"


def getting_match_ids_2015(file_path):
    """
    Extract match IDs for the 2015 IPL season.
    Args:
        matches_file (str): Path to the matches.csv file.
    Returns:
        set: A set of match IDs from the 2015 season.
    """
    match_id_2015 = set()

    with open(file_path, encoding="utf-8") as csv_file:
        match_reader = csv.DictReader(csv_file)
        for match_record in match_reader:
            if match_record[SEASON] == "2015":
                match_id_2015.add(match_record[ID])
    return match_id_2015


def calculate_top_10_economical_bowlers_2015(file_path, match_id_2015):
    """
    Calculate the economy rate for each bowler in the given matches.
    Args:
        deliveries_file (str): Path to the deliveries.csv file.
        match_ids (set): Set of match IDs for the 2015 season.
    Returns:
        dict: Bowler as key and their economy rate as value.
    """

    bowler_runs = {}
    bowler_balls = {}

    with open(file_path, encoding="utf-8") as csv_file:
        delivery_reader = csv.DictReader(csv_file)
        for delivery_record in delivery_reader:
            if (delivery_record["match_id"]
                    in match_id_2015 and delivery_record[IS_SUPER_OVER] == "0"):
                bowler = delivery_record[BOWLER]
                total_runs = int(delivery_record[TOTAL_RUNS])

                bowler_runs[bowler] = bowler_runs.get(bowler, 0) + total_runs
                bowler_balls[bowler] = bowler_balls.get(bowler, 0) + 1

    economy = {}
    for bowler in bowler_runs:
        overs = bowler_balls[bowler] / 6
        economy[bowler] = bowler_runs[bowler] / overs if overs > 0 else 0

    return economy


def getting_top_10_bowlers(economy):
    """
    Get the top 10 bowlers with the best (lowest) economy rates.
    Args:
        economy_data (dict): Dictionary with bowler names and economy rates.
    Returns:
        list: Top 10 bowlers sorted by economy rate.
    """

    top_10_bowlers = sorted(economy.items(), key=lambda x: x[1])[:10]

    return top_10_bowlers


def plot_top_10_bowlers_2015(top_10_bowlers):
    """
    Plot a bar chart of the top 10 economical bowlers in IPL 2015.
    Args:
        top_10_bowlers (list): List of tuples (bowler, economy_rate).
    """

    bowlers = sorted([bowler for bowler, economy in top_10_bowlers])
    economy_rate = sorted([economy for bowler, economy in top_10_bowlers])

    plt.figure(figsize=(10, 6))
    plt.bar(bowlers, economy_rate, color="red")

    plt.title("Top 10 Economical Bowlers in IPL 2015")
    plt.xlabel("Bowlers")
    plt.ylabel("Economy Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("ipl_project/outputs/problem8")
    plt.show()


def execute():
    unique_id = getting_match_ids_2015("ipl_project/data/matches.csv")
    economic_rates = calculate_top_10_economical_bowlers_2015(
        "ipl_project/data/deliveries.csv", unique_id)
    top_bowlers = getting_top_10_bowlers(economic_rates)
    plot_top_10_bowlers_2015(top_bowlers)


execute()

if __name__ == "__main__":
    execute()
