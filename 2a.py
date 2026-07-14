quantity = int(input("รับมาขายเท่าไหร่ : "))
cost = int(input("ต้นทุน : "))
sell = int(input("ราคาขาย : "))
members = int(input("จำนวนลูกน้อง : "))

total_cost = quantity * cost
total_sell = quantity * sell
profit = total_sell - total_cost
boss = int(profit * (1/20))
share = (profit - boss) / members

print("ต้นทุนทั้งหมด ", total_cost , " บาท")
print("ยอดขายทั้งหมด ", total_sell , " บาท")
print("กำไรสุทธิ ", profit , " บาท")
print("หักให้บอส ", boss , " บาท")
print("ลูกน้องแต่ละคนได้ ", share , " บาท")