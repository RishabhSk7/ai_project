import os
from skimage.io import imread
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
import joblib

# Sleep party sad
cats = ["sad", "sleep", "Party"]

def load_data() -> list:
    "load data from the Output FIles folder, and return inoput arr and their indices in output arr"
    dir = "OutputFiles/Moods and Moments"
    Categories = os.listdir(dir)

    input_arr = []
    output_arr = []

    for i in Categories:
        if i not in cats:
            continue
        print("Loading category: ", i)
        path = os.path.join(dir, i)

        limiter = 0  # managing memory

        for j in os.listdir(path):
            if limiter == 50:
                break
            limiter += 1
            img = imread(os.path.join(path, j))
            input_arr.append(img.flatten())
            output_arr.append(Categories.index(i))
        # using index since we need to use numerical value for classes

        print(f"loaded category:{i} successfully")
    return input_arr, output_arr


def generate_model(input_arr, output_arr)-> list:
    "make the SVM model witha arg1 as input data and arg2 as categories"
    df = pd.DataFrame(np.array(input_arr))
    df["Target"] = np.array(output_arr)

    x = df.iloc[:, :-1]  # input data, all rows, all columns except last "target" one
    y = df.iloc[:, -1]  # output data, all rows, only the last column that is the labels

    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    print(X_train)

    # lets avoid scaling for now, since we already scaled frequencies to db once
    # scaler = StandardScaler()
    # X_train_scaled = scaler.fit_transform(X_train)
    # X_test_scaled = scaler.transform(X_test)

    # svm_sgd = SGDClassifier(loss="hinge", alpha=0.001, max_iter=300, random_state=42)
    model = svm.SVC(kernel="rbf", cache_size=1000)
    model.fit(X_train, y_train)

    # Make predictions on the training set
    y_pred = model.predict(X_train)

    # Calculate accuracy
    train_accuracy = accuracy_score(y_train, y_pred)
    # print("Accuracy training:", train_accuracy)  # 1.0

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    test_accuracy = accuracy_score(y_test, y_pred)
    # print("Accuracy testing:", test_accuracy)  # 0.766666

    joblib.dump(model, "SVM.pkl")

    del model, df, x, y, X_train, X_test, y_train, y_test

    print(train_accuracy, test_accuracy)
    return train_accuracy, test_accuracy

if __name__=="__main__":
    input_data, output_data = load_data()
    print(generate_model(input_data, output_data))
