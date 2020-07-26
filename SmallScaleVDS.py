import h5py

# f0 =  h5py.File("0.h5", "w")
# a = f0.create_dataset("d", shape=(3, 1), dtype="i", data=[1, 2, 3])
#
# f1 = h5py.File("1.h5", "w")
# b = f1.create_dataset("d", shape=(3, 1), dtype="i", data=[4, 5, 6])
#
# layout = h5py.VirtualLayout(shape=(2, 3), dtype="i")
#
# layout[0, :] = h5py.VirtualSource(a)
# layout[1, :] = h5py.VirtualSource(b)
#
# with h5py.File("01.h5", "w" ) as f:
#     f.create_virtual_dataset("data", layout=layout)
#     pass


def init_virtual_hdf():
    hdf_path = "./HDF/"
    d = h5py.File(hdf_path + "Primes" + ".h5vd", "r+")
    layout = h5py.VirtualLayout(shape=(50, 1000 * 1000), dtype="u4")
    for n in range(50):
        with h5py.File(hdf_path + f"{n}.h5", "r") as f:
            layout[n] = h5py.VirtualSource(f["Primes"])

    with h5py.File(hdf_path + "Primes.h5vd", "w") as f:
        f.create_virtual_dataset("Primes", layout)
    # TODO: Current - if this works, move on to piecing in the virtual datasets with non-downloaded data
    # TODO: Also, cleanup main code to allow simple access, rather than currently defined iterators on a per-instance basis


def open_hdf():
    return h5py.File("./HDF/" + "Primes" + ".h5vd", "r")


def main():
    init_virtual_hdf()
    d = open_hdf()

    input("End reached!")
    d.close()


if __name__ == "__main__":
    main()
