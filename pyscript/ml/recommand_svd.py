import numpy as np

def load_test_data():

    matrix = [[0.238, 0, 0.1905, 0.1905, 0.1905,
               0.1905], [0, 0.177, 0, 0.294, 0.235,
                         0.294], [0.2, 0.16, 0.12, 0.12, 0.2, 0.2],
              [0.2, 0.16, 0.12, 0.12, 0.2, 0.1]]
    return matrix


def comsSim(vecA, vecB):
    eps = 1.0e-6
    a = vecA[0]
    b = vecB[0]
    return np.dot(a, b) / ((np.linalg.norm(a) * np.linalg.norm(b)) + eps)


def recommand_by_svd():
    r = 1
    dataset = np.mat(load_test_data())
    data_point = np.mat([[0.2174, 0.2174, 0.1304, 0, 0.2174, 0.2174]])
    m, n = np.shape(dataset)
    limit = min(m, n)
    if r > limit: r = limit
    U, S, VT = np.linalg.svd(dataset.T)  #SVD 分解
    V = VT.T
    Ur = U[:, :r]
    Sr = np.diag(S)[:r, :r]  #取前r个U,S,V的值
    Vr = V[:, :r]
    testresult = data_point * Ur * np.linalg.inv(Sr)  # 计算data_point的坐标
    resultarray = np.array([comsSim(testresult, vi) for vi in Vr])  # 计算距离
    descindx = np.argsort(-resultarray)[:1]
    print(descindx)
    # print resultarray
    print(resultarray[descindx])


if __name__ == '__main__':
    # 使用SVD算法进行推荐
    recommand_by_svd()