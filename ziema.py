raksts = input("Vards un Uzvards: ")
with open("ziema.txt", "w", encoding='utf8') as tay:
    tay.write(raksts)