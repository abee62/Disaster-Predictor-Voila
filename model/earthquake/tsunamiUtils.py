from const import getMeanStd
tsunamiInputMean, tsunamiInputStd = getMeanStd()
import os

tsunamiModelAccuracy = {'Logistic Regression': 81.77, 'SVM': 84.37, 'Naive Bayes': 81.77, 'Ensemble': 82.81}

filepath = 'D:/google_hackathon/project/VoilaDisasterPredictor/model/earthquake'
import pickle
def getTsunamiLinearRegressionResult(modelName, month, cdi, mmi, alert, sig, net, nst, dmin, gap, magType, depth, latitude, longitude):
    modelNames = {'Logistic Regression': 'tsunamiLogisticRegressionModel.sav','SVM':'tsunamiSVMModel.sav', 'Naive Bayes': 'tsunamiNbModel.sav'}
    modelCalled = modelNames[modelName]
    pkl_file1 = open('D:/google_hackathon/project/VoilaDisasterPredictor/model/earthquake/alert_encoder.pkl', 'rb')
    pkl_file2 = open('D:/google_hackathon/project/VoilaDisasterPredictor/model/earthquake/magType_encoder.pkl', 'rb')
    pkl_file3 = open('D:/google_hackathon/project/VoilaDisasterPredictor/model/earthquake/net_encoder.pkl', 'rb')
    le_alert = pickle.load(pkl_file1)
    le_magType = pickle.load(pkl_file2)
    le_net = pickle.load(pkl_file3)
    pkl_file1.close()
    pkl_file2.close()
    pkl_file3.close()
    alert = le_alert.transform([alert])[0]
    magType = le_magType.transform([magType])[0]
    net = le_net.transform([net])[0]
    
    #maginitude = (maginitude - tsunamiInputMean[0]) / tsunamiInputStd[0]
    month = (month - tsunamiInputMean[0]) / tsunamiInputStd[0]
    cdi = (cdi - tsunamiInputMean[1]) / tsunamiInputStd[1]
    mmi = (mmi - tsunamiInputMean[2]) / tsunamiInputStd[2]
    alert = (alert - tsunamiInputMean[3]) / tsunamiInputStd[3]
    sig = (sig - tsunamiInputMean[4]) / tsunamiInputStd[4]
    net = (net - tsunamiInputMean[5]) / tsunamiInputStd[5]
    nst = (nst - tsunamiInputMean[6]) / tsunamiInputStd[6]
    dmin = (dmin - tsunamiInputMean[7]) / tsunamiInputStd[7]
    gap = (gap - tsunamiInputMean[8]) / tsunamiInputStd[8]
    magType = (magType - tsunamiInputMean[9]) / tsunamiInputStd[9]
    depth = (depth - tsunamiInputMean[10]) / tsunamiInputStd[10]
    latitude = (latitude - tsunamiInputMean[11]) / tsunamiInputStd[11]
    longitude = (longitude - tsunamiInputMean[12]) / tsunamiInputStd[12]
    
    filename = 'D:/google_hackathon/project/VoilaDisasterPredictor/model/earthquake/'+modelCalled
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict([[ month, cdi, mmi, alert, sig, net, nst, dmin, gap, magType, depth, latitude, longitude]])
    #result = loaded_model.predict([[1,0,0,0,0,0,0,0,0,0,0,0,0]])

    return result[0], tsunamiModelAccuracy[modelName]
