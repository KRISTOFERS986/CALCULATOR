print("Kalkulators")

a = float(input("Pirmais skaitlis: "))
b = float(input("Otrais skaitlis: "))

print("Summa:", a + b)
print("Starpība:", a - b)
print("Reizinājums:", a * b)

if b != 0:
    print("Dalījums:", a / b)
else:
    print("Dalīt ar 0 nevar!")
