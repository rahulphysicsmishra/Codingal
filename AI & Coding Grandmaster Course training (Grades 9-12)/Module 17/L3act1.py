def a_and_b(a, b):

	if a==1:
		prob_student = 0.3
		if b ==1:
			prob_dining = 0.75
		else:
			prob_dining = 0.25
		print("Probability of a given b:", prob_dining)

	if a==2:
		prob_student=0.7
		if b==1:
			prob_dining = 0.6
		else:
			prob_dining = 0.4
		print("Probability of a given b:", prob_dining)
	
	prob_a_and_b = prob_student*prob_dining
	return round(prob_a_and_b, 3)

print("Check the probability of any event occuring. First enter your choices.")

print("Is the student a Freshman? \n 1. Yes \n 2. No")
a = int(input("Enter your choice (1/2): "))

print("Is student eating in dining hall? \n 1. Yes \n 2. No")
b = int(input("Enter your choice (1/2): "))

print("Here is the probability of both the events occuring :", a_and_b(a, b))
