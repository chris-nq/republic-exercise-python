#!/usr/bin/python3

import click

from planet_data import PlanetData
from csv_generator import CSVGenerator

@click.command()
@click.argument("terrain", nargs=-1, required=False)
def main(terrain):
    data = PlanetData("/home/chris/Documents/projects/republic-exam/static")
    csv_gen = CSVGenerator()
    csv_gen.generate(terrain, data)

if __name__ == "__main__":
    main()