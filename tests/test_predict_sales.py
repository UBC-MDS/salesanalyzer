from salesanalyzer_mds.predict_sales import predict_sales
import pytest
import pandas as pd

@pytest.fixture
def test_data():
    """Sample data for function testing"""
    test_data = pd.DataFrame({
    "product_name": [
        "Laptop", "Monitor", "Headphones", "Laptop", "Headphones", "Laptop", "Monitor"
    ],
    "unit_price": [1200, 800, 150, 3000, 200, 2000, 500],
    "invoice_date": ['2023-11-03', '2024-12-08', '2024-06-26', '2024-05-11', '2024-02-14', '2024-01-20', '2024-05-30'],
    "city": ['Vancouver', 'Toronto', 'Calgary', 'Vancouver', 'Calgary', 'Vancouver', 'Toronto'],
    "quantity": [1, 2, 2, 4, 4, 2, 5]
    })
    return test_data


@pytest.fixture
def test_new_data(test_data):
    """Creates a copy of test data to use for new predictions"""
    return test_data.copy()

valid_cat_features = ['product_name', 'city']
valid_num_features = ['unit_price']
valid_date_feature = 'invoice_date'
valid_target = 'quantity'


def test_input_type(test_data, test_new_data):
    """Test that predict_sales() detects the wrong input data types correctly"""
    with pytest.raises(ValueError, match="sales_data parameter should be a pandas DataFrame"):
        predict_sales("not_a_dataframe", test_new_data, valid_num_features,
                      valid_cat_features, valid_target, valid_date_feature)
        
    with pytest.raises(ValueError, match="new_data parameter should be a pandas DataFrame"):
        predict_sales(test_data, "not_a_dataframe", valid_num_features,
                      valid_cat_features, valid_target, valid_date_feature)
        
    with pytest.raises(ValueError, match="numeric features should be a list"):
        predict_sales(test_data, test_new_data, "not_a_list",
                      valid_cat_features, valid_target, valid_date_feature)

    with pytest.raises(ValueError, match="categorical features should be a list"):
        predict_sales(test_data, test_new_data, valid_num_features,
                      "not_a_list", valid_target, valid_date_feature)  

    with pytest.raises(ValueError, match="target should be a string"):
        predict_sales(test_data, test_new_data, valid_num_features,
                      valid_cat_features, 12345, valid_date_feature) 
        
    with pytest.raises(ValueError, match="date features should be a string"):
        predict_sales(test_data, test_new_data, valid_num_features,
                      valid_cat_features, valid_target, 12345) 

    with pytest.raises(TypeError, match="numeric_features should countain numeric data type only"):
        predict_sales(test_data, test_new_data, ['city', 'unit_price'],
                      valid_cat_features, valid_target, valid_date_feature)

  
def test_output_no_date_feature(test_data, test_new_data):
    """Tests that predict_sales() round and returns a dictionary without a date feature"""
    result = predict_sales(test_data, test_new_data, valid_num_features, 
                           valid_cat_features, valid_target)
    assert isinstance(result, pd.DataFrame)
    assert all(isinstance(value, float) for value in result["Predicted values"])
    assert all(abs(value - round(value, 2)) < 1e-6 for value in result["Predicted values"])


def test_output_with_date_feature(test_data, test_new_data):
    """Tests that predict_sales() round and returns a dictionary with a date feature"""
    result = predict_sales(test_data, test_new_data, valid_num_features, 
                           valid_cat_features, valid_target, valid_date_feature)
    assert isinstance(result, pd.DataFrame)
    assert all(isinstance(value, float) for value in result["Predicted values"])
    assert all(abs(value - round(value, 2)) < 1e-6 for value in result["Predicted values"])


def test_missing_input(test_data):
    """Tests if predict_sales() raises a ValueError when there is missing input"""
    with pytest.raises(Exception):
        predict_sales(test_data)
