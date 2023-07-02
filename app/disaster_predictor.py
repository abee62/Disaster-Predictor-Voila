from ipywidgets import widgets
import datetime
import sys
import numpy as np                
import pandas as pd               ## data processing, dataset file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt   ## data visualization & graphical plotting
import seaborn as sns             ## to visualize random distributions
import plotly.express as px       ## data visualization & graphical plotting
import plotly.graph_objects as go ## data visualization & graphical plotting
import plotly.subplots as sp      ## data visualization & graphical plotting


sys.path.append('D:/google_hackathon/project/VoilaDisasterPredictor/model/earthquake')
from tsunamiUtils import getTsunamiLinearRegressionResult
tsunamiDf =pd.read_csv("D:\google_hackathon\earthquake_data.csv")
class disasterPredictorApp(object):
    def __init__(self):
        self._runDate = None
        self._tsunamiPredictionWidget = widgets.Output()
        self._weatherVisualizerWidget = widgets.Output()
        self._tsunamiPredictionInputWidget = widgets.Output()
        self._tsunamiPredictionOutputWidget = widgets.Output()
        self._tsunamiInfoWidget = widgets.Output()

    def getWidget(self):
        ''' This function returns the main widget of the app.
            The main tab consists of:
            1. tsunami Prediction 
            2. Weather Visualizer
            3. Tsunami Predictor
            4. Air Quality Predictor
        '''
        inputWidget = self.initInputWidget()
        resultWidget = self.initResultWidget()
        titleWidget = widgets.HTML(value='<h1>Disaster Predictor</h1>')
        mainWidget = widgets.VBox(
            children=[titleWidget, inputWidget, resultWidget])
        return mainWidget

    def initInputWidget(self):
        self._runDate = widgets.DatePicker(description='Run Date',
                                           value=datetime.date.today(),
                                           disabled=False,
                                           layout=widgets.Layout(width='50%')
                                           )

        runButton = widgets.Button(description='Run',
                                   disabled=False,
                                   icon='check',
                                   button_style='primary',
                                   width=widgets.Layout(width='40px')
                                   )
        inputWidget = widgets.HBox([self._runDate, runButton])
        return inputWidget

    def refreshTab(self):
        self._tsunamiPredictionWidget.children = [self._tsunamiPredictionInputWidget, self._tsunamiPredictionOutputWidget, self._tsunamiInfoWidget]
        self._resultTab.children = [
            self._tsunamiPredictionWidget, self._weatherVisualizerWidget]

    def initResultWidget(self):
        self._resultTab = widgets.Tab()
        self._resultTab.children = [
            self._tsunamiPredictionWidget, self._weatherVisualizerWidget]
        self._resultTab.set_title(0, 'Tsunami Prediction')
        self._resultTab.set_title(1, 'Weather Visualizer')
        try:
            self._weatherVisualizer()
            self._earthqaukePrediction()
        except Exception as e:
            print(e)
        return self._resultTab

    def updatetsunamiResults(self, button = None):
        result, accuracy = getTsunamiLinearRegressionResult(self.modelName.value,
             self.month.value, self.cdi.value, self.mmi.value, self.alert.value, self.sig.value, self.net.value, self.nst.value, self.dmin.value, self.gap.value, self.magType.value, self.depth.value, self.latitude.value, self.longitude.value)
        if result == 1:
            text = 'The earthquake will result in a Tsunami'
        else:
            text = 'The earthquake will not result in a Tsunami'
        children = [widgets.HTML(text)]
        bodytext  = 'The Accuracy score of this mode is ' + str(accuracy)
        children.append(widgets.HTML(bodytext))
        self._tsunamiPredictionOutputWidget = widgets.VBox(children=children)

        self.refreshTab()

    def dummy(self, button = None):
        
        self._tsunamiPredictionOutputWidget = widgets.HTML('stuid shit')
        self.refreshTab()

    def _earthqaukePrediction(self):
        children = [widgets.HTML(value='<h2>tsunami Prediction</h2>')]

        self.modelName = widgets.Dropdown(
            options=['Logistic Regression', 'SVM', 'Naive Bayes'],
            value='Logistic Regression',
            description='Model',
            disabled=False,
        )

        self.month = widgets.Dropdown(
            options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            value=11,
            description='Month:',
            disabled=False,
        )
        self.latitude = widgets.FloatText(
            value=-9.7963,
            min=-90,
            max=90,
            step=0.000001,
            description='Latitude:',
            disabled=False
        )
        self.longitude = widgets.FloatText(
            value=159.596,
            min=-180,
            max=180,
            step=0.000001,
            description='Longitude:',
            disabled=False
        )

        # maginitude = widgets.FloatText(
        #     value=2.5,
        #     min=0.0,
        #     max=12.0,
        #     step=0.1,
        #     description='Magnitude of tsunami:',
        #     style={'description_width': 'initial'},
        #     disabled=False
        # )
        tsunamiInputWidget = widgets.HBox([self.month, self.latitude, self.longitude])
        children.append(tsunamiInputWidget)
        self.cdi = widgets.FloatText(
            value=8,
            min=-2.0,
            max=15.0,
            step=0.1,
            description='Community Density Intensity (CDI):',
            style={'description_width': 'initial'},
            disabled=False
        )
        self.mmi = widgets.BoundedIntText(
            value=7,
            min=0,
            max=10,
            step=1,
            description='Modified Mercalli intensity scale:',
            style={'description_width': 'initial'},
            disabled=False
        )

        self.alert = widgets.Dropdown(
            options=['green', 'yellow', 'orange', 'red'],
            value='green',
            description='Alert:',
            disabled=False
        )
        self.net = widgets.Dropdown(
            options=['ak', 'at', 'ci', 'duputel', 'hv', 'nc', 'nn', 'official', 'pt',
       'us', 'uw'],
            value='us',
            description='Net:',
            disabled=False
        )
        self.nst = widgets.BoundedIntText(
            value=10,
            min=0,
            max=10,
            step=1,
            description='No. of seismic stations ',
            style={'description_width': 'initial'},
            disabled=False)

        self.dmin = widgets.FloatText(
            value=0.509,
            min=0.0000,
            max=12.0000,
            step=0.0001,
            description='Hori dist-epicenter to nearest station',
            disabled=False,
            style={'description_width': 'initial'}

        )
        self.gap = widgets.BoundedIntText(
            value=17,
            min=0,
            max=360,
            step=1,
            description='largest azimuthal gap (degree) ',
            style={'description_width': 'initial'},
            disabled=False)

        self.magType = widgets.Dropdown(
            options=['Mi', 'mb', 'md', 'ml', 'ms', 'mw', 'mwb', 'mwc', 'mww'],
            value='mww',
            description='mag type:',
            disabled=False,

        )
        self.depth = widgets.FloatText(
            value=14,
            min=0.000,
            max=1000.000,
            step=0.001,
            description='Depth',
            disabled=False

        )
        self.sig = widgets.BoundedIntText(
            value=768,
            min=0,
            max=1000,
            step=1,
            description='Significance',
            disabled=False

        )
        children.append(self.modelName)
        children.append(self.cdi)
        children.append(self.mmi)
        children.append(self.alert)
        children.append(self.sig)
        children.append(self.nst)
        children.append(self.dmin)
        children.append(self.gap)
        children.append(self.depth)
        children.append(self.magType)
        children.append(self.net)
        #children.append(maginitude)
        self._tsunamiPredictionOutputWidget = widgets.HTML(
            value='Results to be displayed')
        runButton = widgets.Button(description='Run')
        children.append(runButton)
        runButton.on_click(self.updatetsunamiResults)
        #runButton.on_click(self.dummy)
        self._tsunamiPredictionInputWidget = widgets.VBox(children=children)

        df = pd.DataFrame(dict(
            x = [1, 3, 2, 4],
            y = [1, 2, 3, 4]
        ))
        # out = widgets.Output()
        # with out:
        #     fig = go.FigureWidget()
        #     fig.add_scatter(y=[2, 1, 4, 3])
        #     #px.line(df, x="x", y="y", title="Unsorted Input") 
        #     fig.show()



        # out = widgets.Output()
        # with out:
        # out = widgets.Output()
        # with out:
        # fig = px.density_mapbox(tsunamiDf, lat='latitude', lon='longitude', z='magnitude', radius=6,
        #                     center=dict(lat=0, lon=200), zoom=0, mapbox_style="stamen-terrain")
        # fig.update_geos(fitbounds="locations")
        # fig.update_layout(autosize=False, width=760, height=450, showlegend=False,
        #                     title='Quakes by Country - Density Mapbox', title_x=0.5)
        
        fig = px.density_mapbox(tsunamiDf, lat='latitude', lon='longitude', z='magnitude', radius=6,
                            center=dict(lat=0, lon=200), zoom=0, mapbox_style="stamen-terrain")
        fig.update_geos(fitbounds="locations")
        
        out = go.FigureWidget(fig)
        tsunamiDetails = widgets.HTML('<h3> Some details about Earthquakes and Tsunamis</h3>')
        #self._tsunamiInfoWidget = widgets.VBox(children=[tsunamiDetails, out])
        self._tsunamiInfoWidget = out
        self._tsunamiPredictionWidget = widgets.VBox(
            children=[self._tsunamiPredictionInputWidget, self._tsunamiPredictionOutputWidget, self._tsunamiInfoWidget])
        self.refreshTab()

    def _weatherVisualizer(self):
        children = [widgets.HTML(value='<h2>Weather Visualizer</h2>')]

        self._weatherVisualizerWidget = widgets.VBox(children=children)
        self.refreshTab()
