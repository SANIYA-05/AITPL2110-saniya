import matplotlib.pyplot as p
x=[1,8,27,64,125]
y=[1,4,9,16,25]
a = [1,3,5,7]
b = [2,4,6,8]
lines = p.plot(x,y,a,b)
p.setp(lines[0], color = 'r')
p.setp(lines[1], color = 'g')
p.ylabel("y-axis")
p.xlabel("x-axis")
p.title("Graph 1")
# p.plot(x,y,linewidth=6)
p.grid()
p.show()
