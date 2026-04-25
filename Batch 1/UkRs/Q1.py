n = int(input("Kindly provide the numero that you want to check the prime status for: "))

def main():
    i = 2
    status = 'is a'
    while i < n:
        if n % i == 0:
            status = 'is not a'
            break
        else:
            i += 1
    print(f"{n} {status} prime number.")
main()