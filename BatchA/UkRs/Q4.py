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
            print(f"Total count of the {num} is {len(num)}.")
            break
main()