import csv
import pytest

@pytest.fixture
def mock_csv_writer(mocker):
    class MockDictWriter:
        def __init__(self, *args, **kwargs):
            pass

        def writeheader(self):
            pass

        def writerow(self, row):
            pass

    mocker.patch("csv.DictWriter", MockDictWriter)
