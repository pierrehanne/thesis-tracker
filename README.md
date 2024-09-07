# Thesis Tracker

Thesis Tracker is a Python-based project designed to collect, process, and publish metadata from French academic theses using the [theses.fr API](https://www.theses.fr). The project is automated using GitHub Actions, with an optional Docker setup for consistent and reproducible environments.

## Features

- **Daily Data Collection**: Automatically collects and processes thesis metadata daily.
- **Metadata Extraction**: Extracts relevant information such as thesis title, author, university, and defense date.
- **Automated Workflows**: Uses GitHub Actions for automating data collection, processing, and publishing.
- **Docker Integration**: Provides a Docker setup for consistent environments across development and production.

## Installation

### Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/) for dependency management
- Docker (optional, for containerized environments)

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/thesis-tracker.git
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

4. **Configure environment variables** (if any):

    Create a `.env` file to store your API keys or other configurations:

    ```bash
    touch .env
    ```

    Add the necessary environment variables to `.env`.

### Usage

To start collecting thesis data, run the main script:

```bash
python thesis_tracker.py
```

### CI/CD with GitHub Actions

This project uses GitHub Actions to automate:
- Daily Data Collection: Collect and process data every day.
- Code Testing and Linting: Ensure code quality before merges.

You can find the workflow files in the .github/workflows directory.

### Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Contact

For any questions or suggestions, feel free to open an issue or reach out to the project maintainer.