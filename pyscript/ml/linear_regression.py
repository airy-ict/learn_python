import numpy as np
import scipy as sp
from scipy.stats import norm
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

# 机器学习中的预测问题通常分为2类：回归与分类。
# 简单的说回归就是预测数值，而分类是给数据打上标签归类。

# arange 根据start与stop指定的范围以及step设定的步长，生成一个 ndarray
x = np.arange(0, 1, 0.002)

# scipy.stats.norm.rvs正态分布
# （1）作用：构造正态分布的数据
# （2）函数：scipy.stats.norm.rvs(size=100,loc=0,scal=1) 
# scipy.norm正态分布模块的随机变量函数rvs，size=100是样本大小，loc＝0是均值，scal=1是标准差
y = norm.rvs(loc=0, size=500, scale=0.1)
y = y + x**2
# scatter 散点图
plt.scatter(x, y)
plt.show()


# 均方误差根 
def rmse(y_test, y):
    return sp.sqrt(np.mean((y_test - y)**2))


#R-平方  与均值相比的优秀程度，介于[0~1]。0表示不如均值。1表示完美预测.这个版本的实现是参考scikit-learn官网文档
def R2(y_test, y_true):
    return 1 - ((y_test - y_true)**2).sum() / (
        (y_true - y_true.mean())**2).sum()


# 这是Conway&White《机器学习使用案例解析》里的版本
def R22(y_test, y_true):
    y_mean = np.array(y_true)
    y_mean[:] = y_mean.mean()
    return 1 - rmse(y_test, y_true) / rmse(y_mean, y_true)


def main():
    """
    线性回归以及数据过拟合
    """
    plt.scatter(x, y, s=5)
    degree = [1, 2, 100]
    y_test = []
    y_test = np.array(y_test)

    for d in degree:
        # PolynomialFeatures 	多项式数据转换
        clf = Pipeline([('poly', PolynomialFeatures(degree=d)),
                        ('linear', LinearRegression(fit_intercept=False))])
        # 训练
        clf.fit(x[:, np.newaxis], y)
        # 预测 np.newaxis 为 numpy.ndarray（多维数组）增加一个轴  np.newaxis 在使用和功能上等价于 None，其实就是 None 的一个别名。
        y_test = clf.predict(x[:, np.newaxis])

        print(clf.named_steps['linear'].coef_)
        print('rmse=%.2f, R2=%.2f, R22=%.2f, clf.score=%.2f' %
              (rmse(y_test, y), R2(y_test, y), R22(y_test, y),
               clf.score(x[:, np.newaxis], y)))

        plt.plot(x, y_test, linewidth=2)

    plt.grid()
    plt.legend(['1', '2', '100'], loc='upper left')
    plt.show()


# scipy.stats.norm.rvs正态分布
# （1）作用：构造正态分布的数据
# （2）函数：scipy.stats.norm.rvs(size=100,loc=0,scal=1) 
# scipy.norm正态分布模块的随机变量函数rvs，size=100是样本大小，loc＝0是均值，scal=1是标准差

if __name__ == '__main__':
    main()