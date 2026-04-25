# Finally fixed a shitton of things.. Just need to transfer some functionality to other funcs.. or shit..
def main():
    while True:
        num = input("Kindly provide the numero that you want to check the prime status for: ")
        if not num:
            print("Not a fucking word huh.. Alright then.. Keep your secrets..")
            continue
        elif num.lower() == 'q' or num.lower() == 'quit':
            print("Thank you for using this script! nigga!")
            break
        elif not num.isdigit():
            print("We need a number, you dipshit..")
            continue
        else:
            n = int(num)
            if n <= 1:
                print('Kindly select a number higher than 1 to check the status.')
                continue
            else:
                i = 2
                n_sqr = n ** 0.5
                status = True
                while i <= int(n_sqr):
                    if n % i == 0:
                        status = False
                        break
                    else:
                        i += 1
                print(f"{n} {'is a' if status else 'is not a'} prime number.")
main()
