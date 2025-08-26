import random

# Mapping
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "Snake", -1: "Water", 0: "Gun"}

# Scoreboard
user_score = 0
comp_score = 0
rounds = 5  # best of 5

print("🐍💧🔫 Welcome to Snake Water Gun Game!")
print("Choices: s = Snake | w = Water | g = Gun\n")

for i in range(1, rounds + 1):
    print(f"--- Round {i} ---")

    computer = random.choice([1, -1, 0])
    youstr = input("Enter your choice (s/w/g): ").lower()

    if youstr not in youdict:
        print("❌ Invalid choice! Round skipped.\n")
        continue

    you = youdict[youstr]

    # Show choices
    print(f"You chose 👉 {reversedict[you]}")
    print(f"Computer chose 🤖 {reversedict[computer]}")

    # Decide winner
    if computer == you:
        print("😐 It's a Draw!\n")
    elif (computer == -1 and you == 1) or \
         (computer == 0 and you == -1) or \
         (computer == 1 and you == 0):
        print("🎉 You Win this round!\n")
        user_score += 1
    else:
        print("💀 Computer Wins this round!\n")
        comp_score += 1

# Final Result
print("===== Final Score =====")
print(f"👤 You: {user_score} | 🤖 Computer: {comp_score}")

if user_score > comp_score:
    print("🏆 Congratulations! You are the Winner!")
elif user_score < comp_score:
    print("💻 Computer Wins the Game! Better luck next time.")
else:
    print("😐 It's an Overall Draw!")
