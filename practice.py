#1)print first 10 even numbers in a list using list comprehension
"""list1=[x for x in range(11) if x%2==0 ]
print(list1)"""

#2)print n number of even numbers which are dividible by 5 and 10 using list comprehension:
"""x=int(input("please enter the number of elements you want"))
list1=[i for i in range(x) if i%5==0 and i%10==0]
print(list1)"""

#3)create a dictionary with names and roll number using custom errors
"""students={1:"Nagabasha:o220518",2:"Ravikiran:o220519",3:"Jaswanth:o220519",4:"RajendraReddy:o220520"}
try:
	x=int(input("enter the roll num:"))
	if x==1:
		print(students[1])
	elif x==2:
		print(students[2])
	elif x==3:
		print(students[3])
	elif x==4:
		print(students[4])
except Exception as E:
	print("please enter only int values:::",E )"""
	
#4)create a string using swapcase method:
"""string1="nAgAbAshA"
print(string1.swapcase())"""

#5)python program to interchange last and first element in a list:
#method1:using index 
"""list1=[1,2,3,4,5]
x=list1[0]
y=list1[-1]
list1[0],list1[-1]=y,x
print(list1)"""
#method2:using index
"""list1=[1,2,3,4,5]
list1[0],list1[-1]=list1[-1],list1[0]
print(list1)"""
#method3:using list methods
"""list1=[1,2,3,4,5]
last=list1.pop()
first=list1.pop(0)
print(list1)
list1.insert(0,last)
list1.insert(4,first)
print(list1)"""


#python program to interchange last and first element in a string:
#method1:using index and slicing
"""string="shreeshanth"
new_string=string[-1]+string[1:-1]+string[0]
print(new_string)"""

#swap two elements in a list by giving the positions
"""pos1=int(input("enter the position:"))
pos2=int(input("enter the position:"))
list1=[1,2,3,4,5]
print(list1)
list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
print(list1)"""

#plotting a y=x^2 graph
"""import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y,label="y=x^2",color="red")
plt.title("Y=X^2 GRAPH")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.grid(True)
#plt.savefig("y=x^2_graph.png")
plt.legend()
plt.show()"""

"""#figure-object:
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,100)
#plotting graph in bottom-left
y=x**3
fig=plt.figure(figsize=(5,5,))
axes_bottomleft=fig.add_axes([0.1,0.1,0.3,0.3])#lbwh
axes_bottomleft.plot(x,y,label="y=x^3",color="red")
plt.title("plotting y=x^3 Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
#plt.savefig("graph-1.png")

#plotting graph in top-left
y=x**2
axes_topleft=fig.add_axes([0.1,0.6,0.3,0.3])#lbwh
axes_topleft.plot(x,y,label="y=x^2",color="blue")
plt.title("plotting y=x^2 Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
#plotting graph in top-right
y=x
axes_topright=fig.add_axes([0.5,0.6,0.3,0.3])#lbwh
axes_topright.plot(x,y,label="y=x",color="purple")
plt.title("plotting y=x Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
#plotting graph in bottom-right
m=3
y=m*x
axes_bottomright=fig.add_axes([0.5,0.1,0.3,0.3])#lbwh
axes_bottomright.plot(x,y,label="y=mx",color="cyan")
plt.title("plotting y=mx Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()

plt.show()"""

#sub-plots
"""import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,100)
fig,axes=plt.subplots(2,2)
y=x**2
axes[0,0].plot(x,y,label="y=x^2",color="red")
y=x**3
axes[0,1].plot(x,y,label="y=x^3",color="yellow")
m=2
y=m*x
axes[1,0].plot(x,y,label="y=mx",color="purple")
y=x
axes[1,1].plot(x,y,label="y=x",color="pink")

plt.xlabel("x-axis")
fig.legend()
plt.show()"""

#plotting a Graph
"""import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,10)
y=x**2
plt.style.use("dark_background")
plt.plot(x,y,label="y=x**2",color="red",linestyle="-",marker="D",markersize=7,markerfacecolor="blue",zorder=1)
y=x**3
plt.plot(x,y,label="y=x**3",color="pink",linestyle="-",marker="X",markersize=7,markerfacecolor="yellow",zorder=2)
plt.title("Plotting a y=x**2 Graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.xlim(-10,10)
plt.ylim(-100,100)
plt.legend()
#plt.savefig("Graph1.png")
plt.show()"""

