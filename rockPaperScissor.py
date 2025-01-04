
# Workflow of project:
#     1- Input from user(Rock, Paper, Scissor)
#     2- Computer choice (Computer will choose randomly not conditionally)
#     3- Result print
    
# Cases:
#     A - Rock
#         Rock - Rock = tie
#         Rock - Paper = Paper win
#         Rock - Scissor = Rock win
    
#     B - Paper
#         Paper - Paper = tie
#         Paper - Rock = Paper win
#         Paper - Scissor = Scissor win
    
#     C - Scissor
#         Scissor - Scissor = tie
#         Scissor - Rock = Rock win
#         Scissor - Paper = Scissor win
    

    
import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You Win")
        
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, Computer Win")
    else:
        print("Paper covers rock, You Win")
        
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, You Win")
    else:
        print("Rock smashes scissor, Computer Win")