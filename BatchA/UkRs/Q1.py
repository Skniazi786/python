# Fixed a few things like adding a separate function for checking prime.. still need a few minor fixes/upgrades.
def is_prime(n):
    i = 2
    n_sqr = n ** 0.5
    status = True
    while i <= int(n_sqr):
        if n % i == 0:
            status = False
            break
        else:
            i += 1
    return status

def main():
    while True:
        num = input("Kindly provide the numeber that you want to check the prime status for: ")
        if not num:
            print("You kinda need to enter something..")
            continue
        elif num.lower() == 'q' or num.lower() == 'quit':
            print("Thank you for using this script!")
            break
        elif not num.isdigit():
            print("Apologies for the inconvenience but we need a number.")
            continue
        else:
            n = int(num)
            if n <= 1:
                print('Kindly select a number higher than 1 to check the status.')
                continue
            else:
                status = is_prime(n)
                print(f"{n} {'is a' if status else 'is not a'} prime number.")
main()
