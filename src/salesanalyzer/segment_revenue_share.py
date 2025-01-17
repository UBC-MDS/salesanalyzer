import pandas as pd


def segment_revenue_share(sales_data,
                          price_col='UnitPrice',
                          quantity_col='Quantity'):
    """
    Segments products into three categories—cheap, medium, and expensive—
    based on price, and calculates their respective share in total revenue.

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

    Raises:
    -------
    ValueError:
        If the input DataFrame is empty or specified columns contain
        any missing data
    KeyError:
        If any of the specified columns are missing in the DataFrame.
    TypeError:
        If any of the columns contain invalid data types.
    """
    # Check if input dataframe is empty
    if sales_data.empty:
        raise ValueError("Input DataFrame is empty.")

    # Check if required columns are missing
    required_columns = {price_col, quantity_col}
    missing_columns = required_columns - set(sales_data.columns)
    if missing_columns:
        raise KeyError(f"Missing columns in input DataFrame: {missing_columns}")

    # Check if required columns contain any missing data
    if sales_data[price_col].isna().any() or sales_data[quantity_col].isna().any():
        raise ValueError(f"{price_col} or {quantity_col} column contains missing values.")

    # Check if invalid data types are present in required columns
    if not pd.api.types.is_numeric_dtype(sales_data[price_col]):
        raise TypeError(f"{price_col} must contain numeric data.")
    if not pd.api.types.is_numeric_dtype(sales_data[quantity_col]):
        raise TypeError(f"{quantity_col} must contain numeric data.")

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
