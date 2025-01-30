import pandas as pd
from pandas.api.types import is_numeric_dtype
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def predict_sales(sales_data, new_data, numeric_features, categorical_features, target, date_feature=None, test_size=0.3):
    """
    Predicts future sales based on the provided historical data.
    
    Parameters:
    -----------
    sales_data: pd.DataFrame
        DataFrame containing historical sales data.
    new_data: pd.DataFrame
        DataFrame containing new data to predict on.
    numeric_features: list
        List of columns to use as features with numeric data type.
    categorical_features: list
        List of columns to use as features with character data type.
    target: str
        Name of the target column.
    date_feature: str
        Name of columns to use as features with datetime data type.
        Default: None
    test_size: float
        Proportion of data to be used for testing.
        Default value is 0.3
    
    Returns:
    --------
    pd.DataFrame:
        A data frame with prediction values, and a printed out MSE score.
    
    Examples:
    ---------
    >>> sales_data = pd.DataFrame({'name': ['laptop', 'monitor'], 'price': [100, 200], 'quantity': [2, 1]})
    >>> new_data = pd.DataFrame({'name': 'laptop', 'price' : 300})
    >>> numeric_features = ['price']
    >>> categorical_features = ['name']
    >>> target = 'quantity'
    >>> predict_sales(sales_data, new_data, numeric_features, categorical_features, target)
        MSE of the model: 1.02,
            Predicted values
        0   245.40
    """
    if not isinstance(sales_data, pd.DataFrame):
        raise ValueError("sales_data parameter should be a pandas DataFrame")
    
    if not isinstance(new_data, pd.DataFrame):
        raise ValueError("new_data parameter should be a pandas DataFrame")
    
    if not isinstance(numeric_features, list):
        raise ValueError("numeric features should be a list")
    
    if not isinstance(categorical_features, list):
        raise ValueError("categorical features should be a list")
    
    if not isinstance(target, str):
        raise ValueError("target should be a string")
    
    for column in numeric_features:
        if not is_numeric_dtype(sales_data[column]):
            raise TypeError("numeric_features should countain numeric data type only")
        
    sales_data = sales_data.dropna()
    
    if date_feature:
        if not isinstance(date_feature, str):
            raise ValueError("date features should be a string")
        sales_data["year"] = pd.to_datetime(sales_data[date_feature]).dt.year
        sales_data["month"] = pd.to_datetime(sales_data[date_feature]).dt.month
        sales_data["day"] = pd.to_datetime(sales_data[date_feature]).dt.day
        
        new_data["year"] = pd.to_datetime(new_data[date_feature]).dt.year
        new_data["month"] = pd.to_datetime(new_data[date_feature]).dt.month
        new_data["day"] = pd.to_datetime(new_data[date_feature]).dt.day
        numeric_features.extend(["year", "month", "day"])
    
    X = sales_data[numeric_features + categorical_features]
    y = sales_data[target]
    
    X_new = new_data[numeric_features + categorical_features]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=123)
    
    preprocessor = make_column_transformer(
        (OneHotEncoder(handle_unknown="ignore"), categorical_features),
        remainder='passthrough'
    )
    
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)
    X_new = preprocessor.transform(X_new)
    
    model = RandomForestRegressor(random_state=123)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    new_pred = model.predict(X_new)
    
    print("MSE of the model:", round(mse, 2))
    result = pd.DataFrame({
        "Predicted values": [round(value, 2) for value in new_pred]
    })
    
    return result