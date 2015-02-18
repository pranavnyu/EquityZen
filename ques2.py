def _str():
    #enter the desired string
	str1 = raw_input("enter the string: ");
	str1 = str1.lower()
	return str1


def _check_string(str1,str2):
    #check all the alphabets in string 1
	sol = ""
	for letter in str2:
		if letter not in str1:
			sol = sol + letter
	return sol	



def main():
    #calling main fucntion
	str2 = "abcdefghijklmnopqrstuvwxyz"
	str1 = _str()
	sol = _check_string(str1, str2)
	print sol

if __name__ == '__main__':
	main()