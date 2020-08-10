import h5py


def init_virtual_hdf():
    hdf_path = "./HDF/"
    layout = h5py.VirtualLayout(shape=(50, 1000 * 1000), dtype="u4")
    for n in range(50):
        with h5py.File(hdf_path + f"{n}.h5", "r") as f:
            layout[n] = h5py.VirtualSource(f["Primes"])

    with h5py.File(hdf_path + "Primes.h5vd", "w") as f:
        f.create_virtual_dataset("Primes", layout)


def open_hdf():
    return h5py.File("./HDF/" + "Primes" + ".h5vd", "r")


def main():
    init_virtual_hdf()
    d = open_hdf()
    d.close()


if __name__ == "__main__":
    main()
