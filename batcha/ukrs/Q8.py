def f_tracker(n):
    a,b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def main():
    user_input = input(">> Kindly enter the word you want to check the FIBONACCI status of: ").strip()
    if not user_input:
        print(">> ERROR: BLANK INPUT IS NOT ALLOWED.")
        return
    if " " in user_input:
        print(">> ERROR: KINDLY ONLY ENTER A SINGLE NUMBER")
        return
    if not user_input.isdigit():
        print(">> ERROR: KINDLY ONLY ENTER A POSITIVE NUMBER.")
        return
    n = int(user_input)
    if n >= 50:
        print(">> ERROR: CALM DOWN MAN. ONLY ENTER A NUMBER LOWER THAN 50.")
        return
    nums = f_tracker(n)
    print(f"The Fibonacci sequence for [{user_input}] is :{nums}")

main()