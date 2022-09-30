
import bisect


def grade(score, breakpoints=[60,70,80,90], grades='FDCBA'):
    ind = bisect.bisect(breakpoints, score)
    return grades[ind]


if __name__ == "__main__":
    print([grade(n) for n in [31, 25, 67, 90, 22, 88, 90]])
