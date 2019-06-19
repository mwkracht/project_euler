# Project Euler
Python solutions to Project Euler Problems

This repository contains a set of small python applications which provide solutions to problems found on (Project Euler)[https://www.projecteuler.net]. The username associated with these solutions is `mwkracht`. The set of solutions is not complete nor is it guaranteed to be the most efficient solution. Problems will continue to be added overtime.

The solutions are laid out such that each problem will have a single solution module within the `project_euler` sub-directory of this repository. For example, the solution Problem 1 can be found at `project_euler/problem_001.py`. 

To simplify imports within the package, the project_euler package must be first installed via `pip` prior to running any problem solutions. The package will install a simple script that wraps all problem solutions via CLI: 

```
usage: project_euler [-h] problem [executions]

Run a specific project euler solution.

positional arguments:
  problem     Problem number
  executions  Times to execute solution for timing purposes

optional arguments:
  -h, --help  show this help message and exit
```

All solutions have been run on python 3.6.
