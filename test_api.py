import csv
import requests
import pytest

def read_csv_data():
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            result = row['Result'] == 'True'
            if row['Body']:
                body = eval(row['Body'])
            else:
                body = None
            data.append((row['Method'], row['Path'], body, result))
    return data

@pytest.mark.parametrize("Method,Path,Body,Result", read_csv_data())
def test_http_requests(Method,Path,Body,Result):

    response = getattr(requests, Method.lower())(Path, json=Body)
    assert (response.status_code == 200) == Result or (response.status_code == 204) == Result


