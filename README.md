# Thesis Tracker

Thesis Tracker is a Python-based project designed to collect, process, and publish metadata from French academic theses using the [theses.fr API](https://www.theses.fr). 
The project is automated using GitHub Actions, with an optional Docker setup for consistent and reproducible environments.

## Features

- **Data Collection**: Automatically collects and processes thesis.
- **Metadata Extraction**: Extracts relevant information such as thesis title, author, university, and defense date.
- **Automated Workflows**: Uses ```GitHub Actions``` for automating unit tests for core functionalities using ```pytest```, scan vulnerabilities with ```safety``` and ```bandit```.
- **Docker Integration**: Provides a ```Docker``` setup for consistent environments across development and production.

## Installation

### Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/) for dependency management
- [Pytest](https://docs.pytest.org/en/stable/) for running tests
- [Docker](https://docs.docker.com/get-started/) (optional, for containerized environments)

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/pierrehanne/thesis-tracker.git
    cd thesis-tracker
    ```

2. **Install dependencies using Poetry**:

    ```bash
    poetry install
    ```

3. **Activate the virtual environment**:

    ```bash
    poetry shell
    ```

### Usage

To start collecting thesis data, run the main script:

```bash
python thesis_tracker.py
```

### CI/CD with GitHub Actions

This project uses GitHub Actions for Continuous Integration (CI) and Continuous Deployment (CD). 
The CI/CD pipeline is defined in a YAML file and consists of three main jobs:

1. **Linting:** Checks the code for formatting, import order, and style issues.
   - Tools: ```isort```, ```Flake8```, ```Black```
   - Python version: 3.11
   - Poetry is used to install dependencies and manage the environment.
2. **Security Scans:** Runs security scans to ensure there are no vulnerabilities in dependencies or code.
   - Tools: ```Safety```, ```Bandit```
   - Python version: 3.11
   - Runs after the linting job.
3. **Testing:** Runs unit tests in a Docker container to ensure reproducibility and consistency across environments.
   - Docker Build: The pipeline builds a Docker image using Buildx for caching.
   - Run Tests: The Docker container runs the pytest tests inside the built image.

You can find the workflow files in the ```.github/workflows directory```.

### Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes. 
When contributing, ensure that new code is covered with appropriate unit tests.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Contact

For any questions or suggestions, feel free to open an issue or reach out to the project maintainer.