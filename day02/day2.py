# # a = 10
# # b = 10
print("STart")
# # print(a ,b)
# c = "Ahtisham"
# d = "Parveen"
# # print("c" + "d")
# print(c + " " +d)


a = 10
b= 5
# Arithmatic oprators

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**2)
# print(a//3) #round off

# a = a+b this means a+=b
# a-=b    this means a = a-b
# print(a)

# logical oprators
# print(a==b) false
# print(a<b)  false
# print(a<=b) false

# print(a>b)  true
# print(a!=b) true
# print(a>=b)  true
A_age = 18
user_age = 18
# and and or 
# print(A_age<user_age or user_age==18) one of all so its true
# print(not A_age == user_age) this means average age user age k equal nhin h 
string = "Ahtisham" #string
# print("a" in str)  in and not in used to find the world or letter
#  in the string 
#in and not in are called membership operators
friends = ['Hamza','Daniyal','Sahil','Afzal'] #list 
# if("Hamza" in friends):
#     print ("yes") true

# else:
#     print("no")
# if("amza" in friends):
#     print ("yes")

# else:
#     print("no") true

# if("amza" not in friends):
#     print ("yes") true

# else:
#     print("no") false

# identity oprators
# print(a is b,a==b) # if all the variables have the same value return true
# print(a is not b,a!=b)# if all the var have the different value return false


# bitwise oparations binery oparations
# print (bin(a)) 
# print (bin(b))
# print(a&b,bin(a&b))
# print(a|b,bin(a|b))

# data types

# number                           
# print(a,type(a)) int

# a = 6.6
# print(a,type(a)) float

# a= 6.5j
# print(a,type(a)) complex

# string 
# print(string)
# str = """ahtisham  string triple qoutes are used for spacing like
#where ever you want to write
# Yousaf
# a 
# python
# developer"""
# print(str)



# list: list is an ordered sequence of items it is very flexible []
# list is mutable data type
# list = [4,"ahtisham",5.5]
# list[0] = "develper"
# print(list[0])
# print(list)


# tuple values should be more than one
tuple = (10,20,"AI")
# tuple = (10,10)
# tuple[1]= 0 error tuple is not changable
# print(tuple,type(tuple))

# dictionary = {
#     "name":"Ahtisham",
#     'Father':"Yousaf",
#     "course":"Python",
# }
# # print(dictionary,type(dictionary))
# # dictionary[0]= "first name" #in this line 0 is a new key and first name is value
# dictionary['name']= "bilal" # this line change the value of name key
# print(dictionary)
# print(dictionary["Father"])
# print(dictionary["course"])
# print(dictionary[0]) Error doesn't support indexing

# set inmutable
# s = {1,1,2,3,4,4}
# s[2]= 4 #error becouse set is no changable

# print(set,type(set))

# input and cancatination
# input1 = input("Enter the name:-")
# input2 = input("Enter your father name:-")
# print(input1+" "+input2)
# print(input1 + input2)
# int
# input1 = int(input("Enter the num1:-"))
# input2 = int(input("Enter the num2:-"))
# print(input1+" "+input2) Error this is just for str
# print(input1+input2)
# input1 = eval(input("Enter Your Age:")) #also support float + int
# input2 = eval(input("Enter height:-"))
# print(input1+input2)


# if statements
# if input1 >= 18 and input1 <= 24:
#     print("User age is",input1,"He is eligible")

# else:
#     print("User age is",input1,"He is not eligible")

# print(type(input1))
# input1 = eval(input("Enter your marks:"))
# marks = input1
# totalMarks = 1000
# # user_marks = int(marks / totalMarks * 100)
# user_marks = marks / totalMarks * 100
# # print(user_marks, type(user_marks))

# if user_marks >= 90:
#     print("A+ Grad",user_marks,"%")
# elif user_marks >= 80:
#     print("A Grad",user_marks,"%")
# elif user_marks >= 70:
#     print("B Grad",user_marks,"%")
# elif user_marks >= 50:
#     print("C Grad",user_marks,"%")
# elif 30 <= user_marks > 20:  # Adjusted this condition
#     print("just pass",user_marks,"%")
# else:
#     print("Fail",user_marks,"%")


# Range 
range(10)
# start 0
# condition<10
# increamant 1
range(1,10)
# start 1
# condition<10
# increamant 1
range(1,10,2)
# start 2
# condition<10
# increamant 2

# for loop in range
# for n in range(11):
#     print(n)
# print("___________")

# for n in range(1,11):
#     print(n)
# print("___________")

# for n in range(1,11,2):
#     print(n)

# for a in range(1,11):
#     print("3 *",a,"=",3*a)

# for a in range(1,11):
#     print("4 *",a,"=",4*a)

