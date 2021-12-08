# first-fit

Given a maximum rod size and list of segments, [first-fit.py](first-fit.py) uses a first fit decreasing bin packing algorithm to pack those segments into rods of the size indicated.

## Requirements

[first-fit.py](first-fit.py) requires [Python 3](https://www.python.org/download/releases/3.0/). It can also be run in [Docker](https://docker.com).

## Usage

```
$ ./first-fit.py -h
usage: first-fit.py [-h] --rod_size ROD_SIZE --segments SEGMENTS [--version]

Use first fit decreasing algorithm for bin packing.

optional arguments:
  -h, --help           show this help message and exit
  --rod_size ROD_SIZE  Rod size - e.g.: 20
  --segments SEGMENTS  List of segment lengths specified by a space - e.g.: 5 12
                       8 4 15 10
  --version            Version
```

## Example usage

### Using command line arguments:
```
$ ./first-fit.py --rod_size 20 --segments "5 12 15 15 4 8 3"

Segments: [15, 15, 12, 8, 5, 4, 3]
Rod size: 20

Rods:
[15, 5]
[15, 4]
[12, 8]
[3]
```

### Using environment variables:

```
$ RODSIZE=25 SEGMENTS="1 17 5 3 2 9" ./first-fit.py 

Segments: [17, 9, 5, 3, 2, 1]
Rod size: 25

Rods:
[17, 5, 3]
[9, 2, 1]
```

### When a segment size is too large for the rod size specified:

```
$ RODSIZE=10 SEGMENTS="1 5 21 8 2 4 8 11" ./first-fit.py 

Segments: [21, 11, 8, 8, 5, 4, 2, 1]
Rod size: 10

Error: Segment of length 21 is too large for rod size 10.
Error: Segment of length 11 is too large for rod size 10.
Rods:
[8, 2]
[8, 1]
[5, 4]
```

### Error handling.

```
$ ./first-fit.py --rod_size two --segments "5 12 15 15 4 8 3"
Error: Invalid rod size: 'two'.
       Rod size must be specified as an integer.
```

```
$ ./first-fit.py --rod_size 20 --segments "5 12 15 15 4 8 3f"
Error: Invalid segment specified: '5 12 15 15 4 8 3f'.
       Segments must be specified as integers separated by spaces.
```

## Running using the docker image:

```
$ docker run -e RODSIZE=20 -e SEGMENTS="1 15 12 9 3" ykhemani/first-fit:0.0.1

Segments: [15, 12, 9, 3, 1]
Rod size: 20

Rods:
[15, 3, 1]
[12]
[9]
```

---
