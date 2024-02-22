import random
print("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.")
img=["Rock","Paper","Scissors"]
a=int(input())
print(img[a])
b=random.randint(0,2)
print(img[b])
result=[["draw","loose","win"],["win","draw","loose"],["loose","win","draw"]]
print(f"You {result[a][b]}")
