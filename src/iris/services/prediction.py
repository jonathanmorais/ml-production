import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from .interfaces import IClassify, ILabel, ITrainning

class Label(ILabel):
    def get_label(x):
        if x == 0:
            return 'setosa'
        elif x == 1:
            return 'versicolor'
        else:
            return 'virginica'

class Trainnig(ITrainning):
    def model_trainning(raw_features):
        label = Label
        iris = load_iris()
        X = iris.data
        y = iris.target

        pd_iris = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

        pd_iris['target'] = pd_iris['target'].apply(label.get_label)

        # split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.5)

        # build the model
        clf = RandomForestClassifier(n_estimators=10)

        # train the classifier
        clf.fit(X_train, y_train)

        return clf

class ClassIris(IClassify,Trainnig):
    def classify_iris(features: dict):
        label = Label
        t = Trainnig().model_trainning()
        raw_features = [features['sepal_l'], features['sepal_w'], features['petal_l'], features['petal_w']]
        prediction =  t.predict_proba([raw_features])
        return {'class': label.get_label([np.argmax(prediction)]), 'probability': round(max(prediction[0]), 2)}