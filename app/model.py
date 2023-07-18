import h2o
from h2o.automl import H2OAutoML

h2o.init()
saved_model = h2o.import_mojo('D:/education/misis/sem2/practice/misis_practice_i-4/app/StackedEnsemble_BestOfFamily_4_AutoML_5_20230717_164905.zip')

def prediction(df):
    dataframe = h2o.H2OFrame(df)
    prediction = saved_model.predict(dataframe)
    print(prediction)
    return prediction