from sgd_alg.context.reservoir_sampling import reservoir_sampling


def ex_reservoir_sampling():
    li = list(range(100))
    print(reservoir_sampling(li, keep_num=1))
    print(reservoir_sampling(li, keep_num=15))


if __name__ == '__main__':
    ex_reservoir_sampling()
