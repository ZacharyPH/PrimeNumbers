import os
import h5py
import numpy as np


def init_hdf():
    newpath = "./HDF/"
    with h5py.File(newpath + "Primes" + ".hdf5", "w") as hdf:
        hdf.create_dataset("Primes", (50 * 1000 * 1000,), data=np.zeros(50 * 1000 * 1000), dtype="i", chunks=True)


def fill_hdf():
    d = h5py.File("./HDF/" + "Primes" + ".hdf5", "r+")
    path = "./Millions/"
    for (_, _, filenames) in os.walk(path):
        for i, file in enumerate(filenames):
            print(file, end="\r")
            with open(path + file, "r") as f:
                d["Primes"][i * 1000 * 1000: (i + 1) * 1000 * 1000, ] = np.array([int(p) for p in f.read().split(",")])
    return d


def open_hdf():
    return h5py.File("./HDF/" + "Primes" + ".hdf5", "r")


def main():
    init_hdf()
    d = fill_hdf()
    d = open_hdf()
    print(d["Primes"][40 * 1000 * 1000 + 15: 40 * 1000 * 1000 + 28])
    pass


if __name__ == "__main__":
    main()
