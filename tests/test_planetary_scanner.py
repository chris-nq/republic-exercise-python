import csv
import pytest

from src.planetary_scanner import PlanetaryScanner
from src.planetary_archive import PlanetaryArchive


def test_planetary_scanner_scan(mocker, mock_csv_writer):
    scanner = PlanetaryScanner()
    archive = PlanetaryArchive("tests/data")
    spy = mocker.spy(csv.DictWriter, "writerow")
    scanner.scan([], archive, throttle=0)
    assert spy.call_count == 30
    