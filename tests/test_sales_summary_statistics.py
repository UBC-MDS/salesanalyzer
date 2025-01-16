from salesanalyzer.sales_summary_statistics import sales_summary_statistics
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal


def test_sales_summary_statistics():
    """
    Test function for sales_summary_statistics
    """
    # Edge Case 1: Empty DataFrame (No sales data)
    empty_df = pd.DataFrame(columns=['Description', 
                                     'Quantity', 'InvoiceDate', 'UnitPrice', 
                                     'CustomerID'])
    result = sales_summary_statistics(empty_df)
    expected_empty_result = pd.DataFrame({
        'Average Order Value': [None],
        'Average Customer Lifetime Value (CLV)': [None],
        'Average Invoice Value': [None],
        'Total Revenue': [0],
        'Total Products Sold': [0],
        'Unique Customers': [0],
        'Top Selling Product by Quantity': [None],
        'Top Selling Product by Revenue': [None],
        'Average Revenue per Customer': [None],
        'Return Proportion': [None]
    })

    assert_frame_equal(result, expected_empty_result)