# Virtual Environment

## Summary

- this is a "virtual environment" (venv)
- you can use it to scope python package installations to your project instead of your machine
- this is useful in two ways: (1) you can distill exact lists of dependencies that were installed with ```pip install``` for your project, and (2) other developers can quickly install all the dependencies (including python version) for your project because they are being tracked.

## How to use

1. navigate to the top-level gut theory folder:

```sh

cd ./GutTheory

```

2. activate the venv:

```sh

source venv/bin/activate

```

3. after activating the venv you can use pip as normal and it will install the target package to your venv instead of your machine.

## Other commands

1. create a new virtual envrionment:

```sh

python -m venv "the name of your new venv"

```

2. make a pip freeze file:

```sh

cd GutTheory/venv

pip freeze -l > requirements.txt

```