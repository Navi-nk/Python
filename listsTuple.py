#lists - mutable
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
sublist = [34,'rich']
list[2]=2.21
#list[5]='navi' #error out of bound
list=list+['navi']
print(list[1:3])
print(list*2)
slist=(sublist+list)
print(slist)

#tuple immutable
tp=(2,21,43)
tp1=('navi',) #syntax for making a 1-tuple 
print(tp,tp1) 
#tp[1]=5 #error because tuple is immutable
#tp[3]=89 #doesnot work
tp=tp+('navi',) #or tp=tp+tp1
print(tp[:2]) #prints first 2 elements


#supercool
print(tp[::-1]) #reverse the values!! simple as that
#first empty: means start at beginning
#second empty: means traverse till end
#-1 means traverse list backwards
print(tp[::1]) #same as print(tp)