#Top batsman for Royal Challengers Bangalore

import csv
import matplotlib.pyplot as plt

BATTING_TEAM = "batting_team"
BATSMAN = "batsman"
BATSMAN_RUNS = "batsman_runs"


def calculate_top_batsman_rcb(file_path):
    top_batsmen = {}
    with open(file_path, encoding="utf-8") as csv_file:
        delivery_reader = csv.DictReader(csv_file)
        for delivery_record in delivery_reader:
            if delivery_record[BATTING_TEAM] == "Royal Challengers Bangalore":
                batsman = delivery_record[BATSMAN]
                runs = int(delivery_record[BATSMAN_RUNS])

                top_batsmen[batsman] = top_batsmen.get(batsman, 0) + runs
    top10_batsmen = sorted(
        top_batsmen.items(),
        key=lambda x: x[1],
        reverse=True)[
        :10]
    return top10_batsmen


def plot_top_batsmen_rcb(top10_batsmen):
    batsmen = [batsman for batsman, runs in top10_batsmen]

    runs = [runs for batsman, runs in top10_batsmen]

    plt.figure(figsize=(12, 6))
    plt.bar(batsmen, runs, color="red")
    plt.title("Top batsman for Royal Challengers Bangalore")
    plt.xlabel("batsman")
    plt.ylabel("Runs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.savefig("ipl_project/outputs/problem2")
    plt.show()


def execute():
    top_batsmen = calculate_top_batsman_rcb("ipl_project/data/deliveries.csv")
    plot_top_batsmen_rcb(top_batsmen)


execute()

if __name__ == "__main__":
    execute()
