#!/bin/bash

python main.py

echo "Main.py completed and CSV file generated."

pytest test_api.py --html=report.html

echo "Report generation complete. It is available at: http://localhost:8080/report.html"
