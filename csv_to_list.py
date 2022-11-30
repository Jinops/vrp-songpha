import csv

def getList():
    list = []
    
    with open('xy.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar=' ')
        for row in reader:
            data_list = []
            for column in row:
                data_list.append(int(column))
            list.append(data_list)

    return list
    
def printList(list):
    print("x = [%s]" %','.join(list[0]))
    print("y = [%s]" %','.join(list[1]))
