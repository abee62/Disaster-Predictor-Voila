# Saftey Net - A Natural Disaster Guide
This a voila App aimed at predicting natural disasters before they occur. In the first version, this predicts the possibility of occurance of Tsunami in the event of an Earthquake.The app aslo contains real time weather  forecast data visualization, news related to natural disasters around the world. 

## Target users
1. The common man - to browse through news, visualize weather forecasts
2. Tsunami predicting centers who have access to earthquake details when it occurs. Or anyone with access to earthquake information.

## File Structure
* notebook - contains the jupyter notebook required to run the app 
* model - this contains the models that are used to predict the natural disaster 
* app - runs on the voila framework and utilizes the stored results from the model to predict the event 
* tests - contains the unit tests

## Working 
- The model is trained on earthquake dataset obtained from kaggle. The dataset is trained on mutiple models and the models are stored using pickle
- Voila App lets the user select a model and for their input parameters, fetches the results using the stored model. It predicts whether Tsunami can occure due to the Earthquake.
- The App contains a Weather Visualizer section where the user can select a location, and it displays comaprison plot between the weather forecast of rainfall and humidity for that location. It helps the user visalize how the weather parameters are changing and what the upcoming weather is. This data is obtained using open weather api. We can add more locations and more weather parameters to these plots.
- There is a News section that displays headlines and links to the top 100 news related to natural disasters. This helps the user remain aware and get an idea of what is happening around the world and take necessary precautions. We get the news from news api

## Models used
1. Logistic Regression Model - Accuracy : 81.77
2. SVM Model - Accuracy : 84.375
3. Naive Bayes - Accuracy : 81.77
4. Ensemble : 82.81

k-fold cross-validation technique is used to cross validate the Ensemble model. It gives a cross validation score of 82.32

## Running the App
Go to 'app' directory. Type 'voila' in the terminal. It will show you the notebook you want to run. Click on that, and you can see the App.

## Demo

[Demo](https://drive.google.com/file/d/115xplxifkFG-V30P6KZ36MdEcgMrfN2K/view?usp=sharing)


https://github.com/abee62/Disaster-Predictor-Voila/assets/62689173/83714ade-ef21-471c-8b83-3c9160853f25


Press play to see the video


## App features
![4](https://github.com/abee62/Disaster-Predictor-Voila/assets/62689173/64e57325-8960-4cde-9cef-f66bdb2d1d8a)
![5](https://github.com/abee62/Disaster-Predictor-Voila/assets/62689173/71b945b1-772e-48b4-a1aa-f3fc0bfcf720)
![6](https://github.com/abee62/Disaster-Predictor-Voila/assets/62689173/1ed0d418-8a9c-4107-a81b-790e35aef2e3)
![7](https://github.com/abee62/Disaster-Predictor-Voila/assets/62689173/1a73e8af-ca83-4ace-9c7f-d66a8e445b24)



## Further scope
- We can recommend shelters, escape plan and helpline numbers based on the location where tsunami is triggered.
- Feature to predict more natural disasters. It proved difficult to find reliable data, so look more into that.
- User login and provide custom recommentaions based on their location.

Note: Due to time limitation, some of the paths in the code are absolute paths. Kindly change according to your local system
