import numpy as np

T = float(input("give me a T:"))
theta = float(input("give me a theta:"))
def convert_Farenheit(theta):
	return  5/9 * (theta - 32) - 273.15

print("T + theta = ",T + convert_Farenheit(theta))







