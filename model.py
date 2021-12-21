# importing modules

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier

def predict(weight, length, width):
    data = pd.read_csv('datasets/Fish.csv')

    X = data[['Weight', 'Length1', 'Width']]
    y = data.Species

    cat_cols = ['Species']  # categorical columns
    num_cols = ['Length1', 'Weight', 'Width']  # numerical columns

    numericalTransformer = SimpleImputer(strategy='most_frequent')

    OHencoder = OneHotEncoder(handle_unknown='ignore')

    preprocessor = ColumnTransformer(
        transformers=[
            ('imputer', numericalTransformer, num_cols)
        ]
    )

    clf = RandomForestClassifier(criterion='entropy', n_estimators=10, random_state=1)

    # making my pipeline for preprocessing and training

    my_pipeline = Pipeline(
        steps=[
            ('preprocessing', preprocessor),
            ('model', clf)
        ]
    )

    # training the model
    my_pipeline.fit(X, y)

    test_df = pd.DataFrame(np.array([weight, length, width]).reshape(1, 3), columns=
    ['Weight', 'Length1', 'Width'])


    return my_pipeline.predict(test_df)[0]

