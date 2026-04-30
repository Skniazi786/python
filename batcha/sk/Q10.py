from func import cp
	# Importing cp function from my func.py file which only gives me good colouring for terminal.

def ret_list_from_string(a):
	b={}
	for i in a.split():
		if i in b:
			b[i]+=1
		else:
			b[i]=1
	else:
		return b
def main():
	while True:
		inp = input(cp("Please write some text I will give you repeated words :","b","w",inpu=True))
		print(cp(flu=True),end="")
		if inp.strip()=="":
			print(cp("This is empty space! Try again","bk","y"))
			continue
		elif inp.isdigit() == True:
			print(cp("Please type words not numbers","bk","y"))
			continue
		elif len(inp.split())<1:
			print(cp(f"Can't find repeated words for a small sentence such as [{inp}]","cy","r"))
			continue
		else:
			print(cp(f"Your string was {inp} and repeated words/numbers are {ret_list_from_string(inp)}.","y","g"))
			break
main()
