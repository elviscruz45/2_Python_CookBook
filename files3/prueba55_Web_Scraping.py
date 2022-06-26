import sys


print(sys.stdin)

for line in sys.stdin:
	if 'q' == line.rstrip():
		break
	print(f'Input : {line}')

print("Exit")


for i in sys.stdin:
    print(i)