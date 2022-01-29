import pandas as pd
import xlsxwriter
import pathlib


def display(data, index):
    data2 = {}
    lst_content = ['วันที่', 'สัญญาเลขที่', 'สัญญาฉบับนี้ทำขึ้นระหว่าง', 'ผู้ให้เช่าตกลง', 'เครื่องรุ่น',
                   'หมายเลขเครื่อง', 'จำนวน', 'สถานที่ตั้ง', 'ตู้รองเครื่อง', 'สัญญานี้มีผลบังคับใช้เป็นเวลา',
                    'ค่าเช่าเครื่องเดือนละ', 'Fax', 'Printer','หักค่ากระดาษเสียให้ฟรีกับผู้เช่า', 'ค่าเงินประกันความเสียหาย']
    start = 0
    temp = 0
    stop = 40
    for i in range(len(lst_content)):
        while start < stop:
            if lst_content[i] in data[index][start]:
                if i == 0:
                    data2['วันที่ทำสัญญา'] = [data[index][start].replace('วันที่', '').strip()] if data[index][start] else ''
                elif i == 1:
                    data2['สัญญาเลขที่'] = [data[index][start].replace('สัญญาเลขที่', '').strip()] if data[index][start] else ''
                elif i == 2:
                    data2['ชื่อลูกค้า'] = [data[index][start].split('กับ')[1].split('ซึ่งต่อไปนี้ในสัญญานี้จะเรียกว่า')[0].split('ตั้งอยู่เลขที่')[0]] if data[index][start] else ''
                    data2['ที่อยู่ออกบิล'] = [
                        data[index][start].split('กับ')[1].split('ซึ่งต่อไปนี้ในสัญญานี้จะเรียกว่า')[0].split(
                            'ตั้งอยู่เลขที่')[1]] if data[index][start] else ''
                elif i == 3:
                    data2['ผู้ให้เช่าตกลง'] = [data[index][start].split('จำนวน')[1].replace('เครื่อง', '').strip()] if data[index][start] else ''
                elif i == 4:
                    data2['เครื่องรุ่น'] = [data[index][start].split(':')[1].strip()] if data[index][start] else ''
                elif i == 5:
                    data2['หมายเลขเครื่อง'] = [data[index][start].split(':')[1].strip()] if 'หมายเลขเครื่อง' in data[index][start] else ''
                elif i == 6:
                    data2['จำนวน'] = [int(data[index][start].split(':')[1].strip())] if data[index][start] else ''
                elif i == 7:
                    data2['สถานที่ตั้ง'] = [data[index][start].split(':')[1].strip()] if data[index][start] else ''
                elif i == 8:
                    data2['ตู้รองเครื่อง'] = [data[index][start].split('จำนวน')[1].split('ตู้')[0].strip()] if data[index][start] else ''
                elif i == 9:
                    data2['ระยะเวลา'] = [data[index][start].split('เวลา')[1].split('จนถึง')[0].split('ตั้งแต่')[0].strip()] if data[index][start] else ''
                    data2['ตั้งแต่'] = [data[index][start].split('เวลา')[1].split('จนถึง')[0].split('ตั้งแต่')[1].replace('วันที่','').strip()] if data[index][start] else ''
                    data2['จนถึง'] = [data[index][start].split('เวลา')[1].split('จนถึง')[1].replace('วันที่','').strip()] if data[index][start] else ''
                elif i == 10:
                    data2['ค่าเช่าเครื่องเดือนละ'] = [data[index][start].split('ค่าเช่าเครื่องเดือนละ')[1].strip()] if data[index][start] else ['ไม่มีค่าเข่ารายเดือน']
                elif i == 11:
                    data2['Fax'] = [data[index][start].split('=')[1].replace('บาท / เดือน','').strip()] if data[index][start] else ''
                elif i == 12:
                    data2['Printer'] = [data[index][start].split('=')[1].replace('บาท / เดือน','').strip()] if data[index][start] else ''
                elif i == 13:
                    data2['หักค่ากระดาษเสียให้ฟรีกับผู้เช่า'] = \
                    [data[index][start].split('หักค่ากระดาษเสียให้ฟรีกับผู้เช่า')[1].split('%')[0].strip() + " "] if data[index][start] else ''
                elif i == 14:
                    data2['ค่าเงินประกันความเสียหาย'] = \
                    [data[index][start].split('ค่าเงินประกันความเสียหาย')[1].split('บาท')[0].strip()] if data[index][start] else ''

                temp = start
                start += 1
                break
            else:
                start += 1
        start = temp
    df = pd.DataFrame(data2)
    return df


Merge = []
def open_add(num):
    lines = []
    file = open(f"file/copy{num}.txt", "r")
    lines.append(file.readlines())
    file.close()
    df = display(lines, 0)
    Merge.append(df)


def write_Excel(df):
    writer = pd.ExcelWriter(f'final' + '.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='FilterQuery', index=False)
    writer.save()



initial_count = 0
for path in pathlib.Path("./file").iterdir():
    if path.is_file():
        initial_count += 1

for j in range(1,((initial_count-1)//2)+1):
    open_add(j)

save = pd.concat(Merge,ignore_index=True)

write_Excel(save)
