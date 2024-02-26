# Planetary Scanner

## Overview
Using the provided data files containing data in json format, create a simple CSV file generator to support the following functionality: 

> A user should be able to run the file generator via the command line. The file generator should accept an argument with a terrain value. The file generator should read in the planet data from the provided data files, and output a CSV file containing only data for planets that have the terrain value specified in the input. If no terrain value is provided, output a CSV file with data for all planets. You can use any language you'd like (python, .net core, node js, ruby, etc).
## Setup

To setup and activate the virtual environment, run:
```shell
source ./setup.sh
```

## Execution

```shell
./scanplanets
```

```
Usage: scanplanets [OPTIONS] [TERRAIN]...

Options:
  -d, --data-dir TEXT    Data directory path
  -o, --output-dir TEXT  Output CSV filename
  --throttle FLOAT       Throttle in seconds
  -t, --display-table    Display output as table
  --help                 Show this message and exit.
```

## Testing

After running [setup](#setup), install test dependencies:

```shell
pip install -r requirements-test.txt
```


## Development

After running [setup](#setup), install dev dependencies:

```shell
pip install -r requirements-dev.txt
```

## Notes and Technical Requirements: 

- The file generator should output a message to the console with the terrain value it received, or output a message that it did not receive a terrain value 
- The file generator should output a message to the console when finished, and the message should include the name of the CSV file it created 
- The CSV file should be named for the terrain, i.e. mountains.csv 
- The CSV file should be named appropriately if no terrain value is received 
- The CSV file should contain the following- data elements for each planet: name, terrain, population 
- The CSV file should contain an appropriate header row 
- The CSV file should be delimited with a pipe (|) 
- The CSV file should contain quotes around all data values