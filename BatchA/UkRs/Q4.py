import sys
def main():
    while True:
        num = input("~ Kindly enter the digits you want to check length of: ")
        if not num:
            print(">> ERROR: BLANK INPUT.")
            continue
        elif num in ['q','quit']:
            sys.exit()
        elif not num.isdigit():
            print(">> ERROR: ALPHABETS SPOTTED.")
            continue
        else:
            n = 0
            for i in num:
                n += 1
            print(f"Total count of the {num} is {n}.")
            break
main()