import os
from submission_script import *
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
from dataset_script import dataset
from sklearn.metrics import accuracy_score

os.environ['OPENBLAS_NUM_THREADS'] = '1'

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    percent = int(input())
    criteria = input()
    acc_value = 1 - float(percent / 100)

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[int(acc_value * len(dataset)):]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[:int(acc_value * len(dataset))]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    train_x = encoder.transform(train_x)
    test_x = encoder.transform(test_x)

    classifier = DecisionTreeClassifier(criterion=criteria, random_state=0)
    classifier.fit(train_x, train_y)

    predictions = classifier.predict(test_x)
    accuracy = accuracy_score(test_y, predictions)

    stuff = list(classifier.feature_importances_)

    print("Depth: " + str(classifier.get_depth()))
    print("Number of leaves: " + str(classifier.get_n_leaves()))
    print("Accuracy: " + str(accuracy))
    print("Most important feature: " + str(stuff.index(max(stuff))))
    print("Least important feature: " + str(stuff.index(min(stuff))))

    submit_train_data(train_x, train_y)
    submit_test_data(test_x, test_y)
    submit_classifier(classifier)
    submit_encoder(encoder)
