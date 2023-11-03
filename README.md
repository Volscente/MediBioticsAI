# MediBioticsAI
MediBioticsAI is a cutting-edge initiative at the forefront of the healthcare revolution, harnessing the power of AI&ML to address some of the most pressing challenges in the field of health and medicine.

# Setup
## Update PYTHONPATH
Add the current directory to the `PYTHONPATH` environment variables.
``` bash
export PYTHONPATH="$PYTHONPATH:/<absolute_path>/caelvid"
```

## Poetry

### Installation

[Reference Documentation](https://python-poetry.org/)

Run the following command from the terminal:
``` bash
curl -sSL https://install.python-poetry.org | python3 -
```

For **MacOS** with ZSH add the `.local/bin` to the `PATH` environment variable. Modify the `.zshrc` file with the following command:

``` bash
export PATH="$HOME/.local/bin:$PATH"
```

### Init Repository
```bash
poetry init
```

### Add Dependency
``` bash
# NOTE: Use '--group dev' to install in the 'dev' dependencies list
poetry add <library_name>

poetry add <library> --group dev

poetry add <libarry> --group <group_name>
```

### Install Dependencies
``` bash
# Install the dependencies listed in pyproject.toml [tool.poetry.dependencies]
poetry install

# Use the option '--without test,docs,dev' if you want to esclude the specified group from install
poetry install --without test,docs,dev
```