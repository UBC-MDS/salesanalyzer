import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from salesanalyzer.salesanalyzer import segment_revenue_share


@pytest.fixture
def sample_data():
    """Fixture for sample sales data."""
    return pd.DataFrame({
        'unit_price': [1.50, 2.50, 3.50, 4.50, 5.50],
        'quantity': [10, 20, 30, 40, 50]
    })


def test_normal_case(sample_data):
    """Test the function with valid input data."""
    result = segment_revenue_share(sample_data)
    expected = pd.DataFrame({
        'PriceSegment': ['cheap', 'medium', 'expensive'],
        'TotalRevenue': [65.0, 105.0, 455.0],
        'RevenueShare (%)': [10.4, 16.8, 72.8]
    })
    assert_frame_equal(
        result.sort_values('PriceSegment').reset_index(drop=True),
        expected.sort_values('PriceSegment').reset_index(drop=True),
        atol=1e-2
    )


def test_empty_dataframe():
    """Test the function with an empty DataFrame."""
    empty_df = pd.DataFrame(columns=['unit_price', 'quantity'])
    with pytest.raises(ValueError):
        segment_revenue_share(empty_df)


def test_missing_columns(sample_data):
    """Test the function with missing columns."""
    missing_col_df = sample_data.drop(columns=['quantity'])
    with pytest.raises(KeyError):
        segment_revenue_share(missing_col_df)


def test_missing_values():
    """Test the function with missing values in required columns."""
    missing_values_df = pd.DataFrame({
        'unit_price': [2.55, None, 3.39],
        'quantity': [6, 6, None]
    })
    with pytest.raises(ValueError):
        segment_revenue_share(missing_values_df)


def test_invalid_data_types():
    """Test the function with invalid data types in required columns."""
    invalid_df = pd.DataFrame({
        'unit_price': ['a', 2.50, 'c'],
        'quantity': [1, 'b', 3]
    })
    with pytest.raises(TypeError):
        segment_revenue_share(invalid_df)


def test_zero_quantity(sample_data):
    """Test the function when all quantities are zero."""
    zero_quantity_df = sample_data.copy()
    zero_quantity_df['quantity'] = 0
    result = segment_revenue_share(zero_quantity_df)
    expected = pd.DataFrame({
        'PriceSegment': ['cheap', 'medium', 'expensive'],
        'TotalRevenue': [0.0, 0.0, 0.0],
        'RevenueShare (%)': [0.0, 0.0, 0.0]
    })
    assert_frame_equal(
        result.sort_values('PriceSegment').reset_index(drop=True),
        expected.sort_values('PriceSegment').reset_index(drop=True)
    )


def test_single_row():
    """Test the function with a single row of data."""
    single_row_df = pd.DataFrame({
        'unit_price': [5.00],
        'quantity': [10]
    })
    result = segment_revenue_share(single_row_df)
    expected = pd.DataFrame({
        'PriceSegment': ['cheap'],
        'TotalRevenue': [50.0],
        'RevenueShare (%)': [100.0]
    })
    assert_frame_equal(result, expected)


def test_identical_prices():
    """Test the function when all prices are identical."""
    identical_prices_df = pd.DataFrame({
        'unit_price': [10.00, 10.00, 10.00],
        'quantity': [1, 2, 3]
    })
    result = segment_revenue_share(identical_prices_df)
    expected = pd.DataFrame({
        'PriceSegment': ['cheap'],
        'TotalRevenue': [60.0],
        'RevenueShare (%)': [100.0]
    })
    assert_frame_equal(result, expected)


def test_large_data():
    """Test the function with a large dataset."""
    large_data = pd.DataFrame({
        'unit_price': [i for i in range(1, 101)],
        'quantity': [i for i in range(1, 101)]
    })
    result = segment_revenue_share(large_data)
    total_revenue = sum(large_data['unit_price'] * large_data['quantity'])
    assert result['TotalRevenue'].sum() == total_revenue
    assert not result.empty
