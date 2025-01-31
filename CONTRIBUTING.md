# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

## Types of Contributions

### Report Bugs

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

You can never have enough documentation! Please feel free to contribute to any
part of the documentation, such as the official docs, docstrings, or even
on the web in blog posts, articles, and such.

### Submit Feedback

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

### Fixing Typos

If you spot small typos or grammatical errors in documentation, you can fix them directly using the GitHub web interface, as long as the changes are made in the source file.

* **YES**: Edit a comment or documentation block in a `.R` file under the `R/` directory.
* **NO**: Do not edit `.Rd` files under the `man/` directory.

## Get Started!

Ready to contribute? Here's how to set up `salesanalyzer_mds` for local development.

1. Download a copy of `salesanalyzer_mds` locally.
2. Install `salesanalyzer_mds` using `poetry`:

    ```console
    $ poetry install
    ```

3. Use `git` (or similar) to create a branch for local development and make your changes:

    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

4. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests.

5. Commit your changes and open a pull request.

## Pull Request Guidelines

### Prerequisites 

Before submitting a pull request (PR), it’s important to first file an issue to ensure the problem is understood and agreed upon. If you've discovered a bug, please create an issue and provide a minimal [reprex](https://www.tidyverse.org/help/#reprex) that illustrates the problem.

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python

### Pull Request Process

* **Branching**: We recommend creating a separate Git branch for each pull request (PR).
* **Code Style**: Please ensure new code follows the [tidyverse style guide](http://style.tidyverse.org) and PEP8 [style guide](https://www.python.org/dev/peps/pep-0008/). Please don’t reformat code unrelated to your PR.

## Code of Conduct

Please note that the `_mds_` project is released with a
Code of Conduct. By contributing to this project you agree to abide by its terms.
