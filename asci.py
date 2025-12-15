def teglalap(sz, m):
    for sorszam in range(m):
        print("*", end="")

        if sorszam == 0 or sorszam == m - 1:
            print("*" * (sz - 2), end="")
        else:
            print(" " * (sz - 2), end="")

        print("*")


teglalap(8, 5)