# reverse range 
            
# for a in range(10,-1,-1): #Start,Stop ,step
#     print(a)
# print("__________")
# for a in range(10,4,-2):
#     print(a)

# while loop
# i = 0
# while i<= 10: #jab tak i 10 sy kam h
#     print(i,"i love you")
#     i=i+1

# print(i) i saves last value
# i = 10
# while i>=1:# loop tb tk chlay ga jb tk i ki value 1 or 1 sy km na hojay
#     print(i,"i love you")
#     i=i-1
#     # print(i)


# print(i) i main 0 hoga

# string 
# we can use single ,double and even triple quotes

str1 = 'Ahtisham yousaf'
# print(str1.count("a"))
# print(str[14]) error str is keyword
# print(str1[-6]) #y
# # slicing
# print(str1[:]) #starts at 0,goes till end 
# print(str1[0:5]) #From index 0 to index 4 (5 is excluded).
# print(str1[9:15])
# print(str1[0::2]) # rem : means start from 0, :: all execute with increament of 1
# print(str1[::2])
# print(str1[::-2])
# print(str1[::-1])
# print(str1[-2::-2])
# print(str1[-1::-2])
# print(str1[-1::-1])

# string itration 

# length = len(str1)
# print(length)


#enumerate 
# for index,char in enumerate(str1,start=1):
#     print(index,char)

# reverse slicing
# reverse_str = str1[-1::-1] 
# length = len(reverse_str)
# # print(length)
# for range in range(length):
#     print(reverse_str[range])

# reverse_str = str1[-1::-1] 
# length = len(str1)
# # print(length)
# for range in range(length-1,-1,-1):
#     print(str1[range])
# str1 = str1[-1::-1]
# for range in str1:
#     print(range)

# string functions
# lower_case = str1.lower() # rem:use for data matching
# print(lower_case)

# upper_case = str1.upper() #rem: all in upper case
# print(upper_case)

# love="i love you"
# title = love.title() #rem: just first word of all the letters
# print(title)

# captalize = love.capitalize() #rem: just first word of the text
# print(captalize)

# print(str1.find('a')) #rem: to find the chractors in the string
# print(friends.find('Hamza')) #rem: find is only a string function 
# print(str1.find('y'))
# print(str1.find('a',8)) #rem: if value is not find it returns -1

# print(str1.index("a")) #rem: it gives the index no.
# print(str1.index("z")) if value is not find it returns run time
#  error
# isalpha = 'ahtisham'
# print(isalpha.isalpha()) #true
# print(isalpha.isdigit()) #false

# isdigit = '132543'
# print(isdigit.isalpha()) #false
# print(isdigit.isdigit()) #True

# str1 = '45'
# print(str1.isalpha()) false
# print(str1.isdigit()) true means int iniside the qoutes

# str1 = 'ahtisham45'
# print(str1.isalnum()) #rem: true used for string and integers 
# it return an error when there is some special characters 
# like #,!,$.....

# str1 = 'ahtisham 45'
# print(str1.isalnum()) error

# chr to str
# ascii = chr(65)
# print(ascii,type(ascii)) #rem: type = str
# ascii = chr(66)
# print(ascii,type(ascii))
# ascii = chr(67)
# print(ascii,type(ascii))
# ascii = chr(68)
# print(ascii,type(ascii))

# for abc in range(65,110,1):
#     # b = abc
#     print(chr(abc))


# str_to_chr = "a"
# print(ord(str_to_chr))


# 2nd day 25/9/2024
# format()
# str = "{}htisham {}ousaf".format("A","Y")
# print(str)
# str = "{1}htisham {0}ousaf".format("A","Y")
# print(str)
# str = "{a}htisham {b}ousaf".format(a=40,b = 30)
# print(str)
# str = "{a:8}htisham {b:5}ousaf".format(a=40,b = 30)
# print(str)
# :
# ------40 right normal
# ^
# ---40--- center
# <
# 40------ left
# >
# ------40 right 
# str = "{a:^9}htisham {b:5}ousaf".format(a=40,b = 30)
# print(str)
# str = "{a:>8}htisham {b:5}ousaf".format(a=40,b = 30)
# print(str)
# str = "{a:<8}htisham {b:5}ousaf".format(a=40,b = 30)
# print(str)

# list mutable ,changable [] ,spreated

# print(list)
list = [1,2,3,4,[5,6,7],"parveen"]
# list [5]="Ahtisham"
# print(list)
# print(list[0])
# print(list[4][2])
# print(list[4],list[2])
# print(list[5])

# reverse slicing
# print(list[-1])
# print(list[-2],list[-3])
# print(list[0:5])
# print(list[-1::-1])
# print(list[1:])rem: start = 1, : all list,incr of 1 default
# print(list[1::]) rem: start = 1, :: all list,incr of 1 default
# print(list[1::1]) rem: start = 1, :: all list,incr of 1 default

