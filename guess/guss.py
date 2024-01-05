import random

# Create a list of animal names
animals = ["cat", "dog", "lion", "tiger"]

# Choose a random animal from the list
random_animal = random.choice(animals)

# Set maximum number of attempts
attempts = 5

# Initialize number of attempts made
attempts_made = 0

print(f"Welcome to the 'Guess the Animal' game! You have {attempts} attempts to guess the animal.")

while attempts_made < attempts:
    guess = input("Guess the animal: ").lower()

    if guess == random_animal:
        print(f"Congratulations! You guessed the animal - {random_animal}.")
        break
    else:
        attempts_made += 1
        print(f"Sorry, incorrect guess. You have {attempts - attempts_made} attempts remaining.")

if attempts_made == attempts:
    print(f"Sorry, you have run out of attempts. The correct animal was {random_animal}.")