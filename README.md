# salesanalyzer

[![Documentation Status](https://readthedocs.org/projects/salesanalyzer/badge/?version=latest)](https://salesanalyzer.readthedocs.io/en/latest/?badge=latest)

A python package that helps with the analysis on a sales data. The packagage will contain functions to be used as tools for identifying market segment, predicting future sales and analyzing seasonal revenue trends. <br>

The sales_analyzer package will be an addition to the Python ecosystem as a specialized tool for analyzing retail sales data, targeting small to medium-sized businesses that may not have the resources for an in-house data analytics team and who could benefit from ready-to-use functions for common sales-related tasks. While existing packages such as `Pandas` and `Scikit-learn` provide general tools for data manipulation and machine learning predictions, `salesanalyzer` aims to streamline the process by offering a suite of pre-built, retail-specific analytical functions.

## Installation

```bash
$ pip install salesanalyzer
```

## Functions
- `segment_revenue_share`: Segments products into three categories: cheap, medium, expensive, based on price, and calculates their respective share in total revenue. 
- `predictSales`: Predicts future sales based on the provided historical data and the target.
- `sales_summary_statistics`: Calculates a variety of summary statistics that provide insights into overall sales performance,
    customer behavior, and product performance.

## Usage

`salesanalyzer` can be used to extract sales data insights from available data.
1. Set up imports

```
from salesanalyzer.sales_summary_statistics import sales_summary_statistics
from salesanalyzer.segment_revenue_share import segment_revenue_share
from salesanalyzer.predict_sales import predict_sales
import pandas as pd     # additional import to handle your sales data
```

2. Load your sales data as pandas DataFrame

3. Retrieve the insights:

**Summary statistics**
```
sales_summary_statistics(your_sales_data)
```
The `sales_summary_statistics` returns a pandas DataFrame with:
- 'total_revenue': The total revenue generated by all sales.
- 'unique_customers': The number of unique customers.
- 'average_order_value': The average value of an order (sum of revenue per invoice).
- 'top_selling_product_quantity': The product with the highest quantity sold.
- 'top_selling_product_revenue': The product with the highest total revenue.
- 'average_revenue_per_customer': The average revenue generated by each customer.

**Segment revenue share**
```
segment_revenue_share(your_sales_data, 
                      price_col='UnitPrice', 
                      quantity_col='Quantity')      # replace column names with your data column names
```
The `segment_revenue_share` returns a pandas DataFrame showing the total revenue share for each price segment:
'cheap', 'medium', 'expensive'.

**Predict sales**
```
predict_sales(your_sales_data, 
              new_data,     # new sales data to base the predictions on
              numeric_features = ['UnitPrice'],
              categorical_features = ['Description', 'Country'], 
              target = 'Quantity', 
              date_feature = 'InvoiceDate')
```
The `predict_sales` returns a DataFrame with prediction values, and a printed out MSE score.

## Developer notes:
### Running The Tests

Run the following command in the terminal from the project's root directory to execute the tests:
```bash
pytest tests/
```

To assess the branch coverage for this package:
```bash
pytest --cov=salesanalyzer --cov-branch
```

## Dependencies

This package relies on the following dependencies as outlined in [pyproject.toml](https://github.com/UBC-MDS/salesanalyzer/blob/main/pyproject.toml):

- python = ">=3.10"
- scikit-learn = ">=1.6.1"
- pandas = ">=2.2.3"
- pytest = ">=8.3.4"
- jupyter = ">=1.1.1"
- myst-nb = ">=1.1.2"
- sphinx-autoapi = ">=3.4.0"
- sphinx-rtd-theme = ">=3.0.2"

## Contributors
- Yeji Sohn
- Daria Khon
- Franklin Aryee

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`salesanalyzer` was created by Yeji Sohn, Daria Khon, Franklin Aryee. It is licensed under the terms of the MIT license.

## Credits

`salesanalyzer` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
