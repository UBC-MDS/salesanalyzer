# salesanalyzer

A python package that helps with the analysis on a sales data. The packagage will contain functions to be used as tools for identifying market segment, predicting future sales and analyzing seasonal revenue trends. <br>

The sales_analyzer package will be an addition to the Python ecosystem as a specialized tool for analyzing retail sales data, targeting small to medium-sized businesses that may not have the resources for an in-house data analytics team and who could benefit from ready-to-use functions for common sales-related tasks. While existing packages such as `Pandas` and `Scikit-learn` provide general tools for data manipulation and machine learning predictions, `salesanalyzer` aims to streamline the process by offering a suite of pre-built, retail-specific analytical functions.

## Installation

```bash
$ pip install salesanalyzer
```

## Usage
- `segment_revenue_share`: Segments products into three categories: cheap, medium, expensive, based on price, and calculates their respective share in total revenue. 
- `predictSales`: Predicts future sales based on the provided historical data and the target.
- `sales_summary_statistics`: Calculates a variety of summary statistics that provide insights into overall sales performance,
    customer behavior, and product performance.


## Position in Python Ecosystem

The `salesanalyzer` package provides a quick, easy-to-use tools for generating summaries and basic predictive modeling specifically for sales datasets. `salesanalyzer` offers pre-built functions tailored for retail analysis, making it ideal for small to medium-sized businesses needing fast insights into sales performance without complex setup. It simplifies tasks like revenue calculation and sales forecasting, offering a ready-to-use solution for retail-specific analytics.

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
