import os

from src.planetary_archive import PlanetaryArchive


TEST_DATA_DIR = "tests/data"


def test_archive_init():
    archive = PlanetaryArchive(TEST_DATA_DIR)
    assert archive.dir_path == os.path.abspath(TEST_DATA_DIR)

def test_archive_length():
    archive = PlanetaryArchive(TEST_DATA_DIR)
    assert len(archive) == 30

def test_archive_iter_matches_length():
    archive = PlanetaryArchive(TEST_DATA_DIR)
    planets = list(archive)
    assert len(planets) == len(archive)