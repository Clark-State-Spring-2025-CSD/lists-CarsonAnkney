#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random


theList1 = []

theList2 = []
    
for i in range(10):
    theList1.append(random.randint(1, 50))

for i in range(10):
    theList2.append(random.randint(1, 50))
    
player_one_wins = 0
player_two_wins = 0

for num1, num2 in zip(theList1, theList2):
    if num1 > num2:
        player_one_wins += 1
    elif num2 > num1:
        player_two_wins += 1



print(f"player one = {theList1}")

print(f"player two = {theList2}")

print(f"player one won {player_one_wins} times")

print(f"player two won {player_two_wins} times")

biggest_number = max(theList1)

biggest_number2 = max(theList2)

index_of_biggest_number = theList1.index(biggest_number)

index_of_biggest_number2 = theList2.index(biggest_number2)

print(f"player one's highest number is {biggest_number} at index {index_of_biggest_number}")

print(f"player two's highest number is {biggest_number2} at index {index_of_biggest_number2}")

lowest_number = min(theList1)

index_of_lowest_number = theList1.index(lowest_number)

lowest_number2 = min(theList2)

index_of_lowest_number2 = theList2.index(lowest_number2)

print(f"player one's lowest number is {lowest_number} at index {index_of_lowest_number}")

print(f"player two's lowest number is {lowest_number2} at index {index_of_lowest_number2}")