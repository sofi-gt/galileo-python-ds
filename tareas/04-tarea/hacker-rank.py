
def ifelse(n):
    if n % 2 != 0:
        print("Weird")
    
    elif  2 <= n <= 5:
        print("Not Weird")

    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird") 

ifelse(3)
ifelse(24)


def aritmetic(a, b):
    print(a + b)
    print(a - b)
    print(a * b)

aritmetic(3, 2)

def division(a, b):
    print(a // b)
    print(a / b)

division(3, 5)

def loops(n):
    for i in range(0, n):
        print(i ** 2)

loops(3)

def is_leap(year):
    leap = False

    # Write logic here

    # it is leap year if it is evenly divided by 4
    if year % 4 == 0:
        leap = True
    # it is no leap year if it is evenly divided by 100
    if year % 100 == 0:
        leap = False
    # it is leap year if it is evenly divisible by 400
    if year % 400 == 0:
        leap = True

    return leap

is_leap(1990)
is_leap(2000)
is_leap(1800)


def runner_up(n, A):
    A.sort()
    x = max(A)
    m = A.count(x)
    i = m - n
    hi = A[i]
    return hi

runner_up(5, [2, 3, 6, 6, 5])

## how the fuck with map
#if __name__ == '__main__':
 #   n = int(raw_input())
  #  arr = map(int, raw_input().split())

# input
# 4
#57 57 -57 57

#output
# -57

# if __name__ == '__main__':
#     n = int(raw_input())
#     arr = map(int, raw_input().split())
    
#     x = max(arr)
#     count = arr.count(x)
    
#     for i in range(count):
#         arr.remove(x)
#     print(max(arr))
    


def main():
    n = 3
    students = """
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60 """
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = 'Malika'

    student = student_marks[query_name]

    mark_sum = 0
    for mark in student:
        mark_sum += mark

    average_mark = mark_sum / len(student)
    print("{:.2f}".format(average_mark))

## lists
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

def run_commands():
N = int(input())
    numbers = []
    commands = []
    output_list = []
    for _ in range(N):
        x = input().split()
        name, *line = x
        numbers.append(line)
        commands.append(name)

    for i in range(len(commands)):
        if commands[i] == 'insert':
            output_list.insert(int(numbers[i][0]), int(numbers[i][1]))
        elif commands[i] == 'print':
            print(output_list)
        elif commands[i] == 'remove':
            output_list.remove(int(numbers[i][0])) 
        elif commands[i] == 'append':
            output_list.append(int(numbers[i][0]))
        elif commands[i] == 'sort':
            output_list.sort()
        elif commands[i] == 'pop':
            output_list.pop(-1)
        elif commands[i] == 'reverse':
            output_list.reverse()     

    return output_list




## tuple
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    
    print(hash(t))

## floor ceiling
import numpy as np
np.set_printoptions(legacy='1.13')
arr = np.array(input().split(),float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))

## arrays
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.flip(numpy.array(arr, float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


## zeroes and ones
import numpy

arr = numpy.array(input().split(),int)
print(numpy.zeros(arr, int))
print(numpy.ones(arr, int))


## defaultdic
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print (i)

# The * in python is used to unpack the iterable.
# The or condition returns the first true value
# The * is evaluated at last. First it will evaluate [] or [-1]. So our code becomes

from collections import defaultdict
n,m = list(map(int,input().split()))
d = defaultdict(list)
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    print(*d[input()] or [-1])

## counter 
from collections import Counter
myList = ['a','a','b','c','d','e','c','b','c','d','b','a','b','c']
print (Counter(myList))
print (Counter(myList).items())
print (Counter(myList).keys())
print (Counter(myList).values())

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

x = int(input().strip())
from collections import Counter
sizes = Counter(map(int, input().split()))
n = int(input().strip())
customer_size = []
customer_price = []
money = 0
for _ in range(n):
    x = map(int, input().split())
    size, price = x

    if sizes[size] > 0:
        money += price
        sizes[size] -= 1

print(money)


## minimum swaps
def minimumSwaps(arr):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

# Complete the minimumSwaps function below.
def minimumSwaps(arr,n,swaps=0):
    #iterate over entire array
    for i in range(0,n):
        #it's good practice to use a boolean guided function in a long for loop,
        #while will evaluate and IF the statement in it is true it will continue
        #I used the consecutive, increasing values to swap by index
        while arr[i] != (i+1):
            #temp is the correct index of arr[i]
            temp = arr[i]-1
            #swap this with whatever element is where arr[temp] is, this will
            #continue to swap until arr[i] == index+1
            arr[i], arr[temp] = arr[temp], arr[i]
            #increase swaps
            swaps+=1
    return swaps

def minimumSwaps(arr):
    res = 0
    arr = [x-1 for x in arr]
    value_idx = {x:i for i, x in enumerate(arr)}
    for i, x in enumerate(arr):
        if i != x:
            to_swap_idx = value_idx[i]
            arr[i], arr[to_swap_idx] = i, x
            value_idx[i] = i
            value_idx[x] = to_swap_idx
            res += 1
    print(res)
    return res

def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
        while arr[i] != (i+1):
            temp = arr[i]-1
            arr[i], arr[temp] = arr[temp], arr[i]
            swaps+=1
    return swaps


    ## bubble sort
n = 3
a = [3 , 1]
for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        print(a)
        }
    }
    
}

n = 3
a = [3 , 2, 1]
swaps = 0
for i in range(0, n):
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
            swaps += 1
    i += 1
print(a, swaps)

n = int(input())

a = list(map(int, input().rstrip().split()))
def countSwaps(a):
    n = len(a)
    swaps = 0
    for i in range(0, n):
        for j in range(0, n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                j += 1
                swaps += 1
        i += 1
    print("Array is sorted in {swaps} swaps.".format(swaps = swaps))
    print("First Element: {first}".format(first = a[0]))
    print("Last Element: {last}".format(last = a[-1]))
