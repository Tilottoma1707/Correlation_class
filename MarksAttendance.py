import plotly.express as px
import csv
import numpy as np

def getDataSource():
    Marks = []
    Attendance = []

    with open("MarksvsAttendance.csv")as f:
        df = csv.DictReader(f)
        for i in df:
            Marks.append(float(i["Marks In Percentage"]))
            Attendance.append(float(i["Days Present"]))
    return{"x":Marks,"y":Attendance}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])
def Setup():
    dataSource = getDataSource()
    findCorrelation(dataSource)
Setup()


