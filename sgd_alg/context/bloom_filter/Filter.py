class BF_Model:
    def __init__(self, hit_bit=10, ):
        self.hit_bit = hit_bit

    def fit(self, x):
        return self

    def predict(self, target):
        isIn = False
        return isIn


if __name__ == '__main__':
    clf = BF_Model(4)
    clf.fit(3).predict(1)
    print(int(1e2))