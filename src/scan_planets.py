import click

from .planetary_archive import PlanetaryArchive
from .planetary_scanner import PlanetaryScanner
from .table import Table


@click.command()
@click.argument("terrain", nargs=-1, required=False)
@click.option("--data-dir", "-d", default="./data", help="Data directory path")
@click.option("--output-dir", "-o", default=".", help="Output CSV filename")
@click.option("--throttle", default=0.0, help="Throttle in seconds")
@click.option("--display-table", "-t", is_flag=True, help="Display output as table")
def scan_planets(terrain, data_dir, throttle, display_table, output_dir):
    if not terrain:
        click.echo("No terrain specified, generating for all terrains")
    click.echo(
        f"Generating CSV for terrains: {', '.join(terrain) if terrain else 'all'}"
    )
    archive = PlanetaryArchive(data_dir)
    scanner = PlanetaryScanner(output_dir=output_dir)
    scanner.scan(terrain, archive, throttle=throttle)
    click.echo(f"Scanned {len(archive)} planets")
    filename = scanner.filename
    click.echo(f"Generated CSV at {filename}")

    if display_table:
        table = Table.from_csv(filename)
        table.display()