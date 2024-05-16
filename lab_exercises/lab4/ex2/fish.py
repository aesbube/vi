import os
from submission_script import *
from dataset_script import dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

os.environ['OPENBLAS_NUM_THREADS'] = '1'

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    col_index = int(input())
    num_trees = int(input())
    criteria = input()

    train_set = [row[:col_index] + row[col_index + 1:] for row in dataset[:int(0.85 * len(dataset))]]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = [row[:col_index] + row[col_index + 1:] for row in dataset[int(0.85 * len(dataset)):]]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = RandomForestClassifier(criterion=criteria, n_estimators=num_trees, random_state=0)
    classifier.fit(train_x, train_y)

    predictions = classifier.predict(test_x)
    accuracy = accuracy_score(test_y, predictions)

    new_input = list(int(number) for number in input().split())
    new_input = [new_input[:col_index] + new_input[col_index + 1:]]

    print("Accuracy: " + str(accuracy))
    print(classifier.predict(new_input)[0])
    print(classifier.predict_proba(new_input)[0])

    submit_train_data(train_x, train_y)
    submit_test_data(test_x, test_y)
    submit_classifier(classifier)

