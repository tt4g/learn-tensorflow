# Overview

Leaning [TensorFlow](https://www.tensorflow.org/)

## Development

### Use Docker

Launch Docker container.
You can use Jupyter Notebook, visit http://127.0.0.1:8888/?token=learn-tensorflow

```bash
# Jupyter Notebook on 8888 port.
$ docker-compose up -d

# Launch console.
$ docker-compose learn-tensorflow /bin/bash
```

Also use Visual Studio Remote Container environment defined by `.devcontainer/devcontainer.json`.

### Use Virtual environment

`venv`

```bash
$ python -m venv .venv
```

`virtualenv`

```bash
$ virtualenv .venv
```

#### Install dependencies.

```bash
$ ./.venv/Scripts/activate
$ python -m pip install --upgrade pip
$ python -m pip install -r requirements.txt
```