#plotting a figure-object Graph:
"""import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,10)

fig=plt.figure(figsize=(6,4))
plt.style.use("dark_background")
#plotting a graph in topleft 
y=x**2
axes_topleft=fig.add_axes([0.1,0.6,0.3,0.3])#lbwh
axes_topleft.plot(x,y,label="y=x**2",color="Blue",linestyle="-",marker="d",markersize=5,markerfacecolor="Red")
plt.title("y=x**2")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()"""

#plotting a graph in topright
"""y=x**3
axes_topright=fig.add_axes([0.5,0.6,0.3,0.3])#lbwh
axes_topright.plot(x,y,label="y=x**3",color="red",linestyle="dotted",marker="o",markersize=5,markerfacecolor="blue")
plt.title("y=x**3")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()

#plotting a graph in bottomright
y=x
axes_topright=fig.add_axes([0.5,0.1,0.3,0.3])#lbwh
axes_topright.plot(x,y,label="y=x",color="green",linestyle="",marker="x",markersize=5,markerfacecolor="cyan")
plt.title("y=x")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()
#plotting a graph in bottomleft
m=3
y=m*x
axes_topright=fig.add_axes([0.1,0.1,0.3,0.3])#lbwh
axes_topright.plot(x,y,label="y=mx",color="purple",linestyle="",marker=".",markersize=5,markerfacecolor="yellow")
plt.title("y=mx")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()

plt.show()"""

#subplots
"""import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,10)
y=x**2
fig,axes=plt.subplots(2,2)#2rows,2coloums
axes[0,0].plot(x,y,color="red",linestyle="",marker="s")
y=x**3
axes[0,1].plot(x,y,color="yellow",linestyle="-",marker="o")
y=x
axes[1,0].plot(x,y,color="pink",linestyle="dotted",marker="x")
m=3
y=m*x
axes[1,1].plot(x,y,color="blue",linestyle="-.",marker="d")

plt.show()"""

#bargraohs
"""import matplotlib.pyplot as plt
students=["sai","sasi","surya","sukumar","siva"]
marks=[90,80,70,90,95]
plt.style.use("dark_background")
plt.bar(students,marks,color=["blue","yellow","#00ff00","#ff0000","purple"],edgecolor="cyan")
plt.title("Students marks graph")
plt.xlabel("Students")
plt.ylabel("Ranks")
plt.show()"""

#bargraphs-horizontal
"""import matplotlib.pyplot as plt
students=["sai","sasi","surya","sukumar","siva"]
marks=[90,80,70,90,95]
plt.style.use("ggplot")
plt.barh(students,marks,color=["blue","yellow","#00ff00","#ff0000","purple"],edgecolor="cyan")
plt.title("students marks graph")
plt.xlabel("marks")
plt.ylabel("students")
plt.show()"""

#stacked_bar-graphs:
"""import matplotlib.pyplot as plt
students=["sai","sasi","surya","sukumar","siva"]
marks_externals=[40,50,60,38,43]
marks_internals=[30,40,35,29,60]
plt.bar(students,marks_externals,label="externals")
plt.bar(students,marks_internals,bottom=marks_externals,label="internals")
plt.title("stacked bar-graps")
plt.xlabel("students")
plt.ylabel("marks")
plt.legend()
plt.show()"""



#graphs
"""import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,10)
y=x**2
plt.plot(x,y,label="y=X^2",color="red",)
y=x**3
plt.plot(x,y,label="y=X^3",color="blue",)
plt.grid(True)
plt.legend()
plt.show()"""

#Decimal to Binary conversion:
"""x=10
print(bin(x))
print(bin(25))
print(bin(100))"""


#Binary to Decimal conversion:
"""print(0b1010)#10       #we have to mention "0b" in front of binary number
print(0b11001)#25
print(0b1100100)#100"""

#Decimal to Octa conversion:we use oct() built-in method
"""print(oct(10))
print(oct(25))
print(oct(100))"""

#Octa to Decimal conversion:
"""print(0o12)
print(0o31)
print(0o144)"""


