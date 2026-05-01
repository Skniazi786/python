def main():
    error = False
    user_input = input(">> Kindly enter a list of number you want to check the max of: ")
    if not user_input.strip():
        print(">> ERROR: BLANK INPUT IS NOT ALLOWED.")
        error = True
    elif user_input.strip().lower() in ['q','quit']:
        print(">> ERROR: PROGRAM TERMINATED")
        error = True
    elif len(user_input.split()) <= 1:
        print(">> ERROR: KINDLY ENTER MORE THAN ONE NUMBER.")
        error = True
    else:
        nums = user_input.split()
        # Holy s--.. kept thinking about how could i fix this max_num = 0 issue and chatgpt just straight up give a simple as hell answer..
        max_num = int(nums[0])
        for n in nums:
            if not (n.isdigit() or (n.startswith('-') and n[1:].isdigit()) ):
                print(">> ERROR: ONLY NUMBERS ARE ALLOWED.")
                error = True
                break
            else:
                num = int(n)
                if num > max_num:
                    max_num = num
    if not error: 
        print(f">> The biggest number in {nums} is {max_num}")
main()