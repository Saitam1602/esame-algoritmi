import pandas as pd

from sklearn.preprocessing import OrdinalEncoder


def multi_ordinal_encoder(df, ordinal_encoder):

    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

    for c in categorical_columns:
        df[[c]] = ordinal_encoder.fit_transform(df[[c]])

    return df


def get_best_correlation_columns(df, column, threshold=.5):
    correlation = df.corr()
    correlation_level = threshold
    correlation_price = correlation[column].abs().sort_values(ascending=False)
    correlation_columns = correlation_price[correlation_price >
                                            correlation_level].index[1:]
    return correlation_columns


def choose_columns(df, columns):
    df_new = pd.DataFrame()
    for c in columns:
        df_new[[c]] = df[[c]]
    return df_new

def get_best_column_list():
    return ['OverallQual', 'GrLivArea', 'GarageCars', 'ExterQual', 'GarageArea',
       'TotalBsmtSF', '1stFlrSF', 'BsmtQual', 'KitchenQual', 'FullBath',
       'TotRmsAbvGrd', 'YearBuilt', 'YearRemodAdd']
