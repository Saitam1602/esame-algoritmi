import pandas as pd
import pickle

from data.make_dataset import load_data
from features.build_features import get_best_column_list, multi_ordinal_encoder, choose_columns
from sklearn.preprocessing import OrdinalEncoder


# Preprocessing
print("Preprocessing")
path = "../data/raw/test.csv"
df = load_data(path)

# print(df['MSZoning'].unique())
print(df.isna().sum().values)
print(df.isna().sum()[20:])
print(df.GarageCars.unique())
print(df.GarageCars.mode())
exit()

# Encoding
print("Encoding")
oe = OrdinalEncoder()
df = multi_ordinal_encoder(df, oe)

# Colonne migliori, le colonne restituite erano state calcolate nel file del training dei modelli
print("Selezione colonne")
best_correlation_column = get_best_column_list()
X_test = choose_columns(df, best_correlation_column)

# Caricamento modelli
print("Caricamento Modelli")
decision_tree_model = pickle.load(
    open('models/models/decision_tree_regressor_model.sav', 'rb'))
random_forest_model = pickle.load(
    open('models/models/random_forest_regressor_model.sav', 'rb'))
ada_boost_model = pickle.load(
    open('models/models/ada_boost_regressor_model.sav', 'rb'))
xgboost_model = pickle.load(
    open('models/models/xgboost_regressor_model.sav', 'rb'))

# Predict
print("Predict")
predict_decision_tree = decision_tree_model.predict(X_test)
predict_random_forest = random_forest_model.predict(X_test)
predict_ada_boost = ada_boost_model.predict(X_test)
predict_xgboost = xgboost_model.predict(X_test)

# Dataframe per visualizzare
print("Creazione DataFrame")
df_ris = pd.DataFrame()
df_ris['predict_decision_tree'] = predict_decision_tree
df_ris['predict_random_forest'] = predict_random_forest
df_ris['predict_ada_boost'] = predict_ada_boost
df_ris['predict_xgboost'] = predict_xgboost

#Salvataggio risultati
print("Salvataggio")
output = "result.csv"
df_ris.to_csv(output)
