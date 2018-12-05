#pragati Vilas Kate
gr. no. 11810418
n terms=10
#n terms=int(input("How many terms?"))
#first two terms
n1=0
n2=1
count=0
   if n terms <=0:
     print("please enter a positive integer")
   elif n terms==1:
     print("fibonacci sequence upto",n terms,":")
     print(n1)
   else:
     print("fibonacci sequence upto",n terms,":")
     while count<n terms:
     print(n1,end=',')
     nth=n1+n2
     #update values
     n1=n2
     n2=nth
     count+=1
