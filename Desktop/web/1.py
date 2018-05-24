file_in = open("input.txt", "r")
file_out = open("output.txt", "w")
a,b = map(int, file_in.readline().strip().split())
res = a + b
print(res, file = file_out)
file_in.close()
file_out.close()
