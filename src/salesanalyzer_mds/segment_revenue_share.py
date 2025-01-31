import pandas as pd


def segment_revenue_share(sales_data: pd.DataFrame,
                          price_col: str = 'UnitPrice',
                          quantity_col: str = 'Quantity',
                          price_thresholds: tuple = None) -> pd.DataFrame:
    """
    Segments products into three categories—cheap, medium, and expensive—
    based on price and calculates their respective share in total revenue.

    Parameters:
    -----------
    sales_data : pd.DataFrame
        DataFrame containing historical sales data.
    price_col : str
        Column containing product prices. Default is 'UnitPrice'.
    quantity_col : str
        Column containing quantities sold. Default is 'Quantity'.
    price_thresholds : tuple, optional
        User-defined price thresholds (cheap_threshold, expensive_threshold).
        If None, quantiles (0.33, 0.67) are used.

    Returns:
    --------
    pd.DataFrame
        A DataFrame showing the total revenue share for each price segment:
        'cheap', 'medium', 'expensive'.

    Raises:
    -------
    ValueError:
        If the input DataFrame is empty or specified columns contain missing data.
    KeyError:
        If any of the specified columns are missing in the DataFrame.
    TypeError:
        If any of the columns contain invalid data types.
    """

    # Check if input dataframe is empty
    if sales_data.empty:
        raise ValueError("Input DataFrame is empty.")

    # Check if required columns exist
    required_columns = {price_col, quantity_col}
    missing_columns = required_columns - set(sales_data.columns)
    if missing_columns:
        raise KeyError(f"Missing columns in input DataFrame: {missing_columns}")

    # Check for missing values
    if sales_data[price_col].isna().any() or sales_data[quantity_col].isna().any():
        raise ValueError(f"{price_col} or {quantity_col} column contains missing values.")

    # Check for valid numeric types
    if not pd.api.types.is_numeric_dtype(sales_data[price_col]):
        raise TypeError(f"{price_col} must contain numeric data.")
    if not pd.api.types.is_numeric_dtype(sales_data[quantity_col]):
        raise TypeError(f"{quantity_col} must contain numeric data.")

    # Calculate revenue as price * quantity
    sales_data = sales_data.assign(
        Revenue=sales_data[price_col] * sales_data[quantity_col]
        )

    # Determine price price_thresholds
    if price_thresholds is not None:
        cheap_threshold, expensive_threshold = price_thresholds
    else:
        sorted_prices = sales_data[price_col].sort_values()
        cheap_threshold = sorted_prices.quantile(0.33)
        expensive_threshold = sorted_prices.quantile(0.67)

    # Categorize prices based on price_thresholds
    def categorize_price(price):
        if price <= cheap_threshold:
            return 'cheap'
        elif price <= expensive_threshold:
            return 'medium'
        else:
            return 'expensive'

    sales_data = sales_data.assign(
        PriceSegment=sales_data[price_col].apply(categorize_price)
        )

    # Calculate revenue share for each segment
    revenue_share = (
        sales_data.groupby('PriceSegment')['Revenue']
        .sum()
        .reset_index()
        .rename(columns={'Revenue': 'TotalRevenue'})
    )

    total_revenue = revenue_share['TotalRevenue'].sum()

    # Prevent division by zero
    revenue_share['RevenueShare (%)'] = (
        ((revenue_share['TotalRevenue'] / total_revenue)
         * 100 if total_revenue > 0 else 0.0)
    )

    # Round values for better readability
    revenue_share = revenue_share.round({'TotalRevenue': 2,
                                         'RevenueShare (%)': 2})

    # Ensure all segments are included, even if they have zero revenue
    segment_order = ['cheap', 'medium', 'expensive']
    revenue_share = (revenue_share.set_index('PriceSegment')
                     .reindex(segment_order, fill_value=0)
                     .reset_index())

    return revenue_share
