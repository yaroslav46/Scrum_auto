from openpyxl import load_workbook 
def get_info():
    wb = load_workbook("input.xlsx")
    sheet = wb.active 
    i=1 
    info =[]
    for cell in sheet['A']:
        
        i+=1
        info.append({
        'name': sheet[f'A{i}'].value,
        'Work': sheet[f'C{i}'].value,
        'date': sheet[f'D{i}'].value,
        'info_field': sheet[f'E{i}'].value
        })
    return  info
    