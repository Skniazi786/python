def is_prime(n):
    i = 2
    nsqr = n ** 0.5
    status = True
    while i <= int(nsqr):
        if n % i == 0:
            status = False
            break
        else:
            i += 1
    return status

def main():
    while True:
        n = input("Kindly provide the number you want to check the prime numbers before: ")
        if not n:
            print("You did not entered anything. Kindly enter a number.")
        elif n.lower() == 'q' or n.lower() == 'quit':
            print("Okay, babye!")
            break
        elif not n.isdigit():
            print("Kindly enter a number.")
        elif int(n) == 2 or int(n) == 1:
            print(f"You really can't tell if {n} is a prime number or not??")
        else:
            num = int(n)
            list = []
            for i in range(2,num):
                if is_prime(i):
                    list.append(i)
            print(f"{list}")

main()