import csv

def getList(nomalization=False):
    list = []

    fileName = 'xy.csv'
    if nomalization:
        fileName = 'xy_normalization.csv'
    
    with open(fileName, newline='', encoding='utf-8-sig') as csvfile:
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
