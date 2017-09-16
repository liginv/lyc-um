def tables(m, n):
    for i in range(1, n + 1):
        result = m * i
        # print("{} X {} = {}".format(m,i,result)) # old way of doing - python 2.7 to 3.4
        print(f"{m} X {i} = {result}")  # works in 3.6 onwards


def biggest(a, b):
    if a > b:
        return(a)
    else:
        return(b)


def biggest3(a, b, c):
    if a > b:
        if a > c:
            return(a)
        else:
            return(c)
    elif b > c:
        return(b)
    else:
        return(c)


def biggest_in(l):
    result = l[0]
    for i in l[1:]:
        if i > result:
            result = i
    return result


def smallest_in(l):
    result = l[0]
    for i in l[1:]:
        if i < result:
            result = i
    return result


def fizzbizz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("fizzbizz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("bizz")
        else:
            print(i)


def panagram(s):
    txt = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in txt:
            return False
    return True


def table_grid(n):
    for i in range(1, n + 1):
        print(f"\t{i}", end='')

    for i in range(1, n + 1):
        print("\n")  # print by default add a new line so print("\n") give two new line.
        print(f"\n{i}", end='')
        for j in range(1, n + 1):
            result = i * j
            print(f"\t{result}", end='')
    print("\n")


def freq(s):
    letters = {}
    for i in s:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1
    return letters


# def primes(n):
#     primes = list(range(2, n + 1))    
#     for i in primes:
#         p = i
#         for i in primes:
#             primes = [x for x in primes if x != p * i]
#     return primes

def primes(n):
    primes = set(range(2, n + 1))
    cancelled = set()
    for i in primes:
        if i not in cancelled:
            for j in range(i + i, n + 1, i):
                cancelled.add(j)
    # return primes.difference(cancelled)
    return sorted((primes - cancelled))