Версию программы https://github.com/IljaNovo/ProjectOfDataMining Она выглядит более полной (в плане работоспособности меню).

    1) Сделать интерфейс к программе на PyQt5, чтобы было удобнее работать;
    2) Взять алгоритмы из библиотеки Scikit-Learn и настроить их (основная задача), перед обработкой алгоритмом
    3) Сделать модуль получения информации: из файла (лист Excel); из URL; случайная выборка данных (генератор рандомных классов)
    4) Сделать модуль вывода информации: в файл (лист Excel); на график; 
    5) Протестировать алгоритмы на тестовых данных (ирисы, небольшая выборка на русском языке);


Основная программа - окно меню интерфейса. В проекте сделать общую структуру папок. Каждый будет добавлять свой алгоритм туда, можно отрегулировать интеграцию процесса с помощью GIT (каждое изменение попросить сопровождать комментарием).

# Входная информация:
    1. Из документа Excel (из набора документов) в системе;
    2. По ссылке (URL), ** с диска скачать

# Алгоритмы
    1. Из библиотеки + настройка

# Выход программы:
    1. В файлы, все промежуточные результаты (Excel на листы вывод)
    1. Визуализация. Отображение результата (кластеры, классы) в 2D matplotlib, seaborn, plotly

Iris https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html 


Алгоритмы на выбор (методы следующие https://scikit-learn.org/stable/glossary.html#methods):

    • Naive Bayes
    • Decision Tree Classifier
    • Random Forests
    • Support Vector Machines
    • K-Nearest Neighbors

    • K-Means (k-means++)
    • Affinity propagation
    • Mean-shift
    • Spectral clustering
    • Ward hierarchical clustering
    • Agglomerative clustering
    • DBSCAN
    • Birch

Время разработки - до середины мая, крайний срок – конец июня.

# Библиотеки для предобработки:
https://github.com/kmike/pymorphy2 (основная);

https://github.com/nlpub/pymystem3 (стеммер, можно использовать);

https://github.com/natasha/natasha (библиотека больше для word embeddings);
