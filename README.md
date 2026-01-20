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
