# arm-proxy

ARM does not allow you to reference local template files. Because of that limitation, developers are required to deploy their templates to a publically addressable endpoint before deploying the template. This is cumbersome for developers because every template change needs to saved, committed, and pushed to the internet, either via Git, Blob Storage, or some other website.

Until now...

The arm-proxy Azure CLI extension allows you to develop ARM templates locally without having to host them on a public website.  This will speed up your ARM template inner-loop dev cycle.

It uses ngrok to create a secure tunnel to your local machine that can be accessed by Azure when it deploys your template.

> This is for development purposes only.  Do not use in prod.


## Setup

1. Create an ngrok account and install ngrok https://ngrok.com/
2. Make sure ngrok is in your PATH
3. Install the [Azure CLI v2.6.0+](https://aka.ms/azcliget)

## ARM Template Setup

Your base ARM template (the one that links to other ARM templates) needs to include the following:

You can find a complete sample here: [baseTemplate.json](https://github.com/noelbundick/arm-proxy/blob/master/sample/baseTemplate.json)

1. assetsBaseUrl variable

    ```json
    "variables": {
        "assetsBaseUrl": "[uri(deployment().properties.templateLink.uri, './')]"
    },
    ```

2. templateLink that uses assetsBaseUrl variable

    ```json
    "templateLink": {
        "uri": "[uri(variables('assetsBaseUrl'), './linkedTemplate.json')]"
    }
    ```

## Usage

1. Install the arm-proxy extension

    ```shell
    az extension add -s https://github.com/noelbundick/arm-proxy/releases/download/v0.0.1/arm_proxy-0.0.1-py3-none-any.whl
    ```

2. Navigate to a folder that contains your ARM templates

    You can find a sample here: [arm-proxy/sample](https://github.com/noelbundick/arm-proxy/tree/master/sample)


3. Start the arm-proxy

    ```shell
    az arm-proxy start
    ```

    This will output your ngrok URL, which you will use in the next step.

4. Run ARM Template Deployment

    IMPORTANT: Open a separate terminal to run your scripts.


    Iterate on linked ARM templates hosted from your local machine (replace with your ngrok URL)

    ```shell
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
