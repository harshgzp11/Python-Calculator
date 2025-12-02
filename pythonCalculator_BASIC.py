#Building a BASIC Calculator using PYTHON

n1=int(input("Enter the first number: "))
n2=input("Enter the operator: ")
n3=int(input("Enter the second number: "))

if n2=="+":
    print(n1+n3)
elif n2=="-":
    print(n1-n3)
elif n2=="*":
    print(n1*n3)
elif n2=="/":
    if n3 == 0:
        print("NOT DEFINED")
    else:
        print(n1/n3)
else:
    print("INVALID OPERATION")