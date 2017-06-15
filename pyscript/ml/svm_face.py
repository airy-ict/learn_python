import logging
from time import time
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.datasets import fetch_lfw_people
from sklearn.metrics import classification
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.svm import SVC

plt.rcParams['font.sans-serif'] = ['SimHei']  #指定默认字体
plt.rcParams['axes.unicode_minus'] = False  #解决保存图像是负号'-'显示为方块的问题

# 显示进度和错误信息
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


def main():
    lfw_people = fetch_lfw_people(
        min_faces_per_person=70, funneled=False, resize=0.5)
    # 转换为数组
    n_samples, h, w = lfw_people.images.shape

    # 对于机器学习，我们直接使用2个数据（由于该模型忽略了相对像素位置信息）
    X = lfw_people.data
    print("数据集类型：", type(X))
    n_features = X.shape[1]

    # 预测的标签是该人的身份
    y = lfw_people.target
    target_names = lfw_people.target_names

    n_classes = target_names.shape[0]

    print("数据集大小:")
    print("n_samples: %d" % n_samples)
    print("n_features: %d" % n_features)
    print("n_classes: %d" % n_classes)

    # 分为训练集和使用分层k折的测试集
    # 分为培训和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    # 在面部数据集上计算PCA（特征面）（被视为未标记的数据集）：无监督特征提取/维数降低
    n_components = 150

    print("Extracting the top %d eigenfaces from %d faces" %
          (n_components, X_train.shape[0]))
    t0 = time()
    pca = PCA(n_components=n_components, whiten=True).fit(X_train)
    print("done in %0.3fs" % (time() - t0))
    eigenfaces = pca.components_.reshape((n_components, h, w))
    print("Projecting the input data on the eigenfaces orthonormal basis")
    t0 = time()
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test)
    print("done in %0.3fs" % (time() - t0))

    # 训练SVM分类模型
    print("Fitting the classifier to the training set")
    t0 = time()
    param_grid = {
        'C': [1e3, 5e3, 1e4, 5e4, 1e5],
        'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
    }
    clf = GridSearchCV(SVC(kernel='rbf'), param_grid)
    clf = clf.fit(X_train_pca, y_train)
    print("done in %0.3fs" % (time() - t0))
    print("Best estimator found by grid search:")
    print("模型参数", clf.best_estimator_)

    # 测试集上的模型质量的定量评估
    print("Predicting people's names on the test set")
    t0 = time()
    y_pred = clf.predict(X_test_pca)
    print("done in %0.3fs" % (time() - t0))
    print(classification_report(y_test, y_pred, target_names=target_names))
    print(confusion_matrix(y_test, y_pred, labels=range(n_classes)))

    # 使用matplotlib进行定性评估
    def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
        plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
        plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
        for i in range(n_row * n_col):
            plt.subplot(n_row, n_col, i + 1)
            plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
            plt.title(titles[i], size=12)
            plt.xticks(())
            plt.yticks(())

    # 在测试集的一部分绘制预测结果
    def title(y_pred, y_test, target_names, i):
        pred_name = target_names[y_pred[i]].rsplit(' ', 1)[-1]
        true_name = target_names[y_test[i]].rsplit(' ', 1)[-1]
        return '预测:%s\n真实:%s' % (pred_name, true_name)

    prediction_titles = [
        title(y_pred, y_test, target_names, i) for i in range(y_pred.shape[0])
    ]

    plot_gallery(X_test, prediction_titles, h, w)

    # 绘制最有意义的特征面的画廊
    eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
    plot_gallery(eigenfaces, eigenface_titles, h, w)
    plt.show()


if __name__ == '__main__':
    main()