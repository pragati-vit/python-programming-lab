#pragati Vilas Kate 
gr no.11810418
def max_of_two(x,y):
if x>y:
return x
return y
x=int(input())
y=int(input())
z=int(input())
a=max_of_two(z,max_of_two(x,y))
print(a)
