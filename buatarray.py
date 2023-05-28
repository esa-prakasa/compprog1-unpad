import os
import array as arr
os.system("cls")

A = arr.array("i")

for i in range(0,10):
    A.append(2*i)
print("Nilai A awal")
print(A)

N = len(A)

for i in range(5):
    A[i] = A[i] * 10
print("\nSetelah dikalikan 10")
print(A)
print("\n")


