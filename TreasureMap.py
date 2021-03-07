row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
choice = input("Where do you wanna hide your treasure")
choice_list = list(choice)
column = int(choice_list[0])-1
row = int(choice_list[1])-1
map[row][column] = "X"
print(f"{row1}\n{row2}\n{row3}")