#Decimal to Hexa-Decimal conversion:we use hex() built-in method
"""print(hex(10))
print(hex(25))
print(hex(100))"""

#hexa-decimal to decimal conversion:
"""print(0xa)
print(0x19)
print(0x64)"""


#octal to binary:  [octal------> decimal------>binary]
"""x=0o31
print(bin(x))"""

#binary to hexa-decimal:  [binary---->decimal------>hexa-decimal]
"""x=0b1100100
print(hex(x))"""

#hexa-decimal to octal:   [hexa-decimal------>decimal---->octal]
"""x=0x19
print(oct(x))"""

#OOPS CONCEPT IN PYTHON
#practice-1:creating base class:
"""class Employee:
	name="Shiva"
	salary=60000
	company="Tata-Motors"
	def show_info(self):
		print(f"Name:{self.name}\nSalary:{self.salary}\nCompany:{self.company}")
emp1=Employee()
print(emp1.name,emp1.salary,emp1.company)
emp1.show_info()"""

#practice-2:creating base class with constructors:
"""class Employee:
	def __init__(self,name,salary,company):
		self.name=name
		self.salary=salary
		self.company=company
	def show_info(self):
		print(f"Your name is {self.name} and your salary is {self.salary} working in {self.company} company.")
emp1=Employee("Rajesh",70000,"Infosys")
print(emp1.name,emp1.salary,emp1.company)
emp1.show_info()"""

#practice-3":constructor types:02)parameterized
"""print("01)Parameterized-Constructors")
class Employee:
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	def show_info(self):
		print(f"My name is {self.name} and i earn {self.salary} per month")
emp1=Employee("Rahul",50000,)
print(emp1.name,emp1.salary)
emp1.show_info()"""

"""print("02)Default-Constructors")
class Employee:
	def __init__(self):
		print("My name is rahul and i earn 70000 per month/-")
emp1=Employee()"""

#practice-4:Decorators (without parameters)
"""def information(original_function):
	def show_info():
		print("Good Morning !!")
		original_function()
		print("Thank you !!")
	return show_info
@information
def hello_fun():
	print("Hello world")
hello_fun()"""
#practice-5:Decorators(with parameters)
"""def information(original_fun):
	def show_info(*args,**kwargs):
		print("You are using addition_function now")
		original_fun(*args,**kwargs)
		print("Great ! You have successfully used the addition_function !!")
	return show_info
@information
def add(x,y):
	print(x+y)
add(100,100)
#information(add)(100,100)"""
#practice-6:acess specifiers/modifiers:(public)
"""class Employee:
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	def show_info(self):
		print(f"My name is {self.name} and i earn {self.salary} per month")
emp1=Employee("Rahul",50000,)
print(emp1.name,emp1.salary)
emp1.show_info()"""	

#practice-7:acess specifiers/modifiers:(private)
"""class Employee:
	def __init__(self,name,salary):
		self.__name=name
		self.__salary=salary
	def __show_info(self):
		print(f"My name is {self.__name} and i earn {self.__salary} per month")
emp1=Employee("Rahul",50000,)
#print(emp1.__name,emp1.__salary)
#emp1.__show_info()

print(emp1._Employee__name)
print(emp1._Employee__salary)
emp1._Employee__show_info()"""

#practice-8:acess specifiers/modifiers:(protected)
"""class Employee:
	def __init__(self,name,salary):
		self._name=name
		self._salary=salary
	def _show_info(self):
		print(f"My name is {self._name} and i earn {self._salary} per month")
emp1=Employee("Rahul",50000,)
print(emp1._name,emp1._salary)
emp1._show_info()"""

#print biggest prime factor:

"""x=int(input("enter any number:"))
list1=[]
list2=[]
for i in range(1,x+1):
	if x%i==0:
		list1.append(i)

def prime(y):
	for j in y:
		c=0
		for k in range(1,j+1):
			l=k
			if j%k==0:
				c+=1
			else:
				pass	
		if c==2:
			list2.append(l)	
prime(list1)
print(f"factors of {x} is {list1}")
print(f"prime factors of {x} is {list2}")
print(f"Biggest prime factor is {max(list2)}")"""

