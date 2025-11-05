#Total runs scored by team

import csv
import matplotlib.pyplot as plt

BATTING_TEAM = "batting_team"
TOTAL_RUNS = "total_runs"


def calculate_total_runs_each_team(file_path):
    team_runs = {}
    with open(file_path) as csv_file:
        deliveries_reader = csv.DictReader(csv_file)
        for match in deliveries_reader:
            team = match[BATTING_TEAM]
            runs = int(match[TOTAL_RUNS])

            team_runs[team] = team_runs.get(team, 0) + runs

    return team_runs


def plot_total_runs_each_team(file_path):
    teams = list(file_path.keys())
    runs = list(file_path.values())

    plt.figure(figsize=(12, 6))
    plt.bar(teams, runs, color="orange")
    plt.title("Total runs scored by team")
    plt.xlabel("Teams")
    plt.ylabel("Total runs")
    plt.xticks(rotation=45)
    for i, value in enumerate(runs):
        plt.text(i, value + 100, str(value), ha="center")
    plt.tight_layout()
    # plt.savefig("ipl_project/outputs/problem1")
    plt.show()


def execute():
    team_runs = calculate_total_runs_each_team(
        "ipl_project/data/deliveries.csv")
    plot_total_runs_each_team(team_runs)


execute()

if __name__ == "__main__":
    execute()
