def main():
    while True:
        user_input = input("Kindly enter the sentence you want to check the repetitions for: ")
        if not user_input.strip():
            print(">> ERROR: BLANK INPUT IS NOT ALLOWED.")
            continue
        sentence = user_input.split()
        if len(sentence) < 2:
            print(">> ERROR: KINDLY ENTER MORE THAN 1 WORD.")
            continue
        word_count = {}
        for word in sentence:
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1
        for i,(word,count) in enumerate(word_count.items()):
            print(f"{i+1}) {word}: {count}")
        break
main()