import random

def guess_the_number():
    print("\n👑 Welcome to the *Bougie Number Guessing Game*! 👑")
    print("✨ I’ve picked a number between 1 and 100. Your mission, babe, is to guess it.")
    print("Think fast, think smart, and don’t let this number humble you. 💅")

    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0

    # Fun sassy responses
    too_low_responses = [
        "📉 Umm, that's too low, bestie. Aim higher, we’re not in the bargain aisle.",
        "👀 This isn't a clearance sale. Try a bigger number, darling.",
        "🤔 Sweetheart, that guess is giving 'I don’t trust my gut.' Trust it more!"
    ]
    too_high_responses = [
        "📈 Whoa, slow down, queen. That number’s too high—it’s giving unrealistic standards.",
        "🛑 Babe, you’re reaching for the stars, but I need you in reality. Try lower.",
        "😅 Oh no, not that high! This isn’t your rent."
    ]

    # Game loop
    while True:
        try:
            # Get player input
            guess = int(input("\n🎤 Drop your guess: "))
            attempts += 1

            if guess < secret_number:
                print(random.choice(too_low_responses))
            elif guess > secret_number:
                print(random.choice(too_high_responses))
            else:
                print(f"\n🎉 Yasss, queen! You guessed it! The number was {secret_number}.")
                print(f"💎 And you only took {attempts} attempt{'s' if attempts > 1 else ''}. Iconic behavior.")
                print("✨ Pop some champagne, because you’re THAT girl. 🥂")
                break
        except ValueError:
            print("⚠️ Babe, I said a *number*. This isn’t the time for freestyle guessing.")

    print("\n💌 Thanks for playing, gorgeous. Come back for more fun (and maybe a skincare tip or two).")
    
# Run the game
if __name__ == "__main__":
    guess_the_number()
