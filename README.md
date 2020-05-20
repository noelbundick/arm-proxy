# arm-proxy

## Usage

```shell
# Install the arm-proxy extension and start a new dynamic proxy
az extension add -s https://github.com/noelbundick/arm-proxy/releases/download/v0.0.1/arm_proxy-0.0.1-py3-none-any.whl
az arm-proxy start

# Iterate on linked ARM templates hosted from your local machine
az deployment sub create -l westus2 -u http://be5cc4e3.ngrok.io/sample/baseTemplate.json
```

## Development

```shell
# one-time configuration
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
azdev setup -r .

# linting
pylint src
flake8 src
```
