import sys


def rotations(s, start=1):
    "return the rotations of string s"
    l = len(s)
    for i in range(start, l):
        yield s[i:l] + s[0:i]


def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (
        baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


primes = set()

for line in sys.stdin:
    primes.add(int(line))

base = 2

for base in range(2, 17):
    found = set()
    for p in primes:
        if p not in found:
            s = baseN(p, base)
            ok = True
            for r in rotations(s):
                test = int(r, base)
                if test not in primes:
                    ok = False
                    break
            if ok:
                rots = list(rotations(s, 0))
                base_10_rots = [int(rotation, base) for rotation in rots]
                for rotation in rots:
                    found.add(int(rotation, base))
                print(base,
                      '[' + ", ".join(sorted(list(set(rots)))) + ']',
                      sorted(list(set(base_10_rots))), )
                sys.stdout.flush()
