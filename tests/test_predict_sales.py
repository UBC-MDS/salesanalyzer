from salesanalyzer.predict_sales import predict_sales
import pytest
import pandas as pd

test_data = pd.read_csv('tests/test_data.csv')
test_new_data = test_data.copy()
valid_cat_features = ['product_name', 'city']
valid_num_features = ['unit_price']
valid_date_feature = 'invoice_date'
valid_target = 'quantity'

def test_input_type():
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
        
def test_output():
    """Tests that predict_sales() returns a dictionary"""
    result = predict_sales(test_data, test_new_data, valid_num_features, 
                           valid_cat_features, valid_target)
    assert isinstance(result, dict)
    assert all(isinstance(value, float) for value in result["Preicted values"])
    assert all(abs(value - round(value, 2)) < 1e-6 for value in result["Preicted values"])

def test_missing_input():
    """Tests if predict_sales() raises a ValueError when there is missing input"""
    with pytest.raises(Exception):
        predict_sales(test_data, new_data)