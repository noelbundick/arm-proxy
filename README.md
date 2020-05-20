# arm-proxy

## Usage

```shell
# Install the arm-proxy extension
az extension add -s https://github.com/noelbundick/arm-proxy/releases/download/v0.0.1/arm_proxy-0.0.1-py3-none-any.whl

# Start a new proxy pointed at the sample folder
git clone https://github.com/noelbundick/arm-proxy.git
cd arm-proxy/sample
az arm-proxy start

# Iterate on linked ARM templates hosted from your local machine (replace with your ngrok URL)
az deployment sub create -l westus2 -u https://be5cc4e3.ngrok.io/baseTemplate.json
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
