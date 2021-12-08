# first-fit

Given a maximum rod size and list of segments, [first-fit.py](first-fit.py) uses a first fit decreasing bin packing algorithm to pack those segments into rods of the size indicated.

## Requirements

[first-fit.py](first-fit.py) requires [Python 3](https://www.python.org/download/releases/3.0/). It can also be run in [Docker](https://docker.com).

## Usage

```
$ ./first-fit.py -h
usage: first-fit.py [-h] --rod_size ROD_SIZE [--kerf KERF] --segments SEGMENTS
                    [--version]

Use first fit decreasing algorithm for bin packing.

optional arguments:
  -h, --help           show this help message and exit
  --rod_size ROD_SIZE  Rod size - e.g.: 20
  --kerf KERF          Kerf - e.g.: 1/8 or 0.125
  --segments SEGMENTS  List of segment lengths specified by a space - e.g.: 5 12
                       8 4 15 10
  --version            Version
```

## Example usage

### Using command line arguments:
```
$ ./first-fit.py --rod_size 20 --segments "5 12 15 15 4 8 3"

Segments: [15.0, 15.0, 12.0, 8.0, 5.0, 4.0, 3.0]
Rod size: 20.0
Kerf: 0.125

Rods:
[15.0, 4.0]
  waste: 0.75
  loss for kerf: 0.25
[15.0, 3.0]
  waste: 1.75
  loss for kerf: 0.25
[12.0, 5.0]
  waste: 2.75
  loss for kerf: 0.25
[8.0]
  waste: 11.875
  loss for kerf: 0.125
```

### Using environment variables:

```
$ RODSIZE=25 SEGMENTS="1 17 5 3 2 9" ./first-fit.py

Segments: [17.0, 9.0, 5.0, 3.0, 2.0, 1.0]
Rod size: 25.0
Kerf: 0.125

Rods:
[17.0, 5.0, 2.0]
  waste: 0.625
  loss for kerf: 0.375
[9.0, 3.0, 1.0]
  waste: 11.625
  loss for kerf: 0.375
```

### Specifying kerf other than the default:

```
$ ./first-fit.py --rod_size 20 --segments "5 12 15 15 4 8 3" --kerf 1/16 

Segments: [15.0, 15.0, 12.0, 8.0, 5.0, 4.0, 3.0]
Rod size: 20.0
Kerf: 0.0625

Rods:
[15.0, 4.0]
  waste: 0.875
  loss for kerf: 0.125
[15.0, 3.0]
  waste: 1.875
  loss for kerf: 0.125
[12.0, 5.0]
  waste: 2.875
  loss for kerf: 0.125
[8.0]
  waste: 11.9375
  loss for kerf: 0.0625
```

### When a segment size is too large for the rod size specified:

```
$ RODSIZE=10 SEGMENTS="1 5 21 8 2 4 8 11" ./first-fit.py

Segments: [21.0, 11.0, 8.0, 8.0, 5.0, 4.0, 2.0, 1.0]
Rod size: 10.0
Kerf: 0.125

Error: Segment of length 21.0 is too large for rod size 10.0.
Error: Segment of length 11.0 is too large for rod size 10.0.
Rods:
[8.0, 1.0]
  waste: 0.75
  loss for kerf: 0.25
[8.0]
  waste: 1.875
  loss for kerf: 0.125
[5.0, 4.0]
  waste: 0.75
  loss for kerf: 0.25
[2.0]
  waste: 7.875
  loss for kerf: 0.125
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
$ docker run -e RODSIZE=20 -e SEGMENTS="1 15 12 9 3" ykhemani/first-fit:0.0.3

Segments: [15.0, 12.0, 9.0, 3.0, 1.0]
Rod size: 20.0
Kerf: 0.125

Rods:
[15.0, 3.0, 1.0]
  waste: 0.625
  loss for kerf: 0.375
[12.0]
  waste: 7.875
  loss for kerf: 0.125
[9.0]
  waste: 10.875
  loss for kerf: 0.125
```

---
