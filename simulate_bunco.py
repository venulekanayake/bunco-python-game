import random
from collections import Counter
import matplotlib.pyplot as plt

def simulate_bunco_game(no_of_players=6, reroll=False):
    """
    Simulate one game of Bunco with `no_of_players` players.
    Returns the winner player number (1-based).
    """
    score = [0] * no_of_players

    for player in range(no_of_players):
        # initial 6 dice rolls
        for _ in range(6):
            roll = random.randint(1,6)
            if roll == player + 1:
                score[player] += 1
        
        # optional random reroll for simulation
        if reroll:
            reroll_count = random.randint(0, 5)
            for _ in range(reroll_count):
                roll = random.randint(1,6)
                if roll == player + 1:
                    score[player] += 1

    # find the winner (first player with max score)
    max_score = max(score)
    winners = [i+1 for i, s in enumerate(score) if s == max_score]
    return winners[0]  # take the first if tie

# Run simulation 1000 times
num_simulations = 1000
results = []

for _ in range(num_simulations):
    winner = simulate_bunco_game()
    results.append(winner)

# Count how many times each player won
winner_counts = Counter(results)

# Display results
print("Winner counts after 1000 simulations:")
for player, count in sorted(winner_counts.items()):
    print(f"Player {player}: {count} wins")

print("\nWinner percentages:")
for player, count in sorted(winner_counts.items()):
    print(f"Player {player}: {count/num_simulations*100:.2f}%")

# Visualization
players = list(winner_counts.keys())
wins = list(winner_counts.values())

plt.bar(players, wins, color='skyblue')
plt.xlabel('Player Number')
plt.ylabel('Number of Wins')
plt.title('Bunco Simulation: 1000 Games')
plt.xticks(players)
plt.show()
