def outer():
    count = 0

    def inner():
        nonlocal count
        count = count + 1

    inner()
    print(count)

outer()