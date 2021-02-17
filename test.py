# Time이 뭐냐?
# import time
#
# i=0
# while True:
#     print(i)
#     i=i+1
#     time.sleep(1)
#     print("Hello")
#     print("Hi")
#     print("Hola")


# Class Inheritance

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, Exhale")
#
# class Fish(Animal):
#     def __init__(self):     #이거 없어도 돌아가는데?
#         super().__init__()  #왜 있는거야?
#
#     def breathe(self):
#         super().breathe()
#         print("Doing this underwater")
#
#     def swim(self):
#         print("Moving in water")
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)


#turtle.write가 뭐지
# import turtle as t
# screen = t.Screen()
#
# tim = t.Turtle()
# tim.write("Home=", False, align='center', font=('Arial',8,'normal'))
# tim.fd(100)
# screen.exitonclick()

#slice는 또 뭐냐
nlist=['a','b','c','d','e','f']
mlist=nlist[1:5:3]
reverse_list=nlist[::-1]
print(nlist)
print(mlist)
print(reverse_list)