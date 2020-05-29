for i in range(1, 50 + 1):
    print(i)
    with open(f"./Millions/{i}.csv", "r") as f:
        l = [int(i) for i in f.readline().strip("\n").split(",")]
    for j in range(1, 10 + 1):
        with open(f"./HundredThousands/{10 * (i - 1) + j}.csv", "w") as o:
            o.write(str(l[:100 * 1000]).replace(" ", "")[1:-1])
            del l[:100 * 1000]
