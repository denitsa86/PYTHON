import random
from multiprocessing import Pool


def calculate_square(n):
    return f"{n} ** 2 = {n ** 2}"


if __name__ == "__main__":
    numbers = [random.randint(0, 1000) for _ in range(100000)]

    with Pool(processes=16) as pool:
        results = pool.map(calculate_square, numbers) # ot imap_unordered

    print(results)
