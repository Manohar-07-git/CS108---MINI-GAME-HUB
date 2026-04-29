import matplotlib.pyplot as plt

def charts():
    with open("history.csv", "r") as f:
        lines = f.readlines()
        data = []
        for line in lines:
            row = line.strip().split(",")
            data.append(row)

        winners = []
        games = []
        for row in data:
            winner = row[0].strip()
            game_name = row[3].strip()
            if winner != "tie":
                winners.append(winner)
                games.append(game_name)

        player_counts = {}
        for player in winners:
            if player in player_counts:
                player_counts[player] += 1
            else:
                player_counts[player] = 1

        top5 = sorted(player_counts.items(), key=lambda item: item[1], reverse=True)[:5]

        game_counts = {}
        for game in games:
            if game in game_counts:
                game_counts[game] += 1
            else:
                game_counts[game] = 1

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        players = [item[0] for item in top5]
        wins = [item[1] for item in top5]

        ax1.bar(players, wins, color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#c2c2f0'])
        ax1.set_title("Top 5 Players by Win Count", fontsize=14, fontweight='bold')
        ax1.set_xlabel("Players")
        ax1.set_ylabel("Total Wins")

        # Force the Y-axis to show only whole numbers
        ax1.yaxis.get_major_locator().set_params(integer=True)

        game_names = list(game_counts.keys())
        play_counts = list(game_counts.values())

        ax2.pie(
            play_counts,
            labels=game_names,
            autopct='%1.1f%%',
            startangle=140,
            colors=['#ffb3e6', '#c2c2f0', '#ff6666', '#c4e17f']
        )
        ax2.set_title("Most Played Games", fontsize=14, fontweight='bold')

        plt.tight_layout()
        plt.show()

charts()