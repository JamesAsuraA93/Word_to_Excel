import pandas as pd

# open file .txt
from pprint import pprint
# lines = []
# for i in range(3):
#     file = open(f"file/copy{i+1}.txt", "r")
#     lines.append(file.readlines())
#     file.close()
#
# del i

# print(len(lines[0]))
# print(len(lines[1]))
# print(len(lines[2]))
# lst_content might control different len(files)
def display(data, index):
    lst_content = ['วันที่','สัญญาเลขที่','สัญญาฉบับนี้ทำขึ้นระหว่าง','ผู้ให้เช่าตกลง','เครื่องรุ่น','หมายเลขเครื่อง','จำนวน','สถานที่ตั้ง','ตู้รองเครื่อง','สัญญานี้มีผลบังคับใช้เป็นเวลา','ค่าเช่าเครื่องเดือนละ','Fax','Printer','ถ่ายเอกสาร','คิดอัตราค่าบริการ','ถ่ายเอกสาร','หักค่ากระดาษเสียให้ฟรีกับผู้เช่า','ค่าเงินประกันความเสียหาย']
    start = 0
    temp = 0
    stop = 40

    for i in range(len(lst_content)):
        while start < stop:
            if lst_content[i] in data[index][start]:
                if i == 0:
                    data = {'วันที่': data[index][start].replace('วันที่', '').strip()}
                elif i == 1:
                    data = {'สัญญาเลขที่': data[index][start].replace('สัญญาเลขที่', '').strip()}
                elif i == 2:
                    data = {'สัญญาฉบับนี้ทำขึ้นระหว่าง': data[index][start].split('กับ')[1].split('ซึ่งต่อไปนี้ในสัญญานี้จะเรียกว่า')[0].strip()}
                elif i == 3:
                    data = {'ผู้ให้เช่าตกลง': data[index][start].split('จำนวน')[1].strip()}
                elif i == 4:
                    data = {'เครื่องรุ่น': data[index][start].split(':')[1].strip()}
                elif i == 5:
                    data = {'หมายเลขเครื่อง': data[index][start].split(':')[1].strip()}
                elif i == 6:
                    data = {'จำนวน': data[index][start].split(':')[1].strip()}
                elif i == 7:
                    data = {'สถานที่ตั้ง': data[index][start].split(':')[1].strip()}
                elif i == 8:
                    data = {'ตู้รองเครื่อง': data[index][start].split('จำนวน')[1].split('ตู้')[0].strip()}
                elif i == 9:
                    data = {'สัญญานี้มีผลบังคับใช้เป็นเวลา': data[index][start].split('เวลา')[1].split('จนถึง')[0].strip()}
                    data = {'จนถึง' : data[index][start].split('เวลา')[1].split('จนถึง')[1].strip()}
                elif i == 10:
                    data = {'ค่าเช่าเครื่องเดือนละ':data[index][start].split('ค่าเช่าเครื่องเดือนละ')[1].strip()}
                elif i == 11:
                    data = {'Fax':data[index][start].split('=')[1]}
                elif i == 12:
                    data = {'Printer': data[index][start].split('=')[1]}
                elif i == 13:
                    data = {'ถ่ายเอกสารฟรี': data[index][start].split('ฟรี')[1].split('ส่วนเกินตั้งแต่')[0]}
                    data = {'ส่วนเกินตั้งแต่': data[index][start].split('ฟรี')[1].split('ส่วนเกินตั้งแต่')[1]}
                elif i == 14:
                    data = {'คิดอัตราค่าบริการ': data[index][start].split('สำเนาละ')[1].strip()}
                elif i == 15:
                    data = {'หักค่ากระดาษเสียให้ฟรีกับผู้เช่า':data[index][start].split('หักค่ากระดาษเสียให้ฟรีกับผู้เช่า')[1].split('%')[0].strip() + " %"}






                print(lst_content[i],':',data[index][start].strip())
                temp = start
                start += 1
                break
            else:
                # pass
                # print(f"{detail} : ไม่พบข้อมูล")
                # print(data[index][start].strip())
                start += 1
        start = temp
    print('\n')


# for i in range(len(lines)):
#     display(lines[i], i)
    # print(data[index][2].strip())  # วันที่
    # print(data[index][3].strip())  # สัญญาเลขที่
    # print(data[index][5].strip())  # สัญญาฉบับนี้ทำขึ้นระหว่าง
    # print(data[index][7].strip())   # ผู้ให้เช่าตกลง
    # print(data[index][12].strip())   # ตู้รองเครื่อง
    # print(data[index][14].strip())   # สัญญานี้มีผลบังคับใช้เป็นเวลา
    # print(data[index][17].strip())   # วันที่ทำสัญญา
    # print(data[index][25].strip())   # ค่าเช่าเครื่องเดือนละ


# display(lines, 0)
# display(lines, 1)
# display(lines, 2)


lines = []
for i in range(4):
    file = open(f"file/copy{i+1}.txt", "r")
    lines.append(file.readlines())
    file.close()
    display(lines, i)

# for i in range(len(lines)):
#     print(i) if 'ค่าเช่าเครื่องเดือนละ' in lines[i] else None
#

# file = open("file/(64-483)นิติบุคคลอาคารชุด พลัม คอนโด มิกซ์ แจ้ง.doc", "r",encoding="latin-1",errors="xmlcharrefreplace")
# data = file.readlines()
# file.close()
#
# print(data)