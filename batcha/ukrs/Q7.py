def main():
    user_input = input(">> Kindly enter a list of number you want to reverse: ")
    if not user_input.strip():
        print(">> ERROR: BLANK INPUT IS NOT ALLOWED.")
    elif user_input.strip().lower() in ['q','quit']:
        print(">> ERROR: PROGRAM TERMINATED")
    elif len(user_input.split()) <= 1:
        print(">> ERROR: KINDLY ENTER MORE THAN ONE ITEM.")
    else:
        ui_list = user_input.split()
        reversed_list = []
        for i in range(len(ui_list)-1,-1,-1):
            reversed_list.append(list[i])
        print(f"The reverse for the {list} is {reversed_list}")
main()