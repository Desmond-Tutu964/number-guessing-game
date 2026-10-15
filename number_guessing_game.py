import random

score = 0
streak = 0
playing = True

while playing:
    print("choose your difficulty:")
    print("1. Easy (1-20)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        number = random.randint(1,20)
        points = 10
        max_attempts = 7
    elif choice == "2":
        number = random.randint(1,100)
        points = 20
        max_attempts = 8
    elif choice == "3":
        number = random.randint(1,500)
        points = 50
        max_attempts = 10
    else:
        print("Invalid choice! Starting at Easy level.")
        number = random.randint(1,20)
        points = 10
        max_attempts = 7

    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        attempts += 1

        if guess == number:
            print("Correct! You guessed the number!")
            print("you got it in", attempts, "attempts!")
        

            score += points
            streak += 1
            
            print("You earned", points, "points!")
            print("Your total score is", score)
            print("winning streak:", streak)

            break
        elif guess > number:
            print("Too high!")
            if guess - number <= 5:
                print("You're very close!")
        else:
            print("Too low!")
            if guess - number <= 5:
                print("You're very close!")

    if guess != number and attempts == max_attempts:
        print("Game over! You've used all", max_attempts, "attempts.")
        print("The correct number was", number)
        streak = 0
        print("winning streak reset to 0!")
        

    again = input("Do you want to play again? (yes/no): ")

    if again.lower() == "yes":
        continue

    print("Game paused.")

    while True:
        command = input("Type 'start' to play again, or 'exit' to quit: ")

        if command.lower() == "start":
            break
        elif command.lower() == "exit":
            print("Thanks for playing!")
            print("your final score was:", score)
            print("Your final winning streak was:", streak)
            playing = False
            break
        else:
            print("Please type start or exit.")
