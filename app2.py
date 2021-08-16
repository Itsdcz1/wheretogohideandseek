from time import sleep
import random

print("1 end of area")
print("2 start of area")
print("3 middle of area")
print("4 random place")
print("5 rush")


n = input("Go? (y/n): ")

if n == "y":
    sleep(0.8)
    print(random.randint(1, 5))
if n == "n":
    print("Ok.")