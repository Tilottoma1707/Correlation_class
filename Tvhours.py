import plotly.express as px
import csv
import numpy as np
with open("TvandHours.csv")as f:
    df = csv.DictReader(f)

    #fig = px.scatter(df,x="\tAverage time spent watching TV in a week (hours)", y="Size of TV")
    #fig.show()

def getDataSource():
    size = []
    timeSpent = []

    with open("TvandHours.csv")as f:
        df = csv.DictReader(f)
        for i in df:
            size.append(float(i["Size of TV"]))
            timeSpent.append(float(i["\tAverage time spent watching TV in a week (hours)"]))
    return{"x":size,"y":timeSpent}
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation value is", correlation[0,1])
def setup():
    datasource = getDataSource()
    findCorrelation(datasource)
setup()
