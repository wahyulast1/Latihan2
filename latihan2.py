maks = 0

while True:
        a = int(input("Masukan bilangan:"))
        if a >= maks:
            maks = a
        if a == 0:
            break

print("Bilangan terbesar adalah:",maks)
