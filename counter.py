class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def countLeapYears(d):
    years = d.y
    if (d.m <= 2):
        years -= 1
    return int(years / 4) - int(years / 100) + int(years / 400)

def getDifference(dt1, dt2):
    n1 = dt1.y * 365 + dt1.d
    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]
    n1 += countLeapYears(dt1)
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)
    return (n2 - n1)
    
def days(c_date):
    c_date = c_date.split('-')
    dt1 = Date(1, 1, 2000)
    dt2 = Date(int(c_date[2]), int(c_date[1]), int(c_date[0]))
    return getDifference(dt1, dt2)+1


# reading the CSV file 

import pandas as pd  

def change(dataset):
    data = pd.read_csv("dataset/"+dataset+".csv")
    for i in range(len(data.index)):
        data.loc[i,'Date'] = days(data.loc[i,'Date'])
        print(data.loc[i,'Date'])
    data.to_csv("dataset/"+dataset+".csv", index=False)

def remove(dataset):
    data = pd.read_csv("dataset/"+dataset+".csv")
    for i in range(len(data.index)):
        if data.loc[i,'Date'] < 2500:
            data = data.drop([i], axis = 0)
    data.to_csv("dataset/"+dataset+".csv", index=False)


# remove('')

#join() method combines all contents of 
# csvfile.csv and formed as a string 
# text = ''.join([i for i in text]) 

# # search and replace the contents 
# text = text.replace("EmployeeName", "EmpName") 
# text = text.replace("EmployeeNumber", "EmpNumber") 
# text = text.replace("EmployeeDepartment", "EmpDepartment") 
# text = text.replace("lined", "linked")

# # output.csv is the output file opened in write mode 
# x = open("output.csv","w") 

# # all the replaced text is written in the output.csv file 
# x.writelines(text) 
# x.close()
