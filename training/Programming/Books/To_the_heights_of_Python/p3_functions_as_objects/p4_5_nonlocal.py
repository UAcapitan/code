
def make_average():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total

        count += 1
        total += new_value

        return total / count
    
    return averager

if __name__ == "__main__":
    avg = make_average()

    print(avg(10))
    print(avg(100))
    print(avg(25))
