import os
from skimage.io import imread
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler #apparently MLP is sensitive to scaling, so this helps
import joblib
import matplotlib.pyplot as plt


def load_data() -> list:
    "load data from the Output FIles folder, and return inoput arr and their indices in output arr"
    dir = "OutputFiles/Moods and Moments"
    Categories = os.listdir(dir)

    input_arr = []
    output_arr = []

    for i in Categories:
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


def generate_model(input, out):
    """generates the model, saves to NeuralNetwork directory. Also shows the confusion matrix"""
    X_train, X_test, y_train, y_test = train_test_split(
    input, out, test_size=0.25, random_state=16
)

    model = MLPClassifier(
    solver="sgd", alpha=0.001, hidden_layer_sizes=(20,50), random_state=42
    )

    # scaling
    # NOTE I am stupid, should have used it earlier
    # accuracy jumped from 0.17 to 0.79
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    # consider using pipeline for scaling

    # fit the model with data
    model.fit(X_train, y_train)

    # Make predictions on the training set
    y_pred = model.predict(X_train)

    # Calculate accuracy
    train_accuracy = accuracy_score(y_train, y_pred)
    # print("Accuracy training:", train_accuracy)  # 1.0

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot()
    plt.show()

    # Calculate accuracy
    test_accuracy = accuracy_score(y_test, y_pred)

    del model.loss_curve_
    joblib.dump(model, "NeuralNetwork/NN.pkl", compress=3)

    return train_accuracy, test_accuracy


if __name__ == "__main__":
    x, y = load_data()
    print(generate_model(x, y))
