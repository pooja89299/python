# a=1
# b=10
# sum=0
# while a<=b:
#     sum+=a
#     a+=1
# print(sum)





# list=[4,5,6]
# list.append(8)
# print(list)



# list=[1,2,3,4,5,]

# add=list.append(9)
# print(add)





# a=8
# b=5
# c=6
# if a>b and a>c:
#     print(a,"grater than")
# elif b>a and b>c:
#     print(b,"grater than")
# else:
#     print("nothin")






# for i in range (0,10):
#     if i ==5:
#         break
#     print(i)



# for i in range(1,21):
#     if i%2==0:
#         print(i)




# a=1
# while a<=10:
#     print(a)
#     a+=1



# i=2
# while i<=28:
#     print(i)
#     i=i+2



# i=1
# while i<=20:
#     if i==5:
#         continue
#     print(i)
#     i=i+1




# a=1
# while a<=100:
#     if a%3==0 and a%5==0 and a%10!=0:
#         print(a)
#     a+=1




# for i in range (2,10,2):
#     print(i)



# my_list=[]
# i=1
# while i<=30:
#     squares=i*i
#     my_list.append(squares)
#     i=i+1
# print(my_list)






# new_list=[]
# i=1
# while i<=5:
#     squares=i*i
#     new_list.append(i)
#     new_list.append(squares)
#     i=i+1
# print(new_list)




# if 100-33==55:
#     print("equal")
# else:
#     print(" not equal")


# a=int(input("enter a number"))
# while a<=100:
#     if a%2==0:
#         print(a,"*")
#     else:
#         print(a,"#")
#     a=a+1







# marks=[30,23,25,38,45,55,66,64,84,93,63,58,39,42]
# length=len(marks)
# i=0
# less_than50=0
# more_than50=0
# while i<length:
#     count=marks[i]
#     if count<50:
#         less_than50=less_than50+1
#     else:
#         more_than50=more_than50+1
#     i+=1
# print("the number of  student who get more than 50",str(more_than50))
# print("the number of  student get less than 50",str(less_than50))





# p=int(input("entar the total page"))
# n=int(input("enter the page which you want to go"))
# s=p//2
# t=n//2
# v=s-t
# m=min(t,v)
# print(m)

# p=int(input("entar the total page"))
# n=int(input("enter the page which you want to go"))
# s=p//2
# t=n//2
# v=s-t
# if v>t:
#     print(t)
# else:
#     print(v)






# s=input("enter string")
# list1=[]
# k=0
# for i in range (len(s)):
#     if len(list1)==0 or list1[-1]!=s[i]:
#         list1.append(s[i])
#     else:
#         list1.pop()
# # print(list1)   
# if len(list1)==0:
#     print("empty string")
# else:
#     for i in range(len(list1)):
#         k="".join(list1)
#     print(k)

         


# a=int(input("enter number"))
# b=int(input("enter number"))
# c=int(input("enter number"))
# count=0
# for i in range (a,b+1):
#     rvs=int(str(i)[::-1])
#     if (i-rvs)%c==0:
#         count=count+1
# print(count)




# a=int(input("enter number"))
# b=int(input("enter number"))
# c=int(input("enter number"))
# count=0
# while a<=b:
#     n=a
#     r=0
#     while n>0:
#         r=r*10+n%10
#         n=n/10
#     d=abs(a-r)
#     if d%c==0:
#         count=count+1
#     a=a+1
# print(count)

# s=input("enter string")

# a=s.lower()
# c=a.split()
# print(c)
# d="".join(c)
# b={}
# b=set(d)
# print(b)

# if len(b)==26:
#     print("pangram")
# else:
#     print("not pangram")





# n=input("enter")
# a=[]
# c=0
# for i in n:
#     if i not in a:
#         a.append(i)
#         c=c+1
#     else:
#         a.append(i)
# print(a)
# print(c)




# l=int(input("enter length"))
# pw=input("enter password")











elements=[23,14,56,12,19,9,15,31,42,43]
i=0
y=[]
a=[]
sum=0
sum1=0
while i<len(elements):
    b=elements[i]
    if b%2==0:
        y.append(b)
        sum=sum+b
    else:
        a.append(b)
        sum1=sum1+b
    i=i+1
print("even number",y,sum)
print("odd number",a,sum1)  



















