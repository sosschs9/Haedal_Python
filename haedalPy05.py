import turtle as t

f = open("data.txt", "r")
length = int(f.readline())
angle = int(f.readline())

t.shape('turtle')
for i in range(4):
    t.forward(length)
    t.right(angle)
