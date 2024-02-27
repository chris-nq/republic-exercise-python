import os
import csv
from click.testing import CliRunner
from src.scan_planets import scan_planets


def get_csv_data(filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter="|", quoting=csv.QUOTE_NONE)
        data = list(reader)
    return data


def invoke_scan_planets(terrains=None):
    runner = CliRunner()
    return runner.invoke(
        scan_planets,
        ["-d", "tests/data", "-o", "./tests", *(terrains if terrains else [])],
    )


def test_scan_planets_no_terrain():
    result = invoke_scan_planets()
    assert result.exit_code == 0
    assert "No terrain specified, generating for all terrains" in result.output
    assert "planets_all.csv" in os.listdir("./tests")
    assert "./tests/planets_all.csv" in result.output


def test_scan_planets_with_terrain():
    result = invoke_scan_planets(["mountains"])
    assert result.exit_code == 0
    assert "Generating CSV for terrains: mountains" in result.output
    assert "planets_mountains.csv" in os.listdir("./tests")
    assert "./tests/planets_mountains.csv" in result.output


def test_scan_planets_contains_appropriate_header_row():
    result = invoke_scan_planets(["mountains"])
    assert result.exit_code == 0
    data = get_csv_data("tests/planets_mountains.csv")
    assert data[0] == ["name", "terrain", "population"]


def test_scan_planets_contains_data_elements():
    result = invoke_scan_planets(["mountains"])
    assert result.exit_code == 0
    data = get_csv_data("tests/planets_mountains.csv")
    assert all(len(row) == 3 for row in data[1:])
    assert all(
        sum(len(s) for s in row) >= 3 for row in data[1:]
    )  # assert non-empty cells


def test_scan_is_pipe_delimited():
    result = invoke_scan_planets(["mountains"])
    assert result.exit_code == 0
    data = get_csv_data("tests/planets_mountains.csv")
    assert data[0][0] == "name"


def test_scan_planets_contains_quotes():
    result = invoke_scan_planets(["mountains"])
    assert result.exit_code == 0
    data = get_csv_data("tests/planets_mountains.csv")
    assert all(
        cell.startswith('"') and cell.endswith('"') for row in data[1:] for cell in row
    )


def test_scan_planets_is_accurate():
    result = invoke_scan_planets(["mountains"])
    assert result.exit_code == 0
    data = get_csv_data("tests/planets_mountains.csv")
    expected_names = [
        "Alderaan",
        "Endor",
        "Naboo",
        "Coruscant",
        "Mustafar",
        "Mygeeto",
        "Cato Neimoidia",
        "Saleucami",
        "Dantooine",
        "Trandosha",
        "Socorro",
    ]
    for i, name in enumerate(expected_names):
        assert data[i + 1][0] == f'"{name}"'
