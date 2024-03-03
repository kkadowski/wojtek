


def suma(*args, ** kwargs):
    for i in args:
        print(i)
    return sum(args)



print(suma(1,3,4,34,12,12,123))



