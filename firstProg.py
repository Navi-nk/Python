import math
print ("Hello Navi")  #double quotes to signify strings
print('What you want to do now ?') #single quotes to signify strings
#io=input();print(io)
print(("nice "*5)+'5')

io="""this is interesting""" #quadruple double quotes
print(io[6:]) #prints all after 6 elements
print(io[:6]) #prints first 6 elements

print(io[6:11]) #prints elements from 6th index till 11th index not including 11th index 

del io #cant use io anymore. goes out of scope

print(int(math.sqrt(9))) #int cast to round to nearest decimal


a=b=c=12 #multiple variable assignment to single value. nice feature

print(a,b,c)
b=2
print(a,b,c)

