# 由于在Tree中，连续值特征的名称以及改为了  feature<=value的形式
# 因此对于这类特征，需要利用正则表达式进行分割，获得特征名以及分割阈值
def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    if '<=' in firstStr:
        featvalue = float(re.compile("(<=.+)").search(firstStr).group()[2:])
        featkey = re.compile("(.+<=)").search(firstStr).group()[:-2]
        secondDict = inputTree[firstStr]
        featIndex = featLabels.index(featkey)
        if testVec[featIndex] <= featvalue:
            judge = 1
        else:
            judge = 0
        for key in secondDict.keys():
            if judge == int(key):
                if type(secondDict[key]).__name__ == 'dict':
                    classLabel = classify(secondDict[key], featLabels, testVec)
                else:
                    classLabel = secondDict[key]
    else:
        secondDict = inputTree[firstStr]
        featIndex = featLabels.index(firstStr)
        for key in secondDict.keys():
            if testVec[featIndex] == key:
                if type(secondDict[key]).__name__ == 'dict':
                    classLabel = classify(secondDict[key], featLabels, testVec)
                else:
                    classLabel = secondDict[key]
    return classLabel


# 测试决策树正确率
def testing(myTree, data_test, labels):
    error = 0.0
    for i in range(len(data_test)):
        if classify(myTree, labels, data_test[i]) != data_test[i][-1]:
            error += 1
    # print 'myTree %d' %error
    return float(error)


# 测试投票节点正确率
def testingMajor(major, data_test):
    error = 0.0
    for i in range(len(data_test)):
        if major != data_test[i][-1]:
            error += 1
    # print 'major %d' %error
    return float(error)


# 后剪枝
def postPruningTree(inputTree, dataSet, data_test, labels):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    classList = [example[-1] for example in dataSet]
    featkey = copy.deepcopy(firstStr)
    if '<=' in firstStr:
        featkey = re.compile("(.+<=)").search(firstStr).group()[:-2]
        featvalue = float(re.compile("(<=.+)").search(firstStr).group()[2:])
    labelIndex = labels.index(featkey)
    temp_labels = copy.deepcopy(labels)
    del (labels[labelIndex])
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            if type(dataSet[0][labelIndex]).__name__ == 'str':
                inputTree[firstStr][key] = postPruningTree(secondDict[key], splitDataSet(dataSet, labelIndex, key),
                splitDataSet(data_test, labelIndex, key),
               copy.deepcopy(labels))
            else:
                inputTree[firstStr][key] = postPruningTree(secondDict[key],
                                                           splitContinuousDataSet(dataSet, labelIndex, featvalue, key),
                                                           splitContinuousDataSet(data_test, labelIndex, featvalue,
                                                                                  key),
                                                           copy.deepcopy(labels))
    if testing(inputTree, data_test, temp_labels) <= testingMajor(majorityCnt(classList), data_test):
        return inputTree
    return majorityCnt(classList)


data = df.values[:11, 1:].tolist()
data_test = df.values[11:, 1:].tolist()
labels = df.columns.values[1:-1].tolist()
myTree = postPruningTree(myTree, data, data_test, labels)

import treePlotter

treePlotter.createPlot(myTree)