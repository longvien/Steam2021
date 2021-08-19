# Them thu vien de tao so ngau nhien
import random

print("Chung minh cung choi oan tu ti nhe!")

# lenh nay cho ta 1 trong 3 so 0, 1, 2 mot cach ngau nhien
random_number = random.randint(0, 2)
if random_number == 0:
    computer_choice = "keo"
elif random_number == 1:
    computer_choice = "bua"
else:
    computer_choice = "bao"

# Goi y:
# so sanh du lieu nguoi dung nhap vao voi bien computer_choice:  
# trong nhung truong hop nao thi may tinh va nguoi choi hoa nhau?
# trong nhung truong hop nao thi nguoi choi thang?
# trong nhung truong hop nao thi may tinh thang?

# Hoc sinh lap trinh tu dong nay tro xuong
vukhi = input("Ban ra gi? ")
print("May tinh ra "+ computer_choice)
if vukhi == "bua" and computer_choice == "bua":
    print("Hoa roi!")
elif vukhi == "bua" and computer_choice == "bao":
    print("Ban da thua!")
elif vukhi == "bua" and computer_choice == "keo":
    print("Ban da thang!")
elif vukhi == "bao" and computer_choice == "keo":
    print("Ban da thua!")
elif vukhi == "bao" and computer_choice == "bua":
    print("Ban da thang!")
elif vukhi == "bao" and computer_choice == "bao":
    print("Hoa roi!")
elif vukhi == "keo" and computer_choice == "bao":
    print("Ban da thang!")
elif vukhi == "keo" and computer_choice == "bua":
    print("Ban da thua!")
elif vukhi == "keo" and computer_choice == "keo":
    print("Hoa roi!")