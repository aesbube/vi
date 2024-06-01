from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score

import os
# from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    train_set = dataset[:int(0.75 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(0.75 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    encoder = OrdinalEncoder()
    enc_train_x = encoder.fit_transform(train_x)
    enc_test_x = encoder.transform(test_x)

    classifier = CategoricalNB()

    classifier.fit(enc_train_x, train_y)

    predictions = classifier.predict(enc_test_x)

    print(accuracy_score(test_y, predictions))

    new_input = input().split(' ')
    new_enc_x = encoder.transform([new_input])

    prediction = classifier.predict(new_enc_x)
    print(prediction[0])

    probs = classifier.predict_proba(new_enc_x)
    print(probs)

    # submit_train_data(enc_train_x, train_y)
    # submit_test_data(enc_test_x, test_y)
    # submit_classifier(classifier)
    # submit_encoder(encoder)
