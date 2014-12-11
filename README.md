Egyptian Fraction Generator
===========================
A small script used to generate Egyptian fraction solutions for the [Erdős–Straus conjecture](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture).

Usage
-----
Assuming you're trying to find solutions for `n` given `4/n = 1/x + 1/y + 1/z`:
```shell
$python egyptian_fractions.py <n>
```
Will print out solutions for your `4/n`.

Example
-------
```
$python egyptian_fractions.py 9
Finding x,y,z for 9
1/3 1/10 1/90
1/3 1/12 1/36
1/4 1/6 1/36
1/4 1/9 1/12

Time taken: 0:00:00.002382
```
