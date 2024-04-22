import os

namee = []
phnoo = []
idcardd = []
list_room = ["1001","1002","1003","1004","1005","1006","1007","1008","1009","1010"]

cur_path = os.getcwd()
open_info = open(cur_path+"/info.txt",'r', encoding='utf8')
info_data = open_info.read()
print(info_data)

def home():
    print("="*100)
    print("\t\t\t\t\t\t ยินดีต้อนรับสู่โรงแรมซอยปลาเค็ม\n") 
    print("\t\t\t 1 Check in\n") 
    print("\t\t\t 2 Check out\n")

    ch = int(input("->:"))

    if ch == 1:
        print("-"*50)
        checkin()

    if ch == 2:
        print("-"*50)
        checkout()
    
def checkin():
    checkin = int(input("ท่านต้องการเข้าพักกี่วัน (วันละ 800 บาท):"))
    print("จำนวนเงินที่คุณต้องจ่าย :",cal(checkin),"บาท")
    print("="*100)
    print("โปรดกรอกข้อมูลดังนี้เพื่อยืนยันการเข้าพัก")
    info()
    print("="*100)
    print("\nห้องพักของท่านคือห้อง",list_room[0])
    del list_room[0]
    print("ขอบคุณที่ใช้บริการโรงแรมของเรา ขอให้ท่านพักผ่อนอย่างสบายใจ\n")
    home()

def checkout():
    ask = str(input("หมายเลขห้องของท่านคือ:"))
    if ask!="":
        list_room.append(ask)
        
    out = str(input("ท่านได้พักเกินกำหนดหรือไม่ y/n :"))
    if out == 'y':
        ooo = int(input("กี่วัน :"))
        print("-"*50)
        print("จำนวนเงินที่คุณต้องจ่ายเพิ่ม :",cal(ooo))
        print("-"*50)
    out2 = str(input("ท่านได้ใช้เซ็ตสิ่งของของทางโรงแรมหรือไม่ y/n :"))
    if out2 == 'y':
        ooo2 = int(input("กี่เซ็ต :"))
        print("-"*50)
        print("จำนวนเงินที่คุณต้องจ่ายเพิ่ม :",cal2(ooo2))
        print("-"*50)
        print("ขอบคุณที่ใช้บริการโรงแรมของเรา")
    else:
        print("-"*50)
        print("ขอบคุณที่ใช้บริการโรงแรมของเรา")

    home()

def cal(c):
    day = 800
    pay = day * c
    return pay

def cal2(o):
    product = 50
    pay2 = product * o
    return pay2

def info():
    while 1:
        name = str(input("ชื่อ: "))
        phno = str(input("หมายเลขโทรศัพท์: "))
        idcard = str(input("เลขบัตรประชาชน: "))
        
        if name!="" and phno!="":
            namee.append(name)
            phnoo.append(phno)
            idcardd.append(idcard)
            break

        else:
            print("ชื่อหรือเบอร์โทรศัพท์หรือเลขบัตรประชาชนของคุณไม่ถูกต้อง")


home()