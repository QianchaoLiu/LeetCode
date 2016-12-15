def primes_num(n):
    if n <3:
        return 0
    digits = [1]*n
    digits[0] = digits[1] = 0
    for i in xrange(2, int(n**0.5)+1):
        if digits[i] == 1:
            for j in xrange(i+i, n, i):
                digits[j] = 0
    return sum(digits)

print primes_num(2)