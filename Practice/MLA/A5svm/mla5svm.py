from sklearn import datasets

cancer = datasets.load_breast_cancer()

print("Features : ", cancer.feature_names)
