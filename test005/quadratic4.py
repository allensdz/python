#quadratic4.py
#计算二次方程的实数根的程序
#此程序在没有实根的情况下报错
import math
def main():
	print("This program find the real solutions to a quadratic\n")
	a,b,c=eval(input("Please enter the coefficients (a,b,c):"))
	delta=b*b-4*a*c
	if a==0:
		x=-b/c
		print("\nThere is an solution",x)
	elif delta<0:
		print("\nThe equation has no real roots!")
	elif delta==0:
		x=-b/(2*a)
		print("\nThere is a double root at",x)
	else:	
		disc=math.sqrt(delta)
		root1=(-b+delta)/(2*a)
		root2=(-b-delta)/(2*a)
		print("\nThe solutions are:",root1,root2)	
main()		
