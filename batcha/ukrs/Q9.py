def main():
    while True:
        user_input = input(">> Kindly enter the list of items you want to remove duplicates from: ").strip()
        if not user_input:
            print(">> ERROR: BLANK INPUT IS NOT ALLOWED.")
            continue
        ui_list = user_input.split()
        if len(ui_list) < 2:
            print(">> ERROR: KINDLY ENTER MORE THAN 1 NUMBER.")
            continue
        new_list = []
        for item in ui_list:
            if item not in new_list:
                new_list.append(item)
        print(f">>The list: {ui_list}\n>> List without duplicates: {new_list}")
        break
main()