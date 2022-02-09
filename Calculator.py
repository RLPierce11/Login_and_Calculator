from stack import Stack
import math


def infixToPostfix(value):

	s = Stack()
	output = ""
	num = ""
	i = 0
	myinput = value

	mylen = len(myinput)

	while(i < mylen):
		if(myinput[i].isdigit() or myinput[i] == '.'):
			while(index_in_list(myinput, i) and (myinput[i].isdigit() or myinput[i] == '.') ):
				num = num + myinput[i]
				i += 1
			output = output + num + " "
			num = ""
		elif(myinput[i] == '+' or myinput[i] == '*' or myinput[i] == '/'):
			if(s.empty() or s.top() == '('):
				s.push(myinput[i])
				i += 1
			else:
				if(check_precedence(myinput[i]) > check_precedence(s.top())):
					s.push(myinput[i])
					i += 1
				else:
					output = output + s.top() + " "
					s.pop()
					s.push(myinput[i])
					i += 1
		elif(myinput[i] == '('):
			s.push('(')
			i += 1
		elif(myinput[i] == ')'):
			while(s.top() != '('):
				output = output + s.top() + " "
				s.pop()
			s.pop()
			i += 1
		elif(myinput[i] == '-'):
			if(myinput[i - 1] == '+' or myinput[i -1] == '-' or myinput[i - 1] == '*' or myinput[i - 1] == '/' or
				myinput[i - 1] == '^' or myinput[i - 1] == '(' or i == 0):
				while( index_in_list(myinput, i) and (myinput[i] == '-' or myinput[i].isdigit() or myinput[i] == '.')):
					num = num + myinput[i]
					i += 1
				output = output + num + " "
				num = ""
			else:
				if(s.empty() or s.top() == '('):
					s.push(myinput[i])
					i += 1
				else:
					if(check_precedence(myinput[i]) > check_precedence(s.top())):
						s.push(myinput[i])
						i += 1
					else:
						output = output + s.top() + " "
						s.pop()
						s.push(myinput[i])
						i += 1
		elif(myinput[i] == 'c'):
			s.push('@')
			i = i + 3
		elif(myinput[i] == 's'):
			s.push('$')
			i = i + 3
		elif(myinput[i] == 't'):
			s.push('#')
			i = i + 3
		elif(myinput[i] == 'a'):
			if(myinput[i + 1] == 'c'):
				s.push('!')
			elif(myinput[i + 1] == 'c'):
				s.push('!')
			elif(myinput[i + 1] == 'c'):
				s.push('!')
			i = i + 4

	while(not s.empty()):
		output = output + s.top() + " "
		s.pop()

	return output

def evaluate(myinput):
	num = ""
	num1 = num2 = number = i = 0
	s = Stack()
	mylen = len(myinput)

	while(i < mylen):
		if(myinput[i].isdigit() or myinput[i] == '.'):
			while(index_in_list(myinput, i) and (myinput[i].isdigit() or myinput[i] == '.')):
				num = num + myinput[i]
				i += 1
			number = float(num)
			s.push(number)
			num = ""
		elif(myinput[i] == '+'):
			num1 = s.top()
			s.pop()
			num2 = s.top()
			s.pop()
			s.push(num1 + num2)
			i += 1
		elif(myinput[i] == '-'):
			if(myinput[i + 1].isdigit() or myinput[i + 1] == '.'):
				i += 1
				while(index_in_list(myinput, i) and (myinput[i].isdigit() or myinput[i] == '.')):
					num = num + myinput[i]
					i += 1
				number = float(num) * -1
				s.push(number)
				num = ""
			else:
				num1 = s.top()
				s.pop()
				num2 = s.top()
				s.pop()
				s.push(num2 - num1)
				i += 1
		elif(myinput[i] == '/'):
			num1 = s.top()
			s.pop()
			num2 = s.top()
			s.pop()
			s.push(num2 / num1)
			i += 1
		elif(myinput[i] == '*'):
			num1 = s.top()
			s.pop()
			num2 = s.top()
			s.pop()
			s.push(num1 * num2)
			i += 1
		elif(myinput[i] == '@'):
			num1 = s.top()
			s.pop()
			s.push(math.cos(num1))
			i += 1
		elif(myinput[i] == '$'):
			num1 = s.top()
			s.pop()
			s.push(math.sin(num1))
			i += 1
		elif(myinput[i] == '#'):
			num1 = s.top()
			s.pop()
			s.push(math.tan(num1))
			i += 1
		elif(myinput[i] == '!'):
			num1 = s.top()
			s.pop()
			s.push(math.acos(num1))
			i += 1
		elif(myinput[i] == '?'):
			num1 = s.top()
			s.pop()
			s.push(math.asin(num1))
			i += 1
		elif(myinput[i] == '%'):
			num1 = s.top()
			s.pop()
			s.push(math.atan(num1))
			i += 1
		else:
			i += 1

	output = s.top()
	s.pop()
	return output






def index_in_list(a_list, index):
	if(index < len(a_list)):
		return True
	else:
		return False

def check_precedence(char):
	if(char == '+' or char == '-'):
		return 1
	elif(char == '*' or char == '/'):
		return 2
	elif(char == '^'):
		return 3
	else:
		return 4







