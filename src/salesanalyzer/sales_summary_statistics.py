import pandas as pd

def sales_summary_statistics(sales_data):
    """
    Generates a DataFrame with summary statistics for the sales data.
    
    The function calculates a variety of summary statistics that provide insights into overall sales performance,
    customer behavior, and product performance. The statistics include average order value, average customer lifetime value (CLV),
    average invoice value, total revenue, and more.
    
    Args:
        df (pd.DataFrame): The sales data with columns ['Description', 'Quantity', 'InvoiceNo'
                                        'InvoiceDate', 'UnitPrice', 'CustomerID'].
    
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
    if len(sales_data.index) == 0:
        return pd.DataFrame({
            'Average_Customer_Lifetime_Value': [None],
            'Total_Revenue': [0],
            'Total_Products_Sold': [0],
            'Unique_Customers': [0],
            'Top_Selling_Product_by_Quantity': [None],
            'Top_Selling_Product_by_Revenue': [None],
            'Average_Revenue_per_Customer': [None],
            'Return_Proportion': [None]
        })
    
    # Calculate the total revenue (sum of Quantity * UnitPrice)
    sales_data['Revenue'] = sales_data['Quantity'] * sales_data['UnitPrice']
    
    # Calculate totals
    total_revenue = sales_data['Revenue'].sum()
    total_products_sold = sales_data['Quantity'].sum()
    unique_customers = sales_data['CustomerID'].nunique()
    
    # Top Selling Product by Quantity (Most sold product)
    top_selling_product_by_qty = sales_data.groupby('Description')['Quantity'].sum().idxmax()
    
    # Top Selling Product by Revenue (Highest revenue generating product)
    top_selling_product_by_revenue = sales_data.groupby('Description')['Revenue'].sum().idxmax()
    
    # Average Revenue per Customer (Total Revenue / Unique Customers)
    average_revenue_per_customer = total_revenue / unique_customers
    
    # Customer Lifetime Value (CLV) - In this context, we use total revenue per unique customer
    # assuming each customer contributes equally to CLV.
    clv = total_revenue / unique_customers
    
    # Return Proportion - Assuming returns are represented by negative quantities
    # Add a return flag: return sales data with negative quantities
    returns_data = sales_data[sales_data['Quantity'] < 0]
    return_proportion = len(returns_data) / len(sales_data) if len(sales_data) > 0 else 0
    
    # Prepare summary statistics DataFrame
    summary_statistics = {
        'Average_Customer_Lifetime_Value': [clv],
        'Total_Revenue': [total_revenue],
        'Total_Products_Sold': [total_products_sold],
        'Unique_Customers': [unique_customers],
        'Top_Selling_Product_by_Quantity': [top_selling_product_by_qty],
        'Top_Selling_Product_by_Revenue': [top_selling_product_by_revenue],
        'Average_Revenue_per_Customer': [average_revenue_per_customer],
        'Return_Proportion': [return_proportion]
    }

    # Average Order Value (Total Revenue / Number of Orders)
    if 'InvoiceNo' in sales_data.columns:
        average_order_value = sales_data.groupby('InvoiceNo')['Revenue'].sum().mean()
        summary_statistics['Average_Order_Value'] = average_order_value
    
    return pd.DataFrame(summary_statistics)