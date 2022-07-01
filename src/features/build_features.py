import pandas as pd

from sklearn.preprocessing import OrdinalEncoder


def encode_categorical_data(df):
    oe = OrdinalEncoder()

    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

    for c in categorical_columns:
        df[[c]] = oe.fit_transform(df[[c]])

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
