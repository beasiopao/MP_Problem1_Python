import matplotlib.pyplot as plt

n = list(range(100))
pts=[]

def graph_function():
    for x in range(100):
        f=(x**2)-7
        if x<=9:
            pts.append(f)
        elif x>=10:
            while x>=10:
                x = x-10
            if x<=9:
                f = (x**2)-7
                pts.append(f)
    return x

graph_function()

plt.title('Graph of f(n)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.stem(n,pts,'-', use_line_collection = True)

# Description and comments on the graph f(n):
# The produced graph of the piece-wise function f(n)
# shows a recurring pattern for every 10 indices.
# The lowest points of the graph are found at the
# -7 y-axis while its highest points are found at
# the +74 y-axis. 