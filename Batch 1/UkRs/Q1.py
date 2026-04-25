n = int(input("Kindly provide the numero that you want to check the prime status for: "))

def main():
    if n <= 1:
        print('Kindly select a number higher than 1 to check the status.')
    else:
        i = 2
        status = True
        while i < n:
            if n % i == 0:
                status = False
                break
            else:
                i += 1
        print(f"{n} {'is a' if status else 'is not a'} prime number.")
main()