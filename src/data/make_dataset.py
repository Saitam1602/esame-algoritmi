import pandas as pd

def load_data(path):
    # Pulizia generale
    df = pd.read_csv(path)
    df.drop(["Utilities"], axis=1)
    df.drop(["Utilities"], axis=1)
    df.LotFrontage = df.LotFrontage.fillna(round(df.LotFrontage.mean(),1))
    df.Exterior1st = df.Exterior1st.dropna()
    df.Exterior2nd = df.Exterior2nd.dropna()
    df.MasVnrType = df.MasVnrType.dropna()
    df.MasVnrArea = df.MasVnrArea.fillna(round(df.MasVnrArea.mean(),1))
    df.BsmtQual = df.BsmtQual.fillna("No Basement") # nan in NA -> no basement
    df.BsmtCond = df.BsmtCond.fillna("No Basement")
    df.BsmtExposure = df.BsmtExposure.fillna("No Basement")
    df.BsmtFinType1 = df.BsmtFinType1.fillna("No Basement")
    df.BsmtFinType2 = df.BsmtFinType2.fillna("No Basement")
    df.BsmtFinSF1 = df.BsmtFinSF1.fillna("No Basement")
    df.BsmtFinSF2 = df.BsmtFinSF2.fillna("No Basement")
    df.BsmtUnfSF = df.BsmtUnfSF.fillna(round(df.BsmtUnfSF.mean(),1))
    df.TotalBsmtSF = df.TotalBsmtSF.fillna(round(df.TotalBsmtSF.mean(),1))
    df.BsmtFullBath = df.BsmtFullBath.dropna()
    df.BsmtHalfBath = df.BsmtHalfBath.dropna()
    df.KitchenQual = df.KitchenQual.dropna()
    df.Functional = df.Functional.dropna()
    df.Fireplaces = df.Fireplaces.fillna(0)
    df.FireplaceQu= df.FireplaceQu.fillna(0)
    df.GarageType = df.GarageType.fillna("No garage")
    df.GarageYrBlt = df.GarageYrBlt.fillna(df.GarageYrBlt.mean())
    df.GarageFinish = df.GarageFinish.fillna("No garage")
    df.GarageCars = df.GarageCars.dropna()
    df.GarageQual = df.GarageQual.fillna("No garage")
    df.GarageCond = df.GarageCond.fillna("No garage")
    df.PoolQC = df.PoolQC.fillna("No pool")
    df.Fence = df.Fence.fillna("No fence")
    df.MiscFeature = df.MiscFeature.fillna("none")
    df.SaleType = df.SaleType.dropna()

    # Outlier
    df.SalePrice.sort_values(ascending=False)

    to_remove = df[df.SalePrice > 730000].index
    df.drop(to_remove)

    return df