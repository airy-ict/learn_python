import numpy as np
import scipy as sp
from sklearn import tree
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def main():
    """
    决策树算法实现
    """
    data = []
    labels = []
    with open("data/tree.txt") as ifile:
        for line in ifile:
            # strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
            tokens = line.strip().split(" ")
            data.append([float(tk) for tk in tokens[:-1]])
            labels.append(tokens[-1])

    x = np.array(data)  # 所要划分的样本特征集
    labels = np.array(labels)
    y = np.zeros(labels.shape)  # 所要划分的样本结果
    print(y)
    print(labels == 'fat')
    y[labels == "fat"] = 1
    print(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # 使用分类器分类 使用信息熵作为划分标准
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    # 训练
    clf.fit(x_train, y_train)
    # 系数反映每个特征的影响力。越大表示该特征在分类中起到的作用越大
    # 本例中，身高的权重为0.25，体重为0.75  
    print(clf.feature_importances_)

    pre_result = clf.predict(x_train)
    print(pre_result)
    # 准确率和召回率
    precision, recall, thresholds = precision_recall_curve(y_train, pre_result)

    # 例子：
    # 某池塘有1400条鲤鱼，300只虾，300只鳖。现在以捕鲤鱼为目的。撒一大网，逮着了700条鲤鱼，200只虾，100只鳖。那么，这些指标分别如下：
    # 正确率 = 700 / (700 + 200 + 100) = 70%
    # 召回率 = 700 / 1400 = 50%
    # F值 = 70% * 50% * 2 / (70% + 50%) = 58.3%
    # 不妨看看如果把池子里的所有的鲤鱼、虾和鳖都一网打尽，这些指标又有何变化：
    # 正确率 = 1400 / (1400 + 300 + 300) = 70%
    # 召回率 = 1400 / 1400 = 100%
    # F值 = 70% * 100% * 2 / (70% + 100%) = 82.35%        

    answer = clf.predict_proba(x)[:,1]  
    print(classification_report(y, answer, target_names = ['thin', 'fat']))  

if __name__ == '__main__':
    main()