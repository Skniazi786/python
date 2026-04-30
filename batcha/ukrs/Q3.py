import sys
MODES = ['add','subtract','divide','multiply','+','-','/','*']
def check_input(txt):
    words = txt.split()
    if not words:
        return {'status': False,'msg':'!! Kindly type something for the calc to work.'}
    elif words[0].lower() in ['q','quit']:
        sys.exit()
    elif len(words) != 2:
        return {'status': False,'msg':'!! Kindly only provide two numbers for the Calc to work.'}
    elif not words[0].isdigit() or not words[1].isdigit():
        return {'status': False, 'msg':'!! Kindly make sure that both inputs are numbers.'}
    else:
        return {'status': True, 'values': words}
def calc(nums,mode):
    n1, n2 = int(nums[0]), int(nums[1])
    if mode in ['add','+']: return f">> {n1} + {n2} = {n1+n2}"
    elif mode in ['subtract','-']: return f">> {n1} - {n2} = {n1-n2}"
    elif mode in ['divide','/']: 
    # Seriously.. division freaking sucks in mathematics.. my script crashed when i tried dividing by 0 lola
        if n2 == 0: return "YOU FUCKING RETARD!"
        return f">> {n1} / {n2} = {n1/n2:.2f}"    
    elif mode in ['multiply','*']: 
        return f">> {n1} X {n2} = {n1*n2}"
def main():
    user_input = input("~ Welcome to the Usama's Calculator! Kindly provide the two numbers: ")
    check_nums = check_input(user_input)
    if not check_nums['status']:
        print(check_nums['msg'])
    else:
        while True:
            mode = input(">> What would you like to do? [add +, subtract -, divide /, multiply *]: ")
            nums = check_nums['values']
            # just remembered this pretty great alternative to and or method from mode in MODES lmao..
            if mode.lower() in ['q','quit']:
                sys.exit()
            elif mode in MODES:
                print(calc(nums, mode))
                break
            else:
                print("Invalid choice. Please try again!")
        
main()