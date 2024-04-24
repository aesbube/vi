from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka
    train_set = dataset[:int(0.85 * len(dataset))]
    train_x = [[float(x) for x in row[:-1]] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(0.85 * len(dataset)):]
    test_x = [[float(x) for x in row[:-1]] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = GaussianNB()

    classifier.fit(train_x, train_y)

    predictions = classifier.predict(test_x)

    print(accuracy_score(test_y, predictions))

    new_input = input().split(' ')
    new_input = [[float(x) for x in new_input]]

    prediction = classifier.predict(new_input)
    print(prediction[0])

    probs = classifier.predict_proba(new_input)
    print(probs)
# for some reason ne raboti so ovie vo coderunner definitivno imaat skill issue
    # submit_train_data(train_x, train_y)
    # submit_test_data(test_x, test_y)
    # submit_classifier(classifier)
