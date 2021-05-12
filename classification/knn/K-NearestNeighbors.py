from types import FunctionType

from pandas.core.frame import DataFrame
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split


class KnnResult:
    def __init__(self, prediction_result, scope_result, test_data, classifier) -> None:
        self.predictionResult = prediction_result
        self.scope = scope_result
        self.knnClassifier = classifier
        self.testData = test_data
        pass


def knn(n_neighbors: int, weights: FunctionType, data: DataFrame, target_column='target', test_size=0.2) -> KnnResult:
    X = data.drop(columns=[target_column])
    Y = data[target_column].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=1, stratify=Y)

    classifier = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights)
    classifier.fit(X=X_train, y=Y_train)
    return KnnResult(prediction_result=classifier.predict(X=X_test),
                     scope_result=classifier.score(X=X_test, y=Y_test),
                     classifier=classifier, test_data=X_test)


def main():
    iris = datasets.load_iris()
    iris_frame = DataFrame(iris.data)
    iris_frame.columns = iris.feature_names
    iris_frame['target'] = iris.target
    iris_frame['name'] = iris_frame.target.apply(lambda x: iris.target_names[x])
    iris_frame = iris_frame.drop(columns=["name"])
    result = knn(10, 'uniform', iris_frame, 'target', 0.25)

    print(result.scope)
    print(result.predictionResult)


main()
