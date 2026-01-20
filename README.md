# Weather Data Analyzer (CLI)

## Overview

Weather Data Analyzer is a lightweight, command-line Python application
designed to load, clean, analyze, and report daily weather data stored
in CSV format. The project demonstrates clean code organization, modular
design, and basic data analysis techniques using Python's standard
library.

This project is well-suited for learning purposes, portfolio building,
and showcasing structured Git commit history.

------------------------------------------------------------------------

## Key Features

-   Load weather data from a CSV file
-   Validate and clean raw input data
-   Filter weather records by city and date
-   Compute basic statistics:
    -   Average temperature
    -   Minimum temperature
    -   Maximum temperature
-   Display a summary report in the terminal

------------------------------------------------------------------------

## Project Structure

    weather_analyzer/
    │
    ├── main.py              # Application entry point
    ├── config.py            # Global configuration values
    ├── weather_record.py    # Weather record data model
    ├── data_loader.py       # CSV loading logic
    ├── data_cleaner.py      # Data validation and cleaning
    ├── analyzer.py          # Data analysis functions
    ├── report.py            # Report generation and output
    ├── utils.py             # Utility and validation helpers

------------------------------------------------------------------------

## Requirements

-   Python 3.8 or higher
-   No third-party libraries required

------------------------------------------------------------------------

## Input Data Format

The application expects a CSV file named `weather_data.csv` in the
project root directory.

Example:

    date,city,temperature,humidity
    2026-01-01,New York,5.2,60
    2026-01-02,New York,6.1,58
    2026-01-01,Boston,3.8,65

Constraints: - Date format: `YYYY-MM-DD` - Temperature and humidity must
be numeric values

------------------------------------------------------------------------

## How to Run

1.  Clone the repository:

    ``` bash
    git clone <repository-url>
    ```

2.  Navigate to the project directory:

    ``` bash
    cd weather_analyzer
    ```

3.  Add `weather_data.csv` to the project root.

4.  Run the application:

    ``` bash
    python main.py
    ```

------------------------------------------------------------------------

## Sample Output

    Weather Summary Report
    ----------------------
    Average Temp: 6.3
    Max Temp: 9.1
    Min Temp: 2.8
    Records: 10

------------------------------------------------------------------------

## Design Goals

-   Maintain clean separation of concerns
-   Keep functions small and testable
-   Enable meaningful incremental Git commits
-   Use standard Python libraries only

------------------------------------------------------------------------

## Possible Enhancements

-   Add unit tests
-   Accept command-line arguments
-   Export reports to JSON or CSV
-   Integrate Pandas or Spark for large datasets
-   Extend analysis to time-series trends

------------------------------------------------------------------------

## License

This project is intended for educational and demonstration purposes.
