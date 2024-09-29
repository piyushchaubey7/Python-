def add(no1,no2):
  	print("add=",no1+no2)
def sub(no1,no2):
  	print("sub=",not-no2)
def pro(no1,no2):
	print("pro=",no1*no2);
def div(no1,no2):
	print("div=",no1/no2)

choice=0
while(choice!=5):
	print("=============================select operetion==================================");
	print("1 for add");
	print("2 for sub");
	print("3 for pro");
	print("4 for div");
	print("5 for exit");

	choice=int(input("Enter operation"));
	if(choice<=4):
		no1=int(input("Enter the 1 number"));
		no2=int(input("Enter the 2 number"));
		if(choice==1):
			add(no1,no2)
		elif choice==2:
			sub(no1,no2)
		elif choice==3:
			pro(no1,no2)
		elif choice==4:
			div(no1,no2)
		elif choice==5:
			exit(0)
	else:
		print("invalid operation.......try again");



	

