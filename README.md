Dockerized Test Automation Project
==================================

This project is designed to run automated API tests using data scraped from a documentation site. It automates generating a CSV file, runs HTTP tests based on this data, and creates an HTML report viewable in a browser.

Project Structure
-----------------

*   `main.py:` Scrapes API documentation to extract HTTP methods and paths and generates data.csv.
    
*   `test\_api.py:` Runs parameterized HTTP tests using the data.csv file and generates an HTML report.
    
*   `requirements.txt:` Contains Python dependencies for the project.
    
*   `data.csv:` CSV file generated by main.py with method, path, and request body data.
    
*   `Dockerfile:` Docker configuration for setting up and running the project.
    

Prerequisites
-------------

Ensure you have [Docker](https://www.docker.com/) installed on your machine.

How to Build and Run the Docker Container
-----------------------------------------

1. Build the Docker Image:

    ```shell 
    docker build -t test-automation-project .
2. Run the Docker Container:
    ```shell
    docker run --rm -v $(pwd):/app test-automation-project
The `--rm` flag ensures that the container is removed after it stops. The `-v $(pwd):/app` option mounts the current directory inside the container, so the generated report and data are accessible.

What the Docker Container Does
-------------------------------

1. **Runs `main.py`:**
        Scrapes API documentation from `https://reqres.in/api-docs/#/` to generate `data.csv` with API paths and request bodies.

2. **Runs Tests with `test_api.py`:**
        Uses `pytest` to execute tests from `data.csv` and outputs `report.html`.

3. **Opens `report.html` in the Browser:**
        Uses Python's `webbrowser` module to open the report if the tests succeed.

Example Usage
-------------

After running the container, `report.html` will be generated in your project folder. If your host system has a default browser set up, the container will try to open `report.html` automatically.

Dependencies
------------

Listed in `requirements.txt`:

* `selenium`
* `pytest`
* `requests`
* `pytest-html`