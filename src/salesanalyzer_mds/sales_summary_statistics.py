import pandas as pd


def sales_summary_statistics(sales_data: pd.DataFrame, quantity_col: str = 'Quantity', price_col: str = 'UnitPrice',
                             customer_col: str = 'CustomerID', invoice_col: str = 'InvoiceNo',
                             description_col: str = 'Description') -> pd.DataFrame:
    """
    Generate summary statistics for sales data, including total revenue, unique customers, 
    average order value, top-selling products by quantity and revenue, and average revenue 
    per customer.

    Args:
    -----
        sales_data (pandas.DataFrame): A DataFrame containing sales data with at least 
                                       the following columns: quantity_col, price_col, 
                                       customer_col, invoice_col, and description_col. 
        quantity_col (str): The name of the column containing the quantity sold.
        price_col (str): The name of the column containing the unit price of the product.
        customer_col (str): The name of the column containing the customer ID.
        invoice_col (str): The name of the column containing the invoice number.
        description_col (str): The name of the column containing the product description.

    Returns:
    --------
        pandas.DataFrame: A DataFrame containing the calculated summary statistics. If 
                          no sales data is provided, returns an empty DataFrame.

    The function computes the following statistics:
    - 'total_revenue': The total revenue generated by all sales.
    - 'unique_customers': The number of unique customers.
    - 'average_order_value': The average value of an order (sum of revenue per invoice).
    - 'top_selling_product_quantity': The product with the highest quantity sold.
    - 'top_selling_product_revenue': The product with the highest total revenue.
    - 'average_revenue_per_customer': The average revenue generated by each customer.

    Example:
    --------
    >>> df = pd.DataFrame({
    >>>     'Quantity': [10, 5, 3, 15],
    >>>     'UnitPrice': [100, 200, 150, 100],
    >>>     'CustomerID': [1, 2, 1, 3],
    >>>     'InvoiceNo': ['INV001', 'INV002', 'INV003', 'INV004'],
    >>>     'Description': ['Product A', 'Product B', 'Product A', 'Product C']
    >>> })
    >>> summary_df = sales_summary_statistics(df)
    >>> print(summary_df)
    total_revenue  unique_customers  average_order_value  \
    0          3950.0                 3               987.5   

       top_selling_product_quantity top_selling_product_revenue  \
    0                Product C                Product C   

       average_revenue_per_customer  
    0                     1316.666667  
    """

    if not isinstance(sales_data, pd.DataFrame):
        raise ValueError("sales_data parameter should be a pandas DataFrame")

    # Check for missing or incorrect columns
    required_columns = [quantity_col, price_col,
                        customer_col, invoice_col, description_col]
    missing_columns = [
        col for col in required_columns if col not in sales_data.columns]
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}")

    if len(sales_data.index) == 0:
        return pd.DataFrame({})

    # Calculate revenue
    sales_data['Revenue'] = sales_data[quantity_col] * sales_data[price_col]
    sales_data['Revenue'].astype(float)

    # Calculate summary statistics
    unique_customers = sales_data[customer_col].nunique()
    total_revenue = sales_data['Revenue'].sum().astype(float)

    # Calculate top-selling products based on quantity
    top_selling_product_quantity = (
        sales_data.groupby(description_col)[quantity_col].sum())
    max_quantity = top_selling_product_quantity.max()
    top_selling_product_quantity = (
        top_selling_product_quantity[top_selling_product_quantity == max_quantity].index.tolist())

    # Calculate top-selling products based on revenue
    top_selling_product_revenue = (
        sales_data.groupby(description_col)['Revenue'].sum())
    max_revenue = top_selling_product_revenue.max()
    top_selling_product_revenue = (
        top_selling_product_revenue[top_selling_product_revenue == max_revenue].index.tolist())

    average_order_value = sales_data.groupby(
        invoice_col)['Revenue'].sum().mean()

    revenue_per_customer = sales_data.groupby(customer_col)['Revenue'].sum()
    average_revenue_per_customer = revenue_per_customer.mean()

    # Create summary statistics
    summary = {
        'total_revenue': [total_revenue],
        'unique_customers': [unique_customers],
        'average_order_value': [average_order_value],
        'top_selling_product_quantity': [', '.join(top_selling_product_quantity)],
        'top_selling_product_revenue': [', '.join(top_selling_product_revenue)],
        'average_revenue_per_customer': [average_revenue_per_customer]
    }

    # Transpose and rename the column
    summary_t = pd.DataFrame(summary).T.rename(columns={0: "Value"})

    return summary_t
