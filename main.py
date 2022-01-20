from cProfile import run


def run():
    i = 1
    for i in range(1,100):
        print (i)

if __name__ == '__main__':
    run()