from sklearn import MinMaxScaler, MLPClassifier

# from sklearn.preprocessing import MinMaxScaler
# from sklearn.neural_network import MLPClassifier
# # from sklearn.metrics import accuracy_score

dataset = [[30, 92726, 2.0, 9, 2011, -37.8497, 144.968, 10, 0],
           [43, 95408, 0.0, 12, 2014, -37.8497, 144.968, 10, 0],
           [46, 103831, 0.0, 10, 1996, -37.8497, 144.968, 10, 0],
           [48, 96391, 1.0, 6, 1996, -37.8497, 144.968, 10, 0],
           [14, 96626, 0.0, 7, 1997, -37.8497, 144.968, 10, 0],
           [44, 90673, 4.0, 3, 2001, -37.8497, 144.968, 10, 0],
           [2, 93344, 6.0, 2, 2001, -37.8497, 144.968, 10, 1],
           [3, 86613, 2.0, 7, 2004, -37.8497, 144.968, 10, 0],
           [24, 95978, 0.0, 14, 2007, -37.8497, 144.968, 10, 0],
           [16, 88582, 0.0, 12, 2007, -37.8497, 144.968, 10, 0],
           [25, 97840, 4.0, 5, 2009, -37.8497, 144.968, 10, 1],
           [33, 91548, 37.0, 1, 2010, -37.8497, 144.968, 10, 1],
           [14, 89037, 18.0, 2, 2017, -37.8497, 144.968, 10, 0],
           [49, 87147, 10.0, 5, 2017, -37.8497, 144.968, 10, 0],
           [34, 88661, 0.0, 11, 2017, -37.8497, 144.968, 10, 0],
           [10, 92662, 0.0, 12, 2017, -37.8497, 144.968, 10, 0],
           [44, 88476, 4.0, 8, 2018, -37.8497, 144.968, 10, 0],
           [12, 88817, 15.0, 3, 2018, -37.8497, 144.968, 10, 0],
           [20, 123239, 1.0, 14, 2012, 2.76083, 101.738, 18, 0],
           [6, 149445, 0.0, 20, 2012, 2.76083, 101.738, 18, 0],
           [47, 108947, 0.0, 18, 2012, 2.76083, 101.738, 18, 1],
           [10, 106675, 2.0, 13, 2013, 2.76083, 101.738, 18, 0],
           [18, 107748, 6.0, 10, 2014, 2.76083, 101.738, 18, 0],
           [41, 102863, 6.0, 10, 2000, 2.76083, 101.738, 18, 0],
           [48, 101582, 4.0, 13, 2000, 2.76083, 101.738, 18, 0],
           [4, 103743, 0.0, 13, 2002, 2.76083, 101.738, 18, 0],
           [15, 100757, 8.0, 3, 2003, 2.76083, 101.738, 18, 0],
           [16, 96000, 16.0, 1, 2005, 2.76083, 101.738, 18, 0],
           [33, 96293, 11.0, 2, 2006, 2.76083, 101.738, 18, 0],
           [13, 97531, 1.0, 12, 2006, 2.76083, 101.738, 18, 0],
           [29, 98682, 10.0, 4, 2007, 2.76083, 101.738, 18, 0],
           [20, 97503, 0.0, 14, 2008, 2.76083, 101.738, 18, 1],
           [44, 98972, 0.0, 15, 2008, 2.76083, 101.738, 18, 0],
           [30, 101330, 5.0, 12, 2010, 2.76083, 101.738, 18, 0],
           [6, 97824, 177.0, 4, 2017, 2.76083, 101.738, 18, 0],
           [22, 98534, 32.0, 12, 2017, 2.76083, 101.738, 18, 0],
           [3, 104767, 47.0, 2, 2011, 31.3389, 121.22, 5, 0],
           [14, 105242, 24.0, 6, 2011, 31.3389, 121.22, 5, 1],
           [54, 104162, 0.0, 22, 2011, 31.3389, 121.22, 5, 0],
           [12, 118438, 43.0, 2, 2012, 31.3389, 121.22, 5, 1],
           [19, 119265, 0.0, 18, 2012, 31.3389, 121.22, 5, 1],
           [2, 106865, 0.0, 18, 2013, 31.3389, 121.22, 5, 0],
           [21, 105687, 4.0, 13, 2014, 31.3389, 121.22, 5, 0],
           [33, 92935, 79.0, 3, 2004, 31.3389, 121.22, 5, 0],
           [51, 96102, 11.0, 12, 2004, 31.3389, 121.22, 5, 0],
           [2, 96692, 112.0, 2, 2005, 31.3389, 121.22, 5, 0],
           [15, 108420, 18.0, 11, 2006, 31.3389, 121.22, 5, 0],
           [48, 98312, 19.0, 12, 2008, 31.3389, 121.22, 5, 0],
           [46, 97753, 94.0, 1, 2008, 31.3389, 121.22, 5, 0],
           [4, 166819, 0.0, 16, 2009, 31.3389, 121.22, 5, 0],
           [48, 119617, 15.0, 2, 2009, 31.3389, 121.22, 5, 0],
           [43, 101826, 36.0, 3, 2016, 31.3389, 121.22, 5, 1],
           [41, 97819, 22.0, 7, 2018, 31.3389, 121.22, 5, 0],
           [51, 91808, 6.0, 11, 2011, 40.9517, 29.405, 130, 0],
           [18, 87103, 23.0, 11, 2005, 40.9517, 29.405, 130, 0],
           [56, 86456, 1.0, 22, 2005, 40.9517, 29.405, 130, 0],
           [56, 86111, 35.0, 6, 2005, 40.9517, 29.405, 130, 0],
           [14, 91053, 62.0, 3, 2006, 40.9517, 29.405, 130, 0],
           [27, 90377, 7.0, 13, 2007, 40.9517, 29.405, 130, 0],
           [17, 90050, 8.0, 12, 2007, 40.9517, 29.405, 130, 0],
           [22, 89086, 0.0, 20, 2009, 40.9517, 29.405, 130, 0],
           [16, 93746, 7.0, 12, 2010, 40.9517, 29.405, 130, 0],
           [50, 90329, 67.0, 6, 2010, 40.9517, 29.405, 130, 0],
           [40, 96466, 0.0, 21, 2010, 40.9517, 29.405, 130, 1],
           [33, 90507, 25.0, 7, 2011, 41.57, 2.26111, 109, 1],
           [20, 90895, 19.0, 11, 2012, 41.57, 2.26111, 109, 0],
           [7, 96631, 0.0, 24, 2012, 41.57, 2.26111, 109, 1],
           [55, 87362, 45.0, 5, 2013, 41.57, 2.26111, 109, 0],
           [19, 95594, 26.0, 8, 2013, 41.57, 2.26111, 109, 1],
           [35, 90927, 26.0, 8, 2013, 41.57, 2.26111, 109, 0],
           [36, 91495, 39.0, 6, 2015, 41.57, 2.26111, 109, 0],
           [6, 112326, 7.0, 9, 1996, 41.57, 2.26111, 109, 0],
           [23, 86006, 0.0, 19, 1997, 41.57, 2.26111, 109, 1],
           [17, 85847, 11.0, 4, 1998, 41.57, 2.26111, 109, 0],
           [22, 86845, 11.0, 4, 1998, 41.57, 2.26111, 109, 0],
           [21, 87179, 0.0, 15, 1998, 41.57, 2.26111, 109, 0],
           [36, 88138, 0.0, 19, 1998, 41.57, 2.26111, 109, 0],
           [40, 90758, 0.0, 19, 2000, 41.57, 2.26111, 109, 1],
           [9, 83700, 6.0, 7, 2001, 41.57, 2.26111, 109, 0],
           [29, 84082, 1.0, 12, 2001, 41.57, 2.26111, 109, 1],
           [24, 87723, 2.0, 12, 2002, 41.57, 2.26111, 109, 0],
           [4, 140256, 17.0, 6, 2003, 41.57, 2.26111, 109, 0],
           [50, 85873, 0.0, 19, 2003, 41.57, 2.26111, 109, 0],
           [8, 80702, 1.0, 11, 2004, 41.57, 2.26111, 109, 0],
           [10, 104684, 0.0, 14, 2004, 41.57, 2.26111, 109, 1],
           [47, 77455, 14.0, 4, 2005, 41.57, 2.26111, 109, 0],
           [18, 77390, 14.0, 5, 2005, 41.57, 2.26111, 109, 0],
           [27, 82078, 0.0, 19, 2005, 41.57, 2.26111, 109, 0],
           [20, 77989, 24.0, 4, 2006, 41.57, 2.26111, 109, 1],
           [19, 81483, 20.0, 5, 2006, 41.57, 2.26111, 109, 1],
           [57, 79212, 6.0, 12, 2006, 41.57, 2.26111, 109, 0],
           [30, 88099, 0.0, 20, 2007, 41.57, 2.26111, 109, 0],
           [6, 87538, 9.0, 7, 2009, 41.57, 2.26111, 109, 0],
           [59, 84720, 15.5, 4, 2009, 41.57, 2.26111, 109, 0],
           [7, 91987, 22.0, 9, 2016, 41.57, 2.26111, 109, 0],
           [42, 81560, 105.0, 2, 2019, 41.57, 2.26111, 109, 0],
           [59, 81843, 3.0, 15, 2019, 41.57, 2.26111, 109, 0],
           [5, 85456, 12.0, 10, 2019, 41.57, 2.26111, 109, 0],
           [15, 85249, 39.0, 7, 2020, 41.57, 2.26111, 109, 0],
           [55, 84227, 1.0, 17, 2020, 41.57, 2.26111, 109, 0],
           [60, 83001, 0.0, 23, 2011, 43.7347, 7.42056, 7, 0]]


