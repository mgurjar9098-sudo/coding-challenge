# import threading

# t=threading.current_thread().getName()
# print('hello world !')
# print(t)



# create thread without using class

# from threading import Thread

# def disp():
#     for i in range(5):
#         print("thread is running",end="\n")


# t=Thread(target=disp)
# t.start()

# for i in range(5):
#     print("main threading",end="\n")\


# using getname and setname and name property
# getname and setname are depricated

# from threading import Thread,current_thread

# def disp():
#     print("thread is running",current_thread().name,end="")
#     current_thread().name="doc1"
#     print("new thread is running",current_thread().name,end="")

# t=Thread(target=disp)
# t.start()

# print('main thread',current_thread().name,end="")
# current_thread().name="rahul"
# print("new main thread",current_thread().name,end="")


# creating a threading using child class 

# from threading import Thread

# class mythread(Thread):
#     def run(self):
#         for i in range(5):
#             print("child threading is running")


# t=mythread()
# t.start()
# t.join()
# for i in range(5):
#     print('main thread is running')



# thread child class with constructor

# from threading import Thread

# class myThread(Thread):

#     def __init__(self):
#         Thread.__init__(self)
#         print("child constructor is callled")

#     def run(self):
#         pass
        


    

# t=myThread()
# t.start()

# print('main thread')


# creating a thread without a child clsss
# from threading import Thread

# class myThread:

#     def disp(self,a):
#         print("this is my class")

    
# obj=myThread()
# t=Thread(target=obj.disp,args=(11,))
# t.start()



# single tasking using thread
from threading import Thread
from time import sleep

class mythread:

    def qusetion_solved(self):
        self.q1()
        self.q2()
        self.q3()


    def q1(self):
        sleep(3)
        print("qustion 1 is solved")

    def q2(self):
        sleep(3)
        print("qustion 2 is solved")


    def q3(self):
        sleep(3)
        print("qustion 3 is solved")

my=mythread()
t=Thread(target=my.qusetion_solved)
t.start()
