
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

import pandas as pd


def make_prediction():

    # Load dataset
    df = pd.read_csv("data_model/diabetes_data.csv")

    X = df[["age", "sex", "bmi", "bp", "tc",
            "ldl", "hdl", "tch", "ltg", "glucose"]]
    Y = df['Result']

    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=1)

    model = linear_model.LinearRegression()
    # Training data is used always, we have now build our model
    model.fit(x_train, y_train)

    # Prediction of testset result of  the Prepared Model
    test = model.predict(x_test)  # we use test data to predict trained data
    # print(test)

    # Checking predictions acuracy by r2 Scores (value lies between 0 to 1)
    print(r2_score(y_test, test))

    #  Pickle model
    pd.to_pickle(model, "data_model/model.pickle")

    # Unpickle model
    model = pd.read_pickle("model.pickle")
