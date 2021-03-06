import pandas as pd 
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import mean_squared_error
import numpy as np 


class Utils():
    def load_data(self, path):
        return pd.read_csv(path)

    #Función de validación
    def rmsle_cv(self, model, n_folds, train_ds, target):
        """Para las aproximaciones de regresión, cross_val_score añadiendo una línea de codigo que mezcle los datos """
        kf = KFold(n_folds, shuffle=True, random_state=0).get_n_splits(train_ds.values) #Línea de codigo que mezcla los datos
        rmse= np.sqrt(-cross_val_score(model, 
                                    train_ds.values, 
                                    target, 
                                    scoring="neg_mean_squared_error", 
                                    cv = kf))
        return(rmse)

    def rmsle(self, y, y_pred):
        return np.sqrt(mean_squared_error(y, y_pred))

    def make_sub(self, prediction, index):
        sub = pd.DataFrame()
        sub['Id'] = index
        sub['SalePrice'] = np.expm1(prediction)

        return sub