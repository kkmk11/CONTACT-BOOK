print("\t\t\t****** CONTACT BOOK ******")
l1=[]
flag=0
while(True):
    n=int(input("\n\n\n1)Save a contact\n2)Delete a contact\n3)Search a contact\n4)display all contacts\n5)Exit\n\nChoose a option from the above : "))
    if(n==1):
        name=input("Name : ")
        number=input("Mobile Number : ")
        l1.append([name,number])
    if(n==2):
        x=input("Search by Name or Contact no. : ")
        for i in l1:
            for j in i:
                if(j==x):
                    l1.remove(i)
                    flag=1
                    break
        if(flag==1):
            print("Deletion Done")
        else:
            if(x.isalpha()):
                print("No such Name in your Contact Book")
            else:
                print("No such Number in your Contact Book")   
    if(n==3):
        flag1=0
        flag2=0
        x=input("Search by Name or Contact no. : ")
        if(x.isalpha()):
            for i in range(len(l1)):
                if(l1[i][0]==x):
                    flag1=1
                    break
            if(flag1==1):
                print("Contact No. : ",l1[i][1])
            else:
                print("No such Name in your Contact Book")
        if(x.isdigit()):
            for i in range(len(l1)):
                if(l1[i][1]==x):
                    flag2=1
                    break
            if(flag2==1):
                print("Name : ",l1[i][0])
            else:
                print("No such Number in your Contact Book") 
    if(n==4):
        print("\nALL CONTACT NUMBERS :")
        l1.sort(key=lambda x:x[0])
        for i in range(len(l1)):
            print(l1[i][0]," : ",l1[i][1])
    if(n==5):
        exit(0)
                



        







