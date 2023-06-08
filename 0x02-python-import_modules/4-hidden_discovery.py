#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    Names = dir(hidden_4)
    for i in Names:
        if i[0] != "_" and i[1] != "_":
            print(i)
