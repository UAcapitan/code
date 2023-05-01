
import time
import random
from tqdm import tqdm


if __name__ == "__main__":
    list_ = [1,2,3,4,5,6,7,8,9]
    for i in tqdm(list_):
        print(i)
        time.sleep(random.randint(1,3))
