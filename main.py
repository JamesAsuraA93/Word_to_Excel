import pandas as pd
import xlsxwriter
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
    data2 = {}
    lst_content = ['วันที่', 'สัญญาเลขที่', 'สัญญาฉบับนี้ทำขึ้นระหว่าง', 'ผู้ให้เช่าตกลง', 'เครื่องรุ่น',
                   'หมายเลขเครื่อง', 'จำนวน', 'สถานที่ตั้ง', 'ตู้รองเครื่อง', 'สัญญานี้มีผลบังคับใช้เป็นเวลา',
                   'ค่าเช่าเครื่องเดือนละ', 'Fax', 'Printer', 'ถ่ายเอกสาร', 'คิดอัตราค่าบริการ', 'ถ่ายเอกสาร',
                   'หักค่ากระดาษเสียให้ฟรีกับผู้เช่า', 'ค่าเงินประกันความเสียหาย']
    start = 0
    temp = 0
    stop = 40
    # data2['วันที่'] = data[index][1].replace('วันที่', '').strip() if data[index][1] else ''
    # data2['สัญญาเลขที่'] = data[index][start].replace('สัญญาเลขที่', '').strip()
    # print(data2)
    for i in range(len(lst_content)):
        while start < stop:
            if lst_content[i] in data[index][start]:
                if i == 0:
                    data2['วันที่'] = [data[index][start].replace('วันที่', '').strip()] if data[index][start] else ''
                elif i == 1:
                    data2['สัญญาเลขที่'] = [data[index][start].replace('สัญญาเลขที่', '').strip()] if data[index][start] else ''
                elif i == 2:
                    data2['สัญญาฉบับนี้ทำขึ้นระหว่าง'] = \
                    [data[index][start].split('กับ')[1].split('ซึ่งต่อไปนี้ในสัญญานี้จะเรียกว่า')[0].strip()] if data[index][start] else ''
                elif i == 3:
                    data2['ผู้ให้เช่าตกลง'] = [data[index][start].split('จำนวน')[1].strip()] if data[index][start] else ''
                elif i == 4:
                    data2['เครื่องรุ่น'] = [data[index][start].split(':')[1].strip()] if data[index][start] else ''
                elif i == 5:
                    data2['หมายเลขเครื่อง'] = [data[index][start].split(':')[1].strip()] if data[index][start] else ''
                elif i == 6:
                    data2['จำนวน'] = [data[index][start].split(':')[1].strip()] if data[index][start] else ''
                elif i == 7:
                    data2['สถานที่ตั้ง'] = [data[index][start].split(':')[1].strip()] if data[index][start] else ''
                elif i == 8:
                    data2['ตู้รองเครื่อง'] = [data[index][start].split('จำนวน')[1].split('ตู้')[0].strip()] if data[index][start] else ''
                elif i == 9:
                    data2['สัญญานี้มีผลบังคับใช้เป็นเวลา'] = [data[index][start].split('เวลา')[1].split('จนถึง')[
                        0].strip()] if data[index][start] else ''
                    data2['จนถึง'] = [data[index][start].split('เวลา')[1].split('จนถึง')[1].strip()] if data[index][start] else ''
                elif i == 10:
                    data2['ค่าเช่าเครื่องเดือนละ'] = [data[index][start].split('ค่าเช่าเครื่องเดือนละ')[1].strip()] if data[index][start] else ''
                elif i == 11:
                    data2['Fax'] = [data[index][start].split('=')[1]] if data[index][start] else ''
                elif i == 12:
                    data2['Printer'] = [data[index][start].split('=')[1]] if data[index][start] else ''
                elif i == 13:
                    data2['ถ่ายเอกสารฟรี(ขาวดำ)'] = [data[index][start].split('ฟรี')[1].split('ส่วนเกินตั้งแต่')[0]] if data[index][start] else ''
                    data2['ส่วนเกินตั้งแต่(ขาวดำ)'] = [data[index][start].split('ฟรี')[1].split('ส่วนเกินตั้งแต่')[1]] if data[index][start] else ''
                elif i == 14:
                    data2['คิดอัตราค่าบริการ'] = [data[index][start].split('สำเนาละ')[1].strip()] if data[index][start] else ''
                elif i == 15:
                    data2['ถ่ายเอกสาร(สี)'] = [data[index][start].split('สี')[1].split('คิดอัตราค่าบริการ')[0]] if data[index][start] else ''
                    data2['คิดอัตราค่าบริการ(สี)'] = [data[index][start].split('สี')[1].split('คิดอัตราค่าบริการ')[1]] if data[index][start] else ''
                elif i == 16:
                    data2['หักค่ากระดาษเสียให้ฟรีกับผู้เช่า'] = \
                    [data[index][start].split('หักค่ากระดาษเสียให้ฟรีกับผู้เช่า')[1].split('%')[0].strip() + " %"] if data[index][start] else ''
                elif i == 17:
                    data2['ค่าเงินประกันความเสียหาย'] = \
                    [data[index][start].split('ค่าเงินประกันความเสียหาย')[1].split('บาท')[0].strip()] if data[index][start] else ''
                print(lst_content[i], ':', data[index][start].strip()) if data[index][start] else ''
                temp = start
                start += 1
                break
            else:
                # pass
                # print(f"{detail} : ไม่พบข้อมูล")
                # print(data[index][start].strip())
                start += 1
        start = temp
    df = pd.DataFrame(data2)
    print(data2)
    print(df)
    print('\n')
    return df


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
# for i in range(4):
#     i = 3
#     file = open(f"file/copy{i+1}.txt", "r")
#     lines.append(file.readlines())
#     file.close()
#     display(lines, i)

# for i in range(len(lines)):
#     print(i) if 'ค่าเช่าเครื่องเดือนละ' in lines[i] else None
#

file = open(f"file/copy{4}.txt", "r")
lines.append(file.readlines())
file.close()
df = display(lines, 0)

writer = pd.ExcelWriter('test' + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='FilterQuery', index=False)
writer.save()
