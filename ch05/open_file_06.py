import io

s = io.StringIO()

print(s.write('Hello World\n'))
print('Hello print\n', file=s)

print(s.getvalue())

s2 = io.StringIO("Hello World\n")

print(s2.read(4))
print(s2.read())
