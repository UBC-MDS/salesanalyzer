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
