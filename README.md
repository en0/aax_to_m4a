# AAX to M4A

This script makes it easy to convert a bunch of AAX files to M4A. To do this, you will need to
obtain the AAX files first. You can use [OpenAudible](https://openaudible.org/) to backup your audio
books. As of April 2025, you can use the demo license to do the download.

## Quick Start

### Prerequisites

- Ensure you have Python 3.10 or newer installed on your machine
- Install [Poetry](https://python-poetry.org/docs/#installing-with-pipx) for dependency management.

__For Arch__

```bash
sudo pacman -S python-poetry
```

### Setup

1. __Clone the Repository__

Clone the repository to your local machine:

```bash
git clone https://github.com/en0/aax_to_m4a.git
cd aax_to_m4a
```

2. __Install dependencies__

Use Poetry to install the project dependencies:

```bash
poetry install
```

This command will create a virtual environment and install all the required packages as specified in
the pyproject.toml

3. __Activate the Virtual Environment__

Run aax_to_m4a.

```bash
PYTHONPATH=src poetry run python -m aax_to_m4a.convert -h
```

## Convert My Library

Assuming your aax files are located in `~/OpenAudible/aax/`, you can use the following command to
begin the conversion. This command should be run from the root of the gitub repository.

```bash
PYTHONPATH=src poetry run python -m aax_to_m4a.convert ~/OpenAudible/aax/
```

Once the script is complete, you can move the resulting m4a files where ever you would like.

```bash
mv ~/OpenAudible/aax/*.m4a ~/OpenAudible/books/
```
