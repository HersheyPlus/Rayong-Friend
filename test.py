def choose_car():
    sum = 0
    while (True):
        print('*** เลือกประเภทรถ ​***')
        print('1. 4 ล้อ\n2.6 ล้อ\n3. มากกว่า 6 ล้อ\n4. รถพิเศษ (ยกเว้นค่าธรรมเนียม)\nE. ออกจากโปรแกรม')
        print("-----------------------------------")
        input_car = input("เลือกเมนู: ")
        if (input_car == 'E' or input_car == 'e'):
            print("ค่าธรรมเนียมทั้งหมด",sum)
            break
        else:
            if (input_car == '1'):
                print ("ค่าธรรมเนียม",'30','bath\n')
                sum+= 30
            elif (input_car == '2'):
                print ("ค่าธรรมเนียม",'50','bath\n')
                sum+= 50
            elif (input_car == '3'):
                sum+= 80
                print ("ค่าธรรมเนียม",'80','bath\n')
            else:
                print ("ฟรี")

choose_car()