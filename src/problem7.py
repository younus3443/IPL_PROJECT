#Extra runs conceded per team in the year 2016

import csv
import matplotlib.pyplot as plt

SEASON = "season"
ID = "id"
EXTRA_RUNS = "extra_runs"
BOWLING_TEAM = "bowling_team"


def getting_match_id_2016(file_path):
    match_id_2016 = set()

    with open(file_path, encoding="utf-8")as csv_file:
        match_reader = csv.DictReader(csv_file)
        for match_record in match_reader:
            if match_record[SEASON] == "2016":
                match_id_2016.add(match_record[ID])
    return match_id_2016


def calculate_extra_runs_by_team_2016(file_path, match_id_2016):
    extra_runs_by_team = {}
    with open(file_path, encoding="utf-8") as csv_file:
        deliveries_reader = csv.DictReader(csv_file)
        for delivery_record in deliveries_reader:
            if delivery_record["match_id"] in match_id_2016:
                bowling_team = delivery_record[BOWLING_TEAM]
                extra_runs = int(delivery_record[EXTRA_RUNS])

                extra_runs_by_team[bowling_team] = extra_runs_by_team.get(
                    bowling_team, 0) + extra_runs
    return extra_runs_by_team


def plot_extra_runs_by_team_2016(extra_runs_by_team):
    team = list(extra_runs_by_team.keys())
    runs = list(extra_runs_by_team.values())

    plt.figure(figsize=(10, 6))
    plt.bar(team, runs, color="orange")
    plt.title("Extra runs conceded per team in 2016")
    plt.xlabel("Teams")
    plt.ylabel("Extra runs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.savefig("ipl_project/outputs/problem7")
    plt.show()


def execute():
    unique_ids = getting_match_id_2016("ipl_project/data/matches.csv")
    extra_runs = calculate_extra_runs_by_team_2016(
        "ipl_project/data/deliveries.csv", unique_ids)
    plot_extra_runs_by_team_2016(extra_runs)


execute()

if __name__ == "__main__":
    execute()
