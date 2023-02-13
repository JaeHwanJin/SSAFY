def recursive(data):
    if data < 0:
        print("끝!")
    else:
        print(data)
        recursive(data - 1)
        print("returned", data)


recursive(4)