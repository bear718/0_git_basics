import threading
from time import sleep, time

lock = threading.Lock()

def work(n):
    sleep(1)
    with lock:
#        print("это сообщение из функции", n)
        pass
   

balance = 100

def calculate():
    s = 1234567
    p =6543
    for i in range(1000000):
        s = s % p

def spend_money(amount=30):
    global balance
    with lock:
        if balance > amount:
            sleep(0.01)
            balance -= amount
        print(balance)

start = time()
    
print("это сообщение до функции")    

workers=[]

#work()
for i in range(100):
    t1 = threading.Thread(target=calculate)
    t1.start()
    workers.append(t1)
#    t1.join()

#t1 = threading.Thread(target=work, args=[10])
#t1.start()


print("это сообщение после функции")  

#t1.join()
for w in workers:
    w.join()

print(time() - start)  