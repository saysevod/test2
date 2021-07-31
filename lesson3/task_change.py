def main():
    x, y =[int(x) for x in input('Input two numbers x y: ').split()]
    print("x = {}\ny = {}".format(x,y))
    x=x+y
    y=x-y
    x=x-y
    print("Changed x, y\nx = {}\ny = {}".format(x,y))
 # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

