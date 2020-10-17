import csv
import matplotlib.pyplot as plt

def getAllDataSet():
    with open('data.csv', 'r', encoding="utf-8") as csvfile:
        rows = csv.reader(csvfile)
        data = []
        rawData = (list)(rows)
        
        i = 0
        # Get the index of column that we want to analyze
        indexesIWant = []
        for name in rawData[0]:
            if name == 'mon' or name == 'stay' or name == 'money' or name == 'dollar' or name == 'again' or name == 'recom' or name == 'nation' or name == 'age' or name == 'gender':
                indexesIWant.append(i)
            i = i+1
        
        ii = 0
        for i in range(1, len(rawData)):
            if rawData[i][indexesIWant[3]] != '.':
                data.append([])
                y = 0
                
                for index in indexesIWant:
                    data[ii].append(rawData[i][index])
                    #data[i-1][y] = rawData[i][index]
                    y = y+1
                ii = ii+1
        '''
        x = 0
        for row in rawData:
            if x != 0 and row[indexesIWant[3]] != '.':
                data.append([])
                y = 0
                for index in indexesIWant:
                    data[x-1].append([])
                    data[x-1][y] = row[index]
                    y = y+1
            x = x+1
            '''
    # Change string list to int list
    data_int = []
    for i in range(0, len(data)-1):
        data_int.append([])
        for ii in range(0, len(data[0])-1):
            data_int[i].append(int(data[i][ii]))
    return data_int

def getSubDataSet():

    with open('data.csv', 'r', encoding="utf-8") as csvfile:
        rows = csv.reader(csvfile)
        data = []
        rawData = (list)(rows)
        i = 0
        # Get the index of column that we want to analyze
        indexesIWant = []
        for name in rawData[0]:
            if name == 'mon' or name == 'stay' or name == 'money' or name == 'dollar' or name == 'again' or name == 'recom' or name == 'nation' or name == 'age' or name == 'gender':
                indexesIWant.append(i)
            i = i+1
        print(indexesIWant)
        x = 0
        for row in rawData:
            # Only get the data from the people who don't want to travel Taiwan again
            if row[indexesIWant[4]] == '2':
                data.append([])
                y = 0
                for index in indexesIWant:
                    data[x].append(row[index])
                    y = y+1
                x = x+1
    # Change string list to int list
    data_int = []
    for i in range(0, len(data)-1):
        data_int.append([])
        for ii in range(0, len(data[0])):
            data_int[i].append(int(data[i][ii]))
    print(data_int[0])
    return data_int

def countPeopleInMonth(subDatas, allDatas):
    countMonthInSub = [0,0,0,0,0,0,0,0,0,0,0,0]
    for data in subDatas:
        countMonthInSub[data[0]-1] = countMonthInSub[data[0]-1]+1
    
    countMonthInAll = [0,0,0,0,0,0,0,0,0,0,0,0]
    for data in allDatas:
        countMonthInAll[data[0]-1] = countMonthInAll[data[0]-1]+1

    countMonthRatio = []
    for i in range(0, len(countMonthInAll)):
        countMonthRatio.append(countMonthInSub[i]/countMonthInAll[i]*100)
    return (countMonthInSub, countMonthInAll, countMonthRatio)

def countNationFromData(subDatas):
    countNation = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for data in subDatas:
        if data[6] <= 3:
            countNation[data[6]-1] = countNation[data[6]-1]+1
        elif data[6] >= 50 and data[6] <= 57:
            countNation[data[6]-47] = countNation[data[6]-47]+1
        elif data[6] == 60:
            countNation[11] = countNation[11]+1
        elif data[6] == 71:
            countNation[12] = countNation[12]+1
        elif data[6] == 72:
            countNation[13] = countNation[13]+1
        elif data[6] == 80:
            countNation[14] = countNation[14]+1 
        elif data[6] == 95:
            countNation[15] = countNation[15]+1 
        elif data[6] == 90:
            countNation[16] = countNation[16]+1 
    return countNation

def countInAge(subDatas):
    age = [0,0,0,0,0,0,0]
    for data in subDatas:
        age[data[7]-1] = age[data[7]-1]+1
    return age

def countInGender(subDatas):
    age = [0,0]
    for data in subDatas:
        age[data[8]-1] = age[data[8]-1]+1
    return age

def start():  
    subDatas = getSubDataSet()
    allDatas = getAllDataSet()
    print(subDatas[0])
    (countMonthInSub, countMonthInAll, countMonthRatio) = countPeopleInMonth(subDatas, allDatas)
    countNation = countNationFromData(subDatas)
    countOfAge = countInAge(subDatas)
    countOfGender = countInGender(subDatas)

    nation = ['JP', 'CH', 'KR', 'SG', 'MY', 'ID', 'PH', 'TH',
     'VN', 'ST-Asia', 'IN', 'US', 'DE/UK/FR', 'EU', 'NZ/AU', 'ROC', 'Others']

    age = ['12~19', '20~29', '30~39', '40~49', '50~59', '60~69', '66~']

    gender = ['male', 'female']

    plt.plot(['1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12'], countMonthInSub)
    plt.xlabel('Month')
    plt.ylabel('Ratio * 100')
    plt.suptitle('People dont want to travel Taiwan again')
    plt.title('Count in month')
    plt.show()
    
    plt.plot(nation, countNation)
    plt.xlabel('Country')
    plt.ylabel('# of people')
    plt.title('Count in nation')
    plt.show()
    
    plt.bar(age, countOfAge)
    plt.xlabel('age')
    plt.ylabel('# of people')
    plt.title('Count in age')
    plt.show()
    plt.bar(gender, countOfGender)
    plt.xlabel('gender')
    plt.ylabel('# of people')
    plt.title('Count in gender')
    plt.show()

if __name__ == "__main__":
    start()