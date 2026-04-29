import matplotlib.pyplot as plt
import os

def charts():
    # 1. Safety check: Ensure the file exists before trying to open it
    if not os.path.exists("history.csv"):
        print("No history.csv found. Play a game to generate data first!")
        return

    with open("history.csv", "r") as f:
        lines = f.readlines()
        
    data = []
    for line in lines:
        # 2. Safety check: Skip completely blank lines
        if not line.strip():
            continue
            
        row = line.strip().split(",")
        
        # 3. Safety check: Ensure the row actually has all 5 columns
        if len(row) >= 5:
            data.append(row)

    # 4. Safety check: Exit cleanly if the file was empty
    if not data:
        print("Not enough data to plot yet.")
        return

    winners = []
    games = []
    for row in data:
        winner = row[0].strip()
        game_name = row[4].strip()
        
        # 5. Logic fix: Add to the games list even if it was a tie!
        games.append(game_name)
        
        if winner.lower() != "tie":
            winners.append(winner)

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

    # Only plot the bar chart if someone has actually won a game
    if top5:
        players = [item[0] for item in top5]
        wins = [item[1] for item in top5]

        ax1.bar(players, wins, color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#c2c2f0'])
        ax1.set_title("Top 5 Players by Win Count", fontsize=14, fontweight='bold')
        ax1.set_xlabel("Players")
        ax1.set_ylabel("Total Wins")
        ax1.yaxis.get_major_locator().set_params(integer=True)
    else:
        ax1.set_title("Top 5 Players by Win Count", fontsize=14, fontweight='bold')
        ax1.text(0.5, 0.5, "No wins recorded yet", ha='center', va='center')

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

if __name__ == "__main__":
    charts()