#NOTE:three parameters -1,
#blank means for all list,:: end tk read kro
#-1 decreament

#Q: for loop for list 
#Q:how to get the list items or elements

# use: using len funtion
# length = len(list)
# for range in range(length):
#  #  print(range)
#  # print(length)
#  print(range,list[range])

# q: loop working mathod
# rem: list[0]= first value 
# rem: list[1]=second value and so on 

# use: Reverse list slicing using for looop

# length= len(list)
# for r in range(length-1,-1,-1):
#     print(list[r])

# rem: 
#use:by using range
# for r in list:
#     print(r)

# Q: list  fuctions
#  01 delete() rem: it use index to delete Use:use for list, it not return del value
# del list[5]
# del list[4]
# print(list)
# Q: del doesn't returns and pop() returns deleted value
# 02 pop() rem: 

# list.pop() rem: generally last index will be deleted
# list.pop(4) with indes
# list.pop(5)
# print(list.pop(5)) it returns poped value

# 03 remove()
# list.remove("parveen") rem: it remove the with value not index
# list.remove(1) #no
# print(list)

# 04
# clear
# list.clear()rem: it remove all the list values

# 5 insert()  
# list.insert(4,0) # rem: doesn't work without params
# print(list)
#6 append() rem: it adds the given value in last as it is whether its a list 
# list.append("Ahtisham")
new_list=[1,2,3]
# list.append(new_list)
# list.append(49)
# print(list)

#7 extends() rem: it adds the just values inside the brakets andder ki value
# list.extend(new_list) #good
# list.extend('ahtisham') #error
# print(list)
# #8 count
# n_list = [1,2,3,4,5,6,1,2,3]
# count = list.count(1)
# print(count)
#9 max
# max = max(list)
# max for string
# list = ['Ahtisham',"yousaf"]
# max = max(list)
# print(max)

#10 min
# min = min(list)
# print(min)

#11 sort()
# list.sort()
# print(list)

#12 reverse()
# list.reverse()
# print(list)

#13 index()

# print(list.index(2))
# print(list)


# Q: list  updations
# list[0]=2  it adds the value on 0 index

# list comprehension
# rem: normal method 
# list = []
# for r in range(1,101,1):
#     # list.extend(r) #rem: error becouse int not support only str 
#     list.append(r)

# rem: Advanced method to append the values in the list dynamically
# dyn_list = [r for r in range(1,101,1) if r%2 == 1]  # REM: both var in the [] must be same "r"
# dyn_list = [r for r in range(1,101,1) if r%2 == 1]  # filteration using if and modulus
# print(dyn_list)
# Q: for string 

# s = [r for r in str] # rem: it converts the string into list by words like 'a','h','t'
# print(s)

# treating two lists at the same time
# Q: zip()
# for a,b in zip(list,n_list):
#  print(a,b)

# length = len(list)
# for r in range(length):
#     print(list[r],n_list[r])

# Q: 
# input = input("Enter the value:")
# split = input.split()
# print(split)

# rem: conver text into str 
# list = []
# for r in range(1,4):
#     n = input("Enter the value"+str(r)+":")
#     list.append(n)

# print(list)

# REM: stack in python

# list = []
# while True:
#     c =int( input('''
#         1 push Elements
#         2 pop Elements
#         3 peek Elements
#         4 Display Stack
#         5 Exit
#     '''))
#     if c == 1:
#         input_no=input("Enter the value:")
#         list.append(input_no)
#         print(list)
#     elif c== 2:
#         if len(list)==0:
#             print("Empty Stack")
#         else:
#             pop = list.pop()
#             print(pop)
#             print(list)
            
#     elif c== 3:
#         if len(list) == 0:
#             print("Empty con3")
#         else:
#             print("last Stack value",list[-1])
#     elif c== 4:
#         print("Display Stack",list)
#     elif c==5:
#         break
#     else:
#         print("Chose form 1 to 5")
        
# list = []
# while True:
#     c =int( input('''
#         1 push(add) Element in list
#         2 pop(del) first Element of list
#         3 Front(first) Element of list
#         4 last Element of list
#         5 Display Queue(All list values)
#         6 Exit
#     '''))
#     if c == 1:
#         input_no=input("Add the value in list:")
#         list.append(input_no)
#         print("Value",input_no,"added",list)
#     elif c== 2:
#         if len(list)==0:
#             print("Initialy Queue(list) is empty,add some data first.")
#         else:
#             # pop = list.pop()
#             del list[0]
#             # print(pop)
#             print(list)
            