def accuracy_score(predictions, true_classes):
    p = 0
    for x, y in zip(predictions, true_classes):
        if x == y:
            p += 1

    return p / len(true_classes)


if __name__ == '__main__':
    number_hidden = int(input())
    learning_rate = float(input())
    col = int(input())
    new = input()

    train_set = dataset[:int(len(dataset)*0.8)]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(len(dataset)*0.8):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = MLPClassifier(
        max_iter=20,
        activation='relu',
        hidden_layer_sizes=number_hidden,
        learning_rate_init=learning_rate,
        random_state=0
    )

    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(train_x)
    train_x = scaler.transform(train_x)
    test_x = scaler.transform(test_x)
    
    classifier.fit(train_x, train_y)

    accuracy_train = accuracy_score(classifier.predict(train_x), train_y)
    accuracy_test = accuracy_score(classifier.predict(test_x), test_y)

    diff = abs(accuracy_train - accuracy_test)

    new_input = [float(x) for x in new.split(' ')]
    new_input = scaler.transform([new_input])

    if (diff / accuracy_test) >= 0.15:
        train_x = [[row[i]
                    for i in range(len(row)) if i != col] for row in train_x]
        test_x = [[row[i]
                   for i in range(len(row)) if i != col] for row in test_x]
        new_input = [new_input[i] for i in range(len(new_input)) if i != col]

        classifier.fit(train_x, train_y)
        print("Se sluchuva overfitting")
    else:
        print("Ne se sluchuva overfitting")

    prediction = classifier.predict(new_input)[0]
    print(prediction)