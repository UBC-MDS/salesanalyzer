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
    """
    Edge case: Empty DataFrame
    """
    empty_df = pd.DataFrame(columns=['Quantity', 'UnitPrice', 'CustomerID', 'InvoiceNo', 'Description'])
    result = sales_summary_statistics(empty_df)
    
    # Check if the result is an empty DataFrame
    pd.testing.assert_frame_equal(result, pd.DataFrame({}))

def test_sales_summary_statistics_normal_data(sample_data):
    """
    Test with normal data (all columns present)
    """
    result = sales_summary_statistics(sample_data)
    
    expected = pd.DataFrame({
        'total_revenue': [3950.0],
        'unique_customers': [3],
        'average_order_value': [987.5],
        'top_selling_product_quantity': ['Product C'],
        'top_selling_product_revenue': ['Product C'],
        'average_revenue_per_customer': [1316.666667]
    }).T.rename(columns={0: "Value"})
    
    assert_frame_equal(result, expected, check_exact=False, check_like=True)

def test_sales_summary_statistics_single_transaction(sample_data):
    """
    Test with a single transaction
    """
    single_transaction = sample_data.head(1).copy()
    
    result = sales_summary_statistics(single_transaction)
    
    # Single transaction: 
    expected = pd.DataFrame({
        'total_revenue': [1000.0],
        'unique_customers': [1],
        'average_order_value': [1000.0],
        'top_selling_product_quantity': ['Product A'],
        'top_selling_product_revenue': ['Product A'],
        'average_revenue_per_customer': [1000.0]
    }).T.rename(columns={0: "Value"})
    
    assert_frame_equal(result, expected, check_exact=False, check_like=True)


def test_sales_summary_statistics_invalid_input():
    """
    Test that the function raises a ValueError when input is not a pandas DataFrame
    """
    # Test with a list (not a DataFrame)
    with pytest.raises(ValueError, match="sales_data parameter should be a pandas DataFrame"):
        sales_summary_statistics([10, 5, 3, 15])  # List instead of DataFrame

    # Test with a dictionary (not a DataFrame)
    with pytest.raises(ValueError, match="sales_data parameter should be a pandas DataFrame"):
        sales_summary_statistics({'Quantity': [10, 5, 3, 15]})  # Dictionary instead of DataFrame
    
    # Test with None (not a DataFrame)
    with pytest.raises(ValueError, match="sales_data parameter should be a pandas DataFrame"):
        sales_summary_statistics(None)  # None instead of DataFrame

    # Test with a string (not a DataFrame)
    with pytest.raises(ValueError, match="sales_data parameter should be a pandas DataFrame"):
        sales_summary_statistics("invalid_input")  # String instead of DataFrame

def test_sales_summary_statistics_column_errors():
    """
    Test that the dataframe includes required columns
    """
    # Test with missing columns (e.g., missing 'Quantity')
    data_missing_column = pd.DataFrame({
        'UnitPrice': [100, 200],
        'CustomerID': [1, 2],
        'InvoiceNo': ['INV001', 'INV002'],
        'Description': ['Product A', 'Product B']
    })
    with pytest.raises(ValueError, match="Missing required columns: Quantity"):
        sales_summary_statistics(data_missing_column)

    # Test with incorrect column names (e.g., 'InvoiceNO' instead of 'InvoiceNo')
    data_incorrect_column = pd.DataFrame({
        'Quantity': [10, 5],
        'UnitPrice': [100, 200],
        'CustomerID': [1, 2],
        'InvoiceNO': ['INV001', 'INV002'],  # Incorrect case for 'InvoiceNo'
        'Description': ['Product A', 'Product B']
    })
    with pytest.raises(ValueError, match="Missing required columns: InvoiceNo"):
        sales_summary_statistics(data_incorrect_column)