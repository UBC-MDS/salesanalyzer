import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

def predictSales(sales_data, new_data, numeric_features, date_feature, categorical_features, target, test_size=0.3):
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
    date_feature: list
        List of columns to use as features with date data type.
    categorical_features: list
        List of columns to use as features with character data type.
    target: str
        Name of the target column.
    test_size: float
        Proportiona of data to be used for testing.
        Default value is 0.3
    
    Returns:
    --------
    dict:
        A dictionary with model performance and a prediction
    """
    
    if not isinstance(sales_data, pd.DataFrame):
        
        raise ValueError("data parameter should be a pandas DataFrame")
    sales_data = sales_data.dropna()
    if date_feature:
        sales_data["year"] = pd.to_datetime(sales_data[date_feature]).dt.year
        sales_data["month"] = pd.to_datetime(sales_data[date_feature]).dt.month
        sales_data["day"] = pd.to_datetime(sales_data[date_feature]).dt.day
        
        new_data["year"] = pd.to_datetime(new_data[date_feature]).dt.year
        new_data["month"] = pd.to_datetime(new_data[date_feature]).dt.month
        new_data["day"] = pd.to_datetime(new_data[date_feature]).dt.day
        numeric_features.extend(["year", "month", "day"])
    
    X = sales_data[numeric_features + categorical_features]
    y = sales_data[target]
    print('COLUMNS', X.columns.to_list)
    
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
    return {
        "MSE of the model": mse,
        "Preicted values": new_pred
    }


def sales_summary_statistics(sales_data):
    """
    Generates a DataFrame with summary statistics for the sales data.
    
    The function calculates a variety of summary statistics that provide insights into overall sales performance,
    customer behavior, and product performance. The statistics include average order value, average customer lifetime value (CLV),
    average invoice value, total revenue, and more.
    
    Args:
        df (pd.DataFrame): The sales data with columns ['InvoiceNo', 'StockCode', 'Description', 
                            'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'].
    
    Returns:
        pd.DataFrame: A DataFrame containing summary statistics, including:
            - 'Average Order Value'
            - 'Average Customer Lifetime Value (CLV)'
            - 'Average Invoice Value'
            - 'Total Revenue'
            - 'Total Products Sold'
            - 'Unique Customers'
            - 'Top Selling Product by Quantity'
            - 'Top Selling Product by Revenue'
            - 'Average Revenue per Customer'
            - 'Return Proportion (if applicable)'
    """
    pass


def segment_revenue_share(sales_data, price_col='UnitPrice', quantity_col='Quantity'):
    """
    Segments products into three categories—cheap, medium, and expensive—based 
    on price, and calculates their respective share in total revenue.

    Parameters:
    -----------
    sales_data : pd.DataFrame
        DataFrame containing historical sales data.
    price_col : str
        Column containing product prices. Default is 'UnitPrice'.
    quantity_col : str
        Column containing quantities sold. Default is 'Quantity'.

    Returns:
    --------
    pd.DataFrame
        A DataFrame showing the total revenue share for each price segment: 
        'cheap', 'medium', 'expensive'.
    """
    pass
