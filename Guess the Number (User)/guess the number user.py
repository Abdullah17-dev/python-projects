def computer_guesses_game():
    print("Think of a number between 1 and 100 and I'll try to guess it.")
    input("Press Enter when you're ready...")  # Just to let the user start

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is {guess}")

        feedback = input("Is my guess too high (H), too low (L), or correct (C)? ").strip().upper()

        if feedback == "C":
            print(f"I guessed your number {guess} in {attempts} attempts!")
            break
        elif feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
        else:
            print("Please enter H, L, or C.")

# Call the function
computer_guesses_game()