n = int(input ('please enter the part of the sequence you are trying to find'))
r_raw1 = int(input ('please enter the first number in the sequence'))
r_raw2 = int(input ('please enter the second number in the sequence'))
a1 = int(input ('please enter the first number in the sequence again'))
r_solved = r_raw2 / r_raw1
step_1 = a1 * r_solved**(n - 1)
print (step_1)