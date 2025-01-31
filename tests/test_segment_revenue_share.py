import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from salesanalyzer_mds.segment_revenue_share import segment_revenue_share


@pytest.fixture
def sample_data():
    """Sample sales data for testing"""
    return pd.DataFrame({
        'UnitPrice': [1.50, 2.50, 3.50, 4.50, 5.50],
        'Quantity': [10, 20, 30, 40, 50]
    })


def test_normal_case(sample_data):
    """Test default segmentation (quantile-based)"""
    result = segment_revenue_share(sample_data)

    expected = pd.DataFrame({
        'PriceSegment': ['cheap', 'medium', 'expensive'],
        'TotalRevenue': [65.0, 105.0, 455.0],
        'RevenueShare (%)': [10.4, 16.8, 72.8]
    })

    expected = expected.sort_values(by="PriceSegment").reset_index(drop=True)
    result = result.sort_values(by="PriceSegment").reset_index(drop=True)

    assert_frame_equal(result, expected, atol=1e-2)


def test_custom_thresholds(sample_data):
    """Test segmentation with user-defined price thresholds"""
    custom_thresholds = (3.0, 4.0)
    result = segment_revenue_share(
        sample_data,
        price_thresholds=custom_thresholds
        )

    expected = pd.DataFrame({
        'PriceSegment': ['cheap', 'medium', 'expensive'],
        'TotalRevenue': [65.0, 105.0, 455.0],
        'RevenueShare (%)': [10.4, 16.8, 72.8]
    })

    expected = expected.sort_values(by="PriceSegment").reset_index(drop=True)
    result = result.sort_values(by="PriceSegment").reset_index(drop=True)

    assert_frame_equal(result, expected, atol=1e-2)


def test_empty_dataframe():
    """Ensure function raises ValueError on empty DataFrame"""
    empty_df = pd.DataFrame(columns=['UnitPrice', 'Quantity'])
    with pytest.raises(ValueError):
        segment_revenue_share(empty_df)


def test_missing_columns(sample_data):
    """Ensure function raises KeyError when required columns are missing"""
    missing_col_df = sample_data.drop(columns=['Quantity'])
    with pytest.raises(KeyError):
        segment_revenue_share(missing_col_df)


def test_missing_values():
    """Ensure function raises ValueError if NaN values exist"""
    missing_values_df = pd.DataFrame({
        'UnitPrice': [2.55, None, 3.39],
        'Quantity': [6, 6, None]
    })
    with pytest.raises(ValueError):
        segment_revenue_share(missing_values_df)


def test_invalid_data_types():
    """Ensure function raises TypeError for non-numeric data"""
    invalid_df = pd.DataFrame({
        'UnitPrice': ['a', 2.50, 'c'],
        'Quantity': [1, 'b', 3]
    })
    with pytest.raises(TypeError):
        segment_revenue_share(invalid_df)


def test_zero_quantity(sample_data):
    """Ensure function handles case where all quantities are zero"""
    zero_quantity_df = sample_data.copy()
    zero_quantity_df['Quantity'] = 0
    result = segment_revenue_share(zero_quantity_df)

    expected = pd.DataFrame({
        'PriceSegment': ['cheap', 'medium', 'expensive'],
        'TotalRevenue': [0.0, 0.0, 0.0],
        'RevenueShare (%)': [0.0, 0.0, 0.0]
    })

    expected = expected.sort_values(by="PriceSegment").reset_index(drop=True)
    result = result.sort_values(by="PriceSegment").reset_index(drop=True)

    assert_frame_equal(result, expected)


def test_extreme_thresholds(sample_data):
    """Test when price thresholds are extreme (all items fall into a single category)"""
    result = segment_revenue_share(sample_data, price_thresholds=(10, 20))

    expected = pd.DataFrame({
        'PriceSegment': ['cheap', 'medium', 'expensive'],
        'TotalRevenue': [625.0, 0.0, 0.0],  # Everything is "cheap"
        'RevenueShare (%)': [100.0, 0.0, 0.0]
    })

    expected = expected.sort_values(by="PriceSegment").reset_index(drop=True)
    result = result.sort_values(by="PriceSegment").reset_index(drop=True)

    assert_frame_equal(result, expected)


def test_single_row():
    """Ensure function correctly categorizes a single product"""
    single_row_df = pd.DataFrame({
        'UnitPrice': [5.00],
        'Quantity': [10]
    })
    result = segment_revenue_share(single_row_df)

    expected = pd.DataFrame({
        'PriceSegment': ['cheap', 'medium', 'expensive'],
        'TotalRevenue': [50.0, 0.0, 0.0],
        'RevenueShare (%)': [100.0, 0.0, 0.0]
    })

    expected = expected.sort_values(by="PriceSegment").reset_index(drop=True)
    result = result.sort_values(by="PriceSegment").reset_index(drop=True)

    assert_frame_equal(result, expected)


def test_identical_prices():
    """Ensure function handles case where all products have the same price"""
    identical_prices_df = pd.DataFrame({
        'UnitPrice': [10.00, 10.00, 10.00],
        'Quantity': [1, 2, 3]
    })
    result = segment_revenue_share(identical_prices_df)

    expected = pd.DataFrame({
        'PriceSegment': ['cheap', 'medium', 'expensive'],
        'TotalRevenue': [60.0, 0.0, 0.0],
        'RevenueShare (%)': [100.0, 0.0, 0.0]
    })

    expected = expected.sort_values(by="PriceSegment").reset_index(drop=True)
    result = result.sort_values(by="PriceSegment").reset_index(drop=True)

    assert_frame_equal(result, expected)


def test_large_data():
    """Ensure function correctly processes large datasets"""
    large_data = pd.DataFrame({
        'UnitPrice': [i for i in range(1, 101)],
        'Quantity': [i for i in range(1, 101)]
    })
    result = segment_revenue_share(large_data)

    total_revenue = sum(large_data['UnitPrice'] * large_data['Quantity'])

    assert result['TotalRevenue'].sum() == total_revenue
    assert not result.empty
