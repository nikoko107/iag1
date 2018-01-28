# Importer les librairies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn as sk

# Importer le dataset sans prendre la derniere colonne
datarat = pd.read_csv('ratings.csv')
X = datarat.iloc[:, :-2].values
y = datarat.iloc[:, -2].values

# Diviser le dataset entre le Training set et le Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


