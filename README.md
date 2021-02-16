

# Wallstreetbets Sentiment Analyser

This section should include a small description of the project.

## Requirements

* [Python3 installed](https://www.python.org/downloads/)
* [Virtualenv installed](https://virtualenv.pypa.io/en/latest/)
* [wheel installed](https://pypi.org/project/wheel/) due to an open issue with [aws_lambda_layers](https://github.com/awslabs/aws-lambda-builders/issues/71) not resolving dependencies

Project dependencies are installed with

```bash
make requirements
```

## Getting Started
1. Set up your local environment using ```make create-local-env```
2. In the created .env you will need to add the reddit account details

## Installing the module

Run ```python3 -m pip install wallstreeBetsAnalyser```


## Example usage

```python
from wallstreetBetsAnalyser import run

resval = run('wallstreetbets', 100)
print(resval)
```


## Disclaimer

This project is not financial advise.
