import pandas as pd

def load_data(path):
    # Pulizia generale
    df = pd.read_csv(path)
    df = df.drop(["Utilities"], axis=1)
    df.Alley = df.Alley.fillna("No alley access")
    df.LotFrontage = df.LotFrontage.fillna(round(df.LotFrontage.mean(),1))
    df.Exterior1st = df.Exterior1st.fillna("Other")
    df.Exterior2nd = df.Exterior2nd.fillna("Other")
    df.MasVnrType = df.MasVnrType.fillna("None")
    df.MasVnrArea = df.MasVnrArea.fillna(round(df.MasVnrArea.mean(),1))
    df.MSZoning = df.MSZoning.fillna("No info")
    df.BsmtQual = df.BsmtQual.fillna("No Basement") 
    df.BsmtCond = df.BsmtCond.fillna("No Basement")
    df.BsmtExposure = df.BsmtExposure.fillna("No Basement")
    df.BsmtFinType1 = df.BsmtFinType1.fillna("No Basement")
    df.BsmtFinType2 = df.BsmtFinType2.fillna("No Basement")
    df.BsmtFinSF1 = df.BsmtFinSF1.fillna(round(df.BsmtFinSF1.mean(),1))
    df.BsmtFinSF2 = df.BsmtFinSF2.fillna(round(df.BsmtFinSF2.mean(),1))
    df.BsmtUnfSF = df.BsmtUnfSF.fillna(round(df.BsmtUnfSF.mean(),1))
    df.TotalBsmtSF = df.TotalBsmtSF.fillna(round(df.TotalBsmtSF.mean(),1))
    df.BsmtFullBath = df.BsmtFullBath.fillna(1)
    df.BsmtHalfBath = df.BsmtHalfBath.fillna(0)
    df.KitchenQual = df.KitchenQual.fillna("TA")
    df.Functional = df.Functional.fillna("Typ")
    df.Fireplaces = df.Fireplaces.fillna(0)
    df.FireplaceQu= df.FireplaceQu.fillna("No Fireplace")
    df.GarageArea = df.GarageArea.fillna(round(df.GarageArea.mean(),1))
    df.GarageType = df.GarageType.fillna("No garage")
    df.GarageYrBlt = df.GarageYrBlt.fillna(df.GarageYrBlt.mean())
    df.GarageFinish = df.GarageFinish.fillna("No garage")
    df.GarageCars = df.GarageCars.fillna(2)
    df.GarageQual = df.GarageQual.fillna("No garage")
    df.GarageCond = df.GarageCond.fillna("No garage")
    df.PoolQC = df.PoolQC.fillna("No pool")
    df.Fence = df.Fence.fillna("No fence")
    df.MiscFeature = df.MiscFeature.fillna("none")
    df.SaleType = df.SaleType.fillna("No info")

    # Outlier
    if 'SalePrice' in df.columns.tolist():
        df.SalePrice.sort_values(ascending=False)

        to_remove = df[df.SalePrice > 730000].index
        df = df.drop(to_remove)

    return df