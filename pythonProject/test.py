x = 56


def a():
    x = 50

    def b():
        x = 1

        def c():
            global x
            print(x)

        c()
    b()


a()
print(x)