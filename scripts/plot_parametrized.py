#!/usr/bin/python

"""This program shows parametrized `hyperfine` benchmark results as an
errorbar plot."""

import argparse
import json
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("file", help="JSON file with benchmark results", nargs="+")
parser.add_argument(
    "--parameter-name",
    metavar="name",
    type=str,
    help="Name of the parameter / x-axis label",
)
args = parser.parse_args()

for filename in args.file:
    with open(filename) as f:
        results = json.load(f)["results"]

    parameter_values = [float(b["parameter"]) for b in results]
    times_mean = [b["mean"] for b in results]
    times_stddev = [b["stddev"] for b in results]

    plt.errorbar(x=parameter_values, y=times_mean, yerr=times_stddev, capsize=2)

plt.xlabel(args.parameter_name)
plt.ylabel("Time [s]")
plt.ylim(0, None)
plt.show()