#     elif c== 3:
#         if len(list) == 0:
#             print("Initialy Queue(list) is empty,add some data first.")
#         else:
#             print("First queue(list) value is:",list[0])
#     elif c== 4:
#         if len(list) == 0:
#             print("Initialy Queue(list) is empty,add some data first.")
#         else:
#             print("Last queue(list) value is:",list[-1])
#     elif c== 5:
#         if len(list) ==0:
#             print("Queue(list) is empty",list)
#         else:
#            print("Your Queue(list)",list)
#     elif c==6:
#         break
#     else:
#         print("Chose form 1 to 5")

# Q: Dictionary: mutable,changable,{},use "key":"value"

dictionary ={
    "course":"Python",
    "sourse":"Youtube",
    "duration":"4days"
}
# Q: to insert the new data in the list
# dictionary["porpose"]="AI"
# dictionary["company"] = "Xeven Solutions"
# print(dictionary)
# print(dictionary["course"])
# for r in dictionary:
#     print(dictionary[r])

# Q: dictionary fuctions

# 1 get() use: to get value by key
# get = dictionary.get("course")
# print(get)

# # 2 keys() use: it targets the keys
# for r in dictionary.keys():
#     print(r)

# # 3 values() use: it targets the values
# for r in dictionary.values():
#     print(r)

# # 4 items() use: it use for both keys and values,it use two varables
# for a,b in dictionary.items():
#     print(a,b)
# print()

# # 5 del use: it deletes the value by using key, it is a keyword not function
# del dictionary["course"]
# print(dictionary)
# print()

# # 6 pop() use: it returns poped value but del keyword is not return
# pop = dictionary.pop("sourse")
# print(pop)
# print(dictionary)

#7 dict rem: it creates the dict
# dictionary = dict(name="ahtisham", Father_name = "Yousaf")
# print(dictionary)

#7 update() rem: it updates the value by key using {} if key already available it replace
# dictionary.update({"duration":"4daysss"})
# dictionary.update({"duration":"4days"})
# print(dictionary)

#7 clear() rem: all clear
# dictionary.clear()
# print(dictionary)

# Q: Nested  Dictionary

course= {
    "python":{'duration':'4days','fee':'free'},
    "php":{'duration':'4days','fee':'10'},
    "java":{'duration':'4days','fee':'20'}
}
# print(course)
# print(course['php'])
# print(course['php']['duration'])
# course['python']['fee'] = 49999
# del course['python']['fee']
# print(course)
# for index,value in course.items():
#     print(index,":",value['duration'])

# Q: tuple /
tuple =(1,2,3,4,5,1,2,3)
# print(tuple[0])
# tuple = ('python') # rem: str
# print(type(tuple))

# NOTE: itration
# length = len(tuple)
# for r in range(length):
#     print(tuple[r])

# NOTE: 2nd way of itration
# for r in tuple:
#     print(r)

# NOTE:tuple functions
# 1 min() rem: gives min value of tuple,only int
# min = min(tuple)
# print(min)

# 2 max() rem: gives max value of tuple


# 3 count() rem: count the value how many times it repeates

# 4 index()

# 5 sum()
# sum = sum(tuple)
# print(sum)
# sum = sum(tuple,9)
# print(sum)

# Q: sets
# s = {1,2,4,5,6}
# set [2] error undexed 
# for r in set:
#     print(r)
    
# Q: set fuctions
l = [1,2,3,4,5,"s",6,7]
# # 1 set() rem: convert into set whether it's list or dictionary or tuple
# s = set(l)
# print(s)

# 2 remove()
# s.remove("s")
# print(s)
# 3 discard()
# s.discard("s")
# # s.discard(1)
# print(s)
# 4 pop() rem: it return poped fisrt value
# print(s.pop())
# print(s.pop())
# print(s.pop())

# 5 clear() rem: it returns set() all clear
# s.clear()
# print(s)

# 6 add()
# s.add(8) int
# s.add("8") str
# s.add("ahtisha;m") str

# new_set = [ 8,9,7] error it only add single value
# s.add(new_set)
# print(s)
# print(s)

# 7 update() rem: it can a new list and set values with in the set
# new_set = {8,9,7}
# s.update(new_set)
# print(s)

# Q: funtions

# def simplefunction():
#     print("this is a simple funtion.")

# simplefunction()

# rem: funtion with arguments
# def sumdata(n,m):
#     print(n+m)

# sumdata(a,b)
# sumdata(1,2)

# def sumdata(n,m = 4):
#     print(n+m)

# sumdata(a)
# sumdata(1)

# rem:  retur function
# def sumdata(n,m = 4):
#     p = n+m
#     return p

# data =sumdata(a)
# data1 = sumdata(1)
# print(data)
# print(data1) 

# Q: Module






















