def predictSales(sales_data, features, target, test_size=0.3):
    """
    Predicts future sales based on the provided historical data.
    
    Parameters:
    -----------
    sales_data: pd.DataFrame
        DataFrame containing historical sales dta.
    features: list
        List of columns to use as features.
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
    pass


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