#swap the smallest and biggest numbers in a list:
"""
list1=[0,10000,100,200,300,400,900]
big=max(list1)
small=min(list1)
index_big=list1.index(big)
index_small=list1.index(small)
temp=list1[index_big]
list1[index_big]=list1[index_small]
list1[index_small]=temp
print(list1)
"""
#program to swap first and last numbers in a list
"""
list1=[3,1,2,3,4,5,9]
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(list1)
"""

#python program to find length of a list without using built-in functions:
"""
list1=[1,2,3,4,5]
count=0
for i in list1:
	count+=1
print(f"The length of the list is: {count}")
"""

#program to find the given number is palindrome or not:
"""
x=int(input("enter any number:"))
last=0
reverse=0
temp=x
while(x>0):
	last=x%10
	reverse=reverse*10+last
	x=x//10
if temp==reverse:
	print(f"{temp} is a palindrome number")
else:
	print(f"{temp} is not a palindrome number")
"""

#program to find the fabinocci series upto given range:
"""
x=int(input("enter the range:"))
x1=0
y1=1
sum=0
for i in range(1,x+1):
	print(sum)
	x1=y1
	y1=sum
	sum=x1+y1
"""

#take range from the user and check if it is divisible by 5 or not if yes add all the digits in that number:
"""
x=int(input("enter the lower range:"))
y=int(input("enter the upper range:"))
last=0
temp=0
sum=0
for i in range(x,y+1):
	sum=0
	if i%5==0:
		temp=i
		while(i>0):
			last=i%10
			sum+=last
			i=i//10
		print(f"num div by 5 is {temp} and sum of its digits is {sum}")
"""

#if the given num is palindrome print the sum of the digits of that numver:
"""
x=int(input("enter any number:"))
last=0
reverse=0
temp=x
last1=0
sum=0
sum1=0
fact=0
i=1
while(x>0):
	last=x%10
	reverse=reverse*10+last
	x=x//10
	
if temp==reverse:
	while temp>0:
		last1=temp%10
		sum+=last1
		temp=temp//10
print(sum)
"""


#write a program to swap given two numbers in a list:
"""
list1=[1,2,3,4,5]
index_num1=0
index_num2=0
temp=0
x=int(input("enter 1st num that you want to swap:"))
y=int(input("enter 2nd num that you want to swap:"))
if (x,y in list1):
	index_num1=list1.index(x)
	index_num2=list1.index(y)
	temp=list1[index_num1]
	
	list1[index_num1]=list1[index_num2]
	list1[index_num2]=temp
	print(list1)
"""

#swap elements in a string list:
"""
list1=["America","Berlin","Chicago","Delhi","England","France"]
x=input("enter the name that you want to swap:")
y=input("enter the another name that you want to swap:")
index_x=list1.index(x)
index_y=list1.index(y)
temp=list1[index_x]
list1[index_x]=list1[index_y]
list1[index_y]=temp
print(list1)
"""
#find the biggest number in a list without using built-in methods:
"""
list1=[1,10,2,20,3,2,366,43,109,4,5]
temp=0
for i in list1:
	if i>=temp:
		temp=i
print(temp)
"""	

#find the smallest number in a list without using the built-in methods:
"""
list1=[1,299,22,1,321,233,0,1]
temp=0
for i in list1:
	if i<=temp:
		temp=i
print(temp)
"""
"""
#drawing a graph using matplotlib:
import matplotlib.pyplot as plt
list1=[]
list2=[]
for i in range(-10,10):
	list1.append(i)
	list2.append(i*i)
plt.plot(list1,list2)
plt.show()"""

#printing patterns-01:
"""
x=int(input("enter no.of rows:"))
for i in range(x+1):
	for j in range(i):
		print("*",end=" ")
	print(" ")"""
#printing patterns -02:
"""
x=int(input("enter no.of rows:"))
for i in range(x+1):
	for j in range(x-i):
		print(" ",end=" ")
	for k in range(i):
		print("*",end=" ")
	for l in range(i-1):
		print("*",end=" ")
	print(" ")
for m in range(x+1):
	for n in range(m):
		print(" ",end=" ")
	for o in range(x-m):
		print("*",end=" ")
	for p in range(x-m-1):
		print("*",end=" ")

	print(" ")
	
"""


for i in range(101):
    print(i)
    

















 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                  













































































































































































































































































































































































































































































	











