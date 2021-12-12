if __name__ == '__main__':
    N = int(raw_input())
students_data = {}
for i in range(N):
    a = raw_input().split(' ')
    students_data[a[0]] = [float(x) for x in a[1:]]
student = raw_input()
mark = 0
for i in students_data[student]:
    mark = mark + i
    average = mark/3
print "%.2f" %(average)
