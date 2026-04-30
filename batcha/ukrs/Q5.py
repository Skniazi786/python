def main():
    while True:
        user_input = input(">> Kindly enter the word you want to check palindrome status for: ")
        # accidently entered "   " and it gave me a palindrome for that.. so there was some issue with my code.. had to look it up.. but the strip() just removes all the space so worked perfeclty!
        if not user_input.strip():
            print(">> ERROR: Kindly enter a word.")
            continue
        # for the world of me, i could not think of a way to check if the user had entered a second word.. tried multiple times but they all give me an error.. so had to chatgpt this part.. forgive me brother!
        elif " " in user_input.strip():
            print("Kindly only enter a single word.")
            continue
        else:
            word = user_input.lower()
            n = 0
            for i in word:
                n += 1
            reversed_letters = []
            for i in range(n,0,-1):
                reversed_letters.append(word[i-1])
            reversed_word = "".join(reversed_letters)
            print(f">> The reverse for {word} is [{reversed_word}] so {'It is a' if word == reversed_word else 'It is not a'} palindrome")
            break
main()