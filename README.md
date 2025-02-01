# salesanalyzer_mds
[![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![Documentation Status](https://readthedocs.org/projects/salesanalyzer/badge/?version=latest)](https://salesanalyzer.readthedocs.io/en/latest/?badge=latest)
[![ci-cd](https://github.com/UBC-MDS/salesanalyzer/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/salesanalyzer/actions/workflows/ci-cd.yml)
[![codecov](https://codecov.io/gh/UBC-MDS/salesanalyzer/graph/badge.svg?token=BLQNynILl1)](https://codecov.io/gh/UBC-MDS/salesanalyzer)
[![Python Version](https://img.shields.io/badge/python-%3E%3D%203.10-blue)](https://www.python.org/downloads/release/python-3100/)
![PyPI](https://img.shields.io/pypi/v/salesanalyzer-mds?label=pypi%20package)

A Python package designed to simplify retail sales data analysis for small to medium-sized businesses. This tool offers a set of pre-built functions that make it easy to identify market segments, predict future sales, and analyze seasonal revenue trends.  <br>

## Why salesanalyzer_mds?

Small to medium-sized businesses (SMBs) often lack the resources for in-house data teams or complex analytics tools. sales_analyzer is here to bridge that gap by providing easy-to-use, specialized functions that allow businesses to extract valuable insights from their sales data without requiring deep expertise in data science.

### Key Benefits:

- **Tailored for SMBs**: No need for expensive or complex tools. Our package is designed specifically for small to medium-sized businesses to help them make data-driven decisions with ease.
- **Easy-to-use functions**: Simple, pre-built functions for common retail sales tasks so you can get started right away.
- **Cost-effective**: Instead of hiring a full-time data analytics team or paying for expensive software, this package offers an affordable, one-stop solution to meet your business’s analytical needs.
- **Actionable Insights**: Gain a better understanding of your market segments and sales trends, which can inform inventory management, marketing strategies, and customer outreach.

## How It Fits into the Python Ecosystem

While existing Python packages such as `Pandas` and `Scikit-learn` provide powerful general-purpose tools for data manipulation and machine learning, they require significant customization and specialized knowledge to be applied effectively to retail sales analysis. `sales_analyzer` complements these tools by streamlining common retail-specific tasks. It provides a suite of pre-built, easy-to-use functions specifically tailored to sales data, so businesses don't need to spend time customizing solutions for their needs.


## Installation

```bash
$ pip install salesanalyzer_mds
```

## Functions

- `segment_revenue_share`: Segments products into three categories: cheap, medium, expensive, based on price, and calculates their respective share in total revenue. 
- `predictSales`: Predicts future sales based on the provided historical data and the target.
- `sales_summary_statistics`: Calculates a variety of summary statistics that provide insights into overall sales performance,
    customer behavior, and product performance.

## Usage

`salesanalyzer_mds` can be used to extract sales data insights from available data.
1. Set up imports

```python
from salesanalyzer_mds.sales_summary_statistics import sales_summary_statistics
from salesanalyzer_mds.segment_revenue_share import segment_revenue_share
from salesanalyzer_mds.predict_sales import predict_sales
import pandas as pd     # additional import to handle your sales data
```

2. Load your sales data as pandas DataFrame

3. Retrieve the insights:

**Summary statistics**

```python
sales_summary_statistics(your_sales_data)
```

The `sales_summary_statistics()` function returns a pandas DataFrame with:

- 'total_revenue': The total revenue generated by all sales.
- 'unique_customers': The number of unique customers.
- 'average_order_value': The average value of an order (sum of revenue per invoice).
- 'top_selling_product_quantity': The product with the highest quantity sold.
- 'top_selling_product_revenue': The product with the highest total revenue.
- 'average_revenue_per_customer': The average revenue generated by each customer.

**Segment revenue share**

```python
segment_revenue_share(your_sales_data, 
                      price_col='UnitPrice', 
                      quantity_col='Quantity',
                      price_thresholds=None)      # replace column names with your data column names
```

The `segment_revenue_share()` funtion returns a pandas DataFrame showing the total revenue share for each price segment:
'cheap', 'medium', 'expensive'. Custom price thresholds can be set by the user other set automatically.

- Custom price thresholds can be set using the `price_thresholds` parameter.
- If not specified, thresholds are automatically determined based on the data.

**Predict sales**

```python
predict_sales(your_sales_data, 
              new_data,     # new sales data to base the predictions on
              numeric_features = ['UnitPrice'],
              categorical_features = ['Description', 'Country'], 
              target = 'Quantity', 
              date_feature = 'InvoiceDate')
```

The `predict_sales()` function returns a DataFrame with prediction values, and a printed out MSE score.

## Developer notes:
### Install Development Version
1. Clone the repository and navigate into the project root directory.

2. Create a new environment with Python 3.10:

    ```bash
    conda create -n salesanalyzermds python=3.10
    conda activate salesanalyzermds
    ```

3. Install Poetry by following [these instructions](https://python-poetry.org/docs/#installation), and then run the following bash command to install the necessary dependencies:

    ```bash
    poetry install
    ```

### Running The Tests

To test the `salesanalyzer-mds` package, follow the steps below:

1. Execute the tests using `pytest` from the root project directory:

```bash
pytest tests/
```

2. To assess the branch coverage for this package:

```bash
pytest --cov=salesanalyzer_mds --cov-branch
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

`salesanalyzer_mds` was created by Yeji Sohn, Daria Khon, Franklin Aryee. It is licensed under the terms of the MIT license.

## Credits

`salesanalyzer_mds` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
