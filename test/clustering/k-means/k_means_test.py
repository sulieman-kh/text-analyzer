import unittest

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs

from clustering.k_means.k_means import KMeans


class KMeansTest(unittest.TestCase):

    def test_1000_random_points(self):
        # Configuration options
        num_samples_total = 1000
        cluster_centers = [(20, 20), (4, 4)]
        num_classes = len(cluster_centers)

        # Generate data
        X, targets = make_blobs(
            n_samples=num_samples_total, centers=cluster_centers, n_features=num_classes, center_box=(0, 1),
            cluster_std=2
        )
        predict = KMeans(n_clusters=num_classes).k_means_plusplus(X)

        # Generate scatter plot for training data
        colors = list(map(lambda x: '#3b4cc0' if x == 1 else '#b40426', predict))
        plt.scatter(X[:, 0], X[:, 1], c=colors, marker="o", picker=True)
        plt.title('Two clusters of data')
        plt.xlabel('Temperature yesterday')
        plt.ylabel('Temperature today')
        plt.show()

        # Asserts:
        first_cluster_cnt = list(predict).count(0)
        second_cluster_cnt = list(predict).count(1)
        self.assertEqual(first_cluster_cnt, second_cluster_cnt)

    def test_6_known_points(self):
        # Generate data
        X = np.array([[1, 2], [1, 4], [1, 0],
                      [10, 2], [10, 4], [10, 0]])
        predict = KMeans(n_clusters=2, random_state=0).k_means_plusplus(X)
        predict_list = list(predict)

        # Asserts:
        self.assertEqual(predict_list[0], 1)
        self.assertEqual(predict_list[1], 1)
        self.assertEqual(predict_list[2], 1)

        self.assertEqual(predict_list[3], 0)
        self.assertEqual(predict_list[4], 0)
        self.assertEqual(predict_list[5], 0)


if __name__ == '__main__':
    unittest.main()
