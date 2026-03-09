def speel_timer(fun):
    def wrapper():
        print(f'casting {fun.__name__}')
        fun()

    return wrapper


@speel_timer
def hello():
    print("hello world !")


hello()