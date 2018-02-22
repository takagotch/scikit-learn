from sklearn import datasets, cross_validation, svm, metrics

digits = datasets.load_digits()

data_train, data_test, label_train, label_test = \
        cross_validation.train_test_split(digits.data, digits.target)

clf = svm.SVC(gamma=0.001)
clf.fit(data_train, label_train)

predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_tes, predict)
cl_report = metrics.classification_report(label_test, predict)
print("", clf)
print("", ac_score)
print("", cl_report)

