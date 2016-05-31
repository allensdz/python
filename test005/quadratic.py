#quadratic.py
#计算二次方程的实数根的程序
#此程序在没有实根的情况下报错
import math
def main():
	print("This program find the real solutions to a quadratic\n")
	a,b,c=eval(input("Please enter the coefficients (a,b,c):"))
	delta=b*b-4*a*c
	if delta>=0:
		delta=math.sqrt(delta)
		root1=(-b+delta)/(2*a)
		root2=(-b-delta)/(2*a)
		print("\nThe solutions are:",root1,root2)
main()		
