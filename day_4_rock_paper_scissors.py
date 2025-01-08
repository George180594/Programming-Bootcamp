# rock, paper and scissors game
import random

while True:
    # user movement
    while True:
        user_choice = int(
            input(
                "What do you choose? Type 0 for rock,1 for paper and 2 for scissors\n"
            )
        )
        if user_choice == 0:
            print(user_choice, "- Rock\n")
            print(
                """
                _______
            ---'   ____)
                (_____)
                (_____)
                (____)
            ---.__(___)
                  """
            )
        elif user_choice == 1:
            print(user_choice, "- Paper\n")
            print(
                """
                _______
            ---'    ____)____
                    ______)
                    _______)
                    _______)
            ---.__________)
            """
            )

        elif user_choice == 2:
            print(user_choice, "- Scissors\n")
            print(
                """
                _______
            ---'   ____)____
                    ______)
                __________)
                 (____)
            ---.__(___)
            """
            )

        else:
            print("Something wrong, choose again")
            continue
        break

    # Computer movement
    pc_choice = random.randint(0, 2)
    if pc_choice == 0:
        print(pc_choice, "- Rock\n")
        print(
            """
                _______
            ---'   ____)
                (_____)
                (_____)
                (____)
            ---.__(___)
                  """
        )
    elif pc_choice == 1:
        print(pc_choice, "- Paper\n")
        print(
            """
                _______
            ---'    ____)____
                    ______)
                    _______)
                    _______)
            ---.__________)
            """
        )

    elif pc_choice == 2:
        print(pc_choice, "- Scissors\n")
        print(
            """
                _______
            ---'   ____)____
                    ______)
                __________)
                 (____)
            ---.__(___)
            """
        )

    if pc_choice == user_choice:
        print("DRAW - try again")
    elif pc_choice == 2 and user_choice == 1:
        print("THE MACHINE WINS")
    elif pc_choice == 1 and user_choice == 0:
        print("THE MACHINE WINS")
    elif pc_choice == 0 and user_choice == 2:
        print("THE MACHINE WINS")
    elif pc_choice == 0 and user_choice == 1:
        print("YOU WIN")
    elif pc_choice == 1 and user_choice == 2:
        print("YOU WIN")
    elif pc_choice == 2 and user_choice == 0:
        print("YOU WIN")
    continued = input("Do want to play again - Y OR N:\n")
    if continued.upper() == "S":
        continue
    elif continued.upper() == "N":
        break
