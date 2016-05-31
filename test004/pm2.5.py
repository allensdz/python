#pm2.5.py
#空气质量提醒
def main():
	PM=eval(input("What is today's PM2.5?"))
	if PM>75:
		print("Unheathly.Be careful!")
	if PM<35:
		print("Good.Go running")
main()		
