import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''




flag=1


while(flag):
    your_sign = int(input("Enter 0 for rock, 1 for paper, 2 for scissors\n" "Enter 3 to stop Game\n"))
    if(your_sign==3):
        print("Game Over")
        break
    computer_sign = random.randint(0,2)
    rps_list = [rock, paper, scissors]
    print("YOU CHOSE: \n")  
    print(rps_list[your_sign])
    print("\nCOMPUTER CHOSE\n")
    print(rps_list[computer_sign])

    if your_sign == computer_sign:
        print("Draw! Live to fight another day!!!!")
    elif rps_list[your_sign - 2] == rps_list[computer_sign]:
        print("You lose. The machines took over the world!!!")
    elif rps_list[computer_sign - 2] == rps_list[your_sign]:
        print("You win!!!! Great success!!!! Terminator averted!!!")