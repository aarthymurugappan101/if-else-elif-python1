#diviislbe by 4 and not diviible by 100 or dibvible by 400

year1 = 1996
year2 = 1900
if (year1 % 4 == 0 and year1 % 100 != 0) or year1 % 400 == 0:
    print("Year 1 is a leapyear")