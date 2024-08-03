# letters = ["a", "b", "c", "d"]
# d = letters[3]
# a = letters[0]
# letters[0] = d
# letters[3] = a
# print(letters)

# numbers = [1,2,3,4,5]
# numbers.append(6)
# numbers.remove(3)
# numbers.insert(0,-1)
# print(numbers)


fruits =["มะนาว", "มะม่วง", "ลำไย", "ส้ม", "แก้วมังกร"]
fruits.insert(3,"มะเขือเทศ")
fruits.insert(0,"Shinchan")
fruits.remove("มะม่วง")
fruits.insert(2,"Ultraman")
Ultraman = fruits[2]
ลำไย = fruits[4]
fruits[2] = ลำไย
fruits[4] = Ultraman
print(fruits)