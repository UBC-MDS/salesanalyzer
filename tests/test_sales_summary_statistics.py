from salesanalyzer.sales_summary_statistics import sales_summary_statistics
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal


def test_sales_summary_statistics_empty():
    """
    Edge Case 1: Empty DataFrame (No sales data)
    """
    empty_df = pd.DataFrame(columns=['Description', 
                                     'Quantity', 'InvoiceDate', 'UnitPrice', 
                                     'CustomerID'])
    result = sales_summary_statistics(empty_df)
    expected_empty_result = pd.DataFrame({
        'Average_Customer_Lifetime_Value': [None],
        'Total_Revenue': [0],
        'Total_Products_Sold': [0],
        'Unique_Customers': [0],
        'Top_Selling_Product_by_Quantity': [None],
        'Top_Selling_Product_by_Revenue': [None],
        'Average_Revenue_per_Customer': [None],
        'Return_Proportion': [None]
    })

    assert_frame_equal(result, expected_empty_result, check_like=True)

def test_sales_summary_statistics_single():
    """
    Edge Case 2: Single row of sales data
    """
    single_row_df = pd.DataFrame({
        'InvoiceNo': [123],
        'Description': ['Test Product'],
        'Quantity': [1],
        'InvoiceDate': ['2025-01-01'],
        'UnitPrice': [10.0],
        'CustomerID': [123]
    })
    result = sales_summary_statistics(single_row_df)
    expected_single_row_result = pd.DataFrame({
        'Average_Customer_Lifetime_Value': [10.0],
        'Total_Revenue': [10.0],
        'Total_Products_Sold': [1],
        'Unique_Customers': [1],
        'Top_Selling_Product_by_Quantity': ['Test Product'],
        'Top_Selling_Product_by_Revenue': ['Test Product'],
        'Average_Revenue_per_Customer': [10.0],
        'Return_Proportion': [0.0],
        'Average_Order_Value': [10.0]
    })
    assert_frame_equal(result, expected_single_row_result, check_like=True)

