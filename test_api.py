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
            headers = eval(row['Header']) if row['Header'] else {}
            data.append((row['Method'], row['Path'], body, headers, result))
    return data

@pytest.mark.parametrize("Method,Path,Body,Headers,Result", read_csv_data())
def test_http_requests(Method,Path,Body,Headers,Result):

    response = getattr(requests, Method.lower())(Path, json=Body, headers=Headers)
    assert (response.status_code == 200) == Result or (response.status_code == 204) == Result
