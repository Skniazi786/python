# word = input("Kindly provide the numero that you want to check the prime status for: ")

n = 3
def main():
    i = 2
    while i <= n:
        print(n%i)
        if n <= 0:
            print("Kindly provide a valid number!")
        elif n % i == 0:
            print("It is not a prime number.")
            break
        elif n % i == 0 and n != i:
            print("It is not a prime number.")
            break
        else:
            print("It is a prime number.")
            i += 1
main()