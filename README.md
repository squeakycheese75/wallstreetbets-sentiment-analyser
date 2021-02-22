# Wallstreetbets Sentiment Analyser

A library for extracting posts from the r/wallstreetbets reddit group and running them through a sentiment analyser (vader).

## Requirements

- [Python3 installed](https://www.python.org/downloads/)
- [Virtualenv installed](https://virtualenv.pypa.io/en/latest/)
- [wheel installed](https://pypi.org/project/wheel/) due to an open issue with [aws_lambda_layers](https://github.com/awslabs/aws-lambda-builders/issues/71) not resolving dependencies

From your appropriate Python environment run the following:

```bash
make base-requirements
```

## Getting Started

1. Set up your local environment using `make create-local-env`
2. In the .env file you will need to add the reddit account details.

## Installing the module

Run `python3 -m pip install wallstreetBetsAnalyser`

## Example usage

```python
from wallstreetBetsAnalyser import run

resval = run('wallstreetbets', 100)
print(resval)
```

## Disclaimer

This project is not financial advice. Please be aware of Reddit API limits.
