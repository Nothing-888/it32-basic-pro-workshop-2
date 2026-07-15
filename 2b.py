name = input("ชื่อ : ")
age = int(input("อายุ : "))
height = int(input("ส่วนสูง : "))
power = int(input("พลัง : "))
money = int(input("เงิน : "))

if money < 100 :
    print("ไม่รับ เพราะ จนเกินไป บอสไม่ชอบ")
elif money >= 100 & money <= 1000 :
    print("ไม่รับ เพราะ จน")
elif money > 1000 & money <= 10000 :
    print("รับ เพราะ สงสาร ไปเป็นภารโรง")
elif money > 10000 & money <= 100000 :
    print("รับ เพราะ พอมีเงิน ผมเป็นลูกน้องได้")
else :
    print("รับ เพราะ รวย บอสชอบ บอสรัก ไปเป็นหัวหน้าเลย")
