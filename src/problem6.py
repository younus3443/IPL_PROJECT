#Number of matches won per team per year in IPL.

import csv
import matplotlib.pyplot as plt

SEASON = "season"
WINNER = "winner"
TEAM1 = "team1"
TEAM2 = "team2"


def calculate_matches_won_per_team_per_year(file_path):

    matches_won = {}

    with open(file_path, encoding="utf-8") as csv_file:
        match_reader = csv.DictReader(csv_file)
        for match_record in match_reader:
            season = match_record[SEASON]
            winner = match_record[WINNER]

            if not winner:
                continue
            if season not in matches_won:
                matches_won[season] = {}
            matches_won[season][winner] = matches_won[season].get(
                winner, 0) + 1
    return matches_won


a = calculate_matches_won_per_team_per_year("ipl_project/data/matches.csv")
print(a)


def plot_matches_won_per_team_per_year(matches_won):
    seasons = sorted(matches_won.keys())
    all_teams = sorted({team for season in matches_won.values()
                       for team in season.keys()})

    team_count = {team: [] for team in all_teams}

    for season in seasons:
        for team in all_teams:
            team_count[team].append(matches_won[season].get(team, 0))

    plt.figure(figsize=(14, 8))
    width = 0.6
    bottom = [0] * len(seasons)

    for team in all_teams:
        plt.bar(seasons, team_count[team], width, bottom=bottom, label=team)
        bottom = [bottom[i] + team_count[team][i] for i in range(len(seasons))]

    plt.xlabel("Season")
    plt.ylabel("Matches Won")
    plt.title("Matches Won by Each Team per Year in IPL")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    # plt.savefig("ipl_project/outputs/problem6")
    plt.show()


def execute():
    matches_won = calculate_matches_won_per_team_per_year(
        "ipl_project/data/matches.csv")
    plot_matches_won_per_team_per_year(matches_won)


execute()

if __name__ == "__main__":
    execute()
