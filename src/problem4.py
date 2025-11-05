#Stacked chart of matches played by team by season

import csv
import matplotlib.pyplot as plt

SEASON = "season"
TEAM1 = "team1"
TEAM2 = "team2"


def calculate_by_team_by_season(file_path):
    matches_data = {}

    with open(file_path, encoding='utf-8') as csv_file:
        matches_reader = csv.DictReader(csv_file)
        for match_record in matches_reader:
            season = match_record[SEASON]
            team1 = match_record[TEAM1]
            team2 = match_record[TEAM2]

            if season not in matches_data:
                matches_data[season] = {}

            matches_data[season][team1] = matches_data[season].get(
                team1, 0) + 1
            matches_data[season][team2] = matches_data[season].get(
                team2, 0) + 1

    return matches_data


def plot_by_team_by_season(matches_data):

    seasons = sorted(matches_data.keys())
    all_teams = sorted({team for season in matches_data.values()
                       for team in season.keys()})

    team_count = {team: [] for team in all_teams}

    for season in seasons:
        for team in all_teams:
            team_count[team].append(matches_data[season].get(team, 0))
    plt.figure(figsize=(14, 8))
    bar_width = 0.6
    bottom = [0] * len(seasons)

    for team in all_teams:
        plt.bar(
            seasons,
            team_count[team],
            bar_width,
            bottom=bottom,
            label=team)
        bottom = [bottom[i] + team_count[team][i] for i in range(len(seasons))]

    plt.xlabel("Season")
    plt.ylabel("Number of Matches Played")
    plt.title("Matches Played by Each Team (Stacked by Season)")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    # plt.savefig('ipl_project/outputs/problem4')
    plt.show()


def execute():
    matches_data = calculate_by_team_by_season("ipl_project/data/matches.csv")
    plot_by_team_by_season(matches_data)


execute()

if __name__ == "__main__":
    execute()
