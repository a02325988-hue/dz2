import re
minyons_1 = "Minyon minYon Mineyon mIniYon monyon minyon mInYon MINYON moNyOn ManyoN"
minyons_2 = "minyon miNyon mIneYon MinYoN MaNyon MonYon Minyon Bob ManYon minYON MiNyon MinyoN MonyoN"
Bob = re.compile("Bob") #створення обєкту для роботи з регулярними виразами
match_1 = Bob.search(minyons_1) #search шукає перший збіг
print(match_1)
match_2 = Bob.search(minyons_2)
print(match_2)

match_3 = Bob.finditer(minyons_1) #finditer шукає всі збіги
for item in match_3:
    print(f"match_1: {item}")
match_4 = Bob.finditer(minyons_2) #finditer шукає всі збіги
for item in match_4:
    print(f"match_2: {item}")

match_5 = Bob.findall(minyons_1) #findall створює список з усіма входженнями
match_6 = Bob.findall(minyons_2)
print(match_5)
print(match_6)

minyons_with_kevin_1 = Bob.sub("Kevin", minyons_1) #sub зміна чогось на щось
print(minyons_with_kevin_1)

minyons_with_kevin_2 = Bob.sub("Kevin", minyons_2)
print(minyons_with_kevin_2)

split_result = Bob.split(minyons_1)
print(split_result)

fullmatch_1 = Bob.fullmatch(minyons_1)
fullmatch_2 = Bob.fullmatch(minyons_2)

print(fullmatch_1)
print(fullmatch_2)

login_patern = re.compile(r"^/w{3,20}") #r =raw рядок буде приймати буквено-циферні символи та _