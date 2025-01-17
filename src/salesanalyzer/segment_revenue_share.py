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
    # Calculate revenue as price * quantity
    sales_data['Revenue'] = sales_data[price_col] * sales_data[quantity_col]

    # Sort the prices
    sorted_prices = sales_data[price_col].sort_values()

    # Calculate price thresholds for segmentation
    cheap_threshold = sorted_prices.quantile(0.33)
    expensive_threshold = sorted_prices.quantile(0.67)

    # Categorize prices by threshold
    sales_data['PriceSegment'] = sales_data[price_col].apply(
        lambda price: 'cheap' if price <= cheap_threshold else
                      'medium' if price <= expensive_threshold else
                      'expensive'
    )

    # Calculate revenue share for each segment
    revenue_share = (
        sales_data.groupby('PriceSegment')['Revenue']
        .sum()
        .reset_index()
        .rename(columns={'Revenue': 'TotalRevenue'})
    )
    total_revenue = revenue_share['TotalRevenue'].sum()
    revenue_share['RevenueShare (%)'] = (
        (revenue_share['TotalRevenue'] / total_revenue) * 100
        )

    return revenue_share


