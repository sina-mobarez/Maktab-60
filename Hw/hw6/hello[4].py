# get a word and add "hello" to it
def hello(w):
    n = "hello " + w
    return n


words = ["Jane", "Lee", "Will", "Brie"]

# using map function to change a list
hel = list(map(hello, words))

print(hel)
