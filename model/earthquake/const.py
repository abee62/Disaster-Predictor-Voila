from imblearn.over_sampling import SMOTE
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def getModelNames():
    modelNames = {'Logistic Regression': 'tsunamiLogisticRegressionModel','SVM':'tsunamiSVMModel', 'Naive Bayes': 'tsunamiNbModel'}
    return modelNames
def getMeanStd():
    tsunamiDf = pd.read_csv("D:\google_hackathon\earthquake_data.csv")
    del tsunamiDf['title']
    del tsunamiDf['location']
    del tsunamiDf['country']
    del tsunamiDf['continent']
    tsunamiDf["alert"] = tsunamiDf["alert"].fillna("red")
    tsunamiDf["date_time"] = pd.to_datetime(tsunamiDf["date_time"])
    tsunamiDf["date_time"] = pd.DatetimeIndex(tsunamiDf["date_time"]).month    
    le=LabelEncoder()
    tsunamiDf["alert"]=le.fit_transform(tsunamiDf["alert"])
    tsunamiDf["magType"]=le.fit_transform(tsunamiDf["magType"])
    tsunamiDf["net"]=le.fit_transform(tsunamiDf["net"])
    x = tsunamiDf.iloc[:, [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
    y = tsunamiDf.iloc[:, [5]]
    s = SMOTE()
    x_data, y_data = s.fit_resample(x, y)
    tsunamiInputMean = []
    for columns in x_data.columns:
        tsunamiInputMean.append(x_data[columns].mean())
    tsunamiInputStd = []
    for columns in x_data.columns:
        tsunamiInputStd.append(x_data[columns].std())
    return tsunamiInputMean, tsunamiInputStd