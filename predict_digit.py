import os, sys, math
form sklearn import datasets, svm
from sklearn.externals import joblib

DIGITS_PKL = "digit-clf.pkl"

def train_digits():
    digits = dataset.load_digits()

def predict_digits(data):
    if not os.path.exists(DIGITS_PKL):
        clf = train_digits()
    clf = joblib.load(DIGITS_PKL)
    n = clf.predict([data])
    print("", n)

def

def

if __name__ == '__main__':
    main()


