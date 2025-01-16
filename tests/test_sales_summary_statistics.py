from salesanalyzer.sales_summary_statistics import sales_summary_statistics
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'Quantity': [10, 5, 3, 15],
        'UnitPrice': [100, 200, 150, 100],
        'CustomerID': [1, 2, 1, 3],
        'InvoiceNo': ['INV001', 'INV002', 'INV003', 'INV004'],
        'Description': ['Product A', 'Product B', 'Product A', 'Product C']
    })

def test_empty_dataframe():
    # Edge case: Empty DataFrame
    empty_df = pd.DataFrame(columns=['Quantity', 'UnitPrice', 'CustomerID', 'InvoiceNo', 'Description'])
    result = sales_summary_statistics(empty_df)
    
    # Check if the result is an empty DataFrame
    pd.testing.assert_frame_equal(result, pd.DataFrame({}))

# Test 2: Test with normal data (all columns present)
def test_sales_summary_statistics_normal_data(sample_data):
    result = sales_summary_statistics(sample_data)
    
    expected = pd.DataFrame({
        'total_revenue': [3950],
        'unique_customers': [3],
        'average_order_value': [987.5],
        'top_selling_product_quantity': ['Product C'],
        'top_selling_product_revenue': ['Product C'],
        'average_revenue_per_customer': [1316.666667]
    })
    
    assert_frame_equal(result, expected, check_exact=False, check_like=True)