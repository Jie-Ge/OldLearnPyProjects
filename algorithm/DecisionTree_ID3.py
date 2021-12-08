from math import log
import operator
import trees
import treePlotter
import sys
from imp import reload

reload(sys)


# sys.setdefaultencoding("utf-8")

def createDataSet():
    # 不浮出水面是否可以生存(no surfacing), 是否有脚蹼(flippers), 是否属于鱼类
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']  # 属性
    # change to discrete values
    return dataSet, labels


myData, labels = createDataSet()
print(myData)
print(labels)


##### 计算信息熵 ######
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)  # 样本数
    labelCounts = {}  # 创建一个数据字典：key是最后一列的数值（即标签，也就是目标分类的类别），value是属于该类别的样本个数
    for featVec in dataSet:  # 遍历整个数据集，每次取一行
        currentLabel = featVec[-1]  # 取该行最后一列的值, 作为key
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0  # 初始化信息熵
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)  # log base 2  计算信息熵
    return shannonEnt


print(calcShannonEnt(myData))


##### 按给定的特征划分数据 #########
# 当这里传入的是(dataSet, 0, 0)时，返回的是第0列中等于0的行(并且是不包括第0列的元素)， 返回的就是[[1, 'no'], [1, 'no']]
def splitDataSet(dataSet, axis, value):  # axis是dataSet数据集下要进行特征划分的列号例如0列，value是该列下某个特征值，0列中的sunny
    retDataSet = []
    for featVec in dataSet:  # 遍历数据集，并抽取按axis的当前value特征进行划分的数据集(不包括axis列的值)
        if featVec[axis] == value:  #
            reducedFeatVec = featVec[:axis]  # chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
            # print axis,value,reducedFeatVec
    # print retDataSet
    return retDataSet


##### 选取当前数据集下，用于划分数据集的最优特征
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  # 获取当前数据集的特征个数，最后一列是分类标签
    baseEntropy = calcShannonEnt(dataSet)  # 计算当前数据集的信息熵
    bestInfoGain = 0.0
    bestFeature = -1  # 初始化最优信息增益和最优的特征
    for i in range(numFeatures):  # 遍历每个特征iterate over all the features
        featList = [example[i] for example in dataSet]  # 获取数据集中当前特征下的所有值
        uniqueVals = set(featList)  # 获取当前特征值，例如outlook下有sunny、overcast、rainy
        newEntropy = 0.0
        for value in uniqueVals:  # 计算每种划分方式的信息熵
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy  # 计算信息增益
        if infoGain > bestInfoGain:  # 比较每个特征的信息增益，只要最好的信息增益
            bestInfoGain = infoGain  # if better than current best, set to best
            bestFeature = i
    return bestFeature  # returns an integer
'''
C4.5算法， 主要在96、97行的不同
def chooseBestFeatureToSplit(dataSet):  
    numFeatures = len(dataSet[0])-1  #求属性的个数
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1  
    for i in range(numFeatures):  #求所有属性的信息增益
        featList = [example[i] for example in dataSet]  
        uniqueVals = set(featList)  #第i列属性的取值（不同值）数集合
        newEntropy = 0.0  
        splitInfo = 0.0;
        for value in uniqueVals:  #求第i列属性每个不同值的熵*他们的概率
            subDataSet = splitDataSet(dataSet, i , value)  
            prob = len(subDataSet)/float(len(dataSet))  #求出该值在i列属性中的概率
            newEntropy += prob * calcShannonEnt(subDataSet)  #求i列属性各值对于的熵求和
            splitInfo -= prob * log(prob, 2);
        infoGain = (baseEntropy - newEntropy) / splitInfo;  #求出第i列属性的信息增益率
        print infoGain;    
        if(infoGain > bestInfoGain):  #保存信息增益率最大的信息增益率值以及所在的下表（列值i）
            bestInfoGain = infoGain  
            bestFeature = i  
    return bestFeature  
'''

print(splitDataSet(myData, 0, 0))
print(splitDataSet(myData, 0, 1))
print(chooseBestFeatureToSplit(myData))


#####该函数使用分类名称的列表，然后创建键值为classList中唯一值的数据字典。字典
#####对象的存储了classList中每个类标签出现的频率。最后利用operator操作键值排序字典，
#####并返回出现次数最多的分类名称
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    # 对字典进行排序， 按照value从小到大排序（1），【若是0的话就按key排序】， reverse：翻转
    sortedClassCount = sorted(classCount.items, key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]  # dict[][]?


##### 生成决策树主方法
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]  # 返回当前数据集下标签列所有值
    if classList.count(classList[0]) == len(classList):
        return classList[0]  # 当类别完全相同时则停止继续划分，直接返回该类的标签
    if len(dataSet[0]) == 1:  # 遍历完所有的特征时，仍然不能将数据集划分成仅包含唯一类别的分组 dataSet
        return majorityCnt(classList)  # 由于无法简单的返回唯一的类标签，这里就返回出现次数最多的类别作为返回值
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 获取最好的分类特征索引
    bestFeatLabel = labels[bestFeat]  # 获取该特征的名字

    # 这里直接使用字典变量来存储树信息，这对于绘制树形图很重要。
    myTree = {bestFeatLabel: {}}  # 当前数据集选取最好的特征存储在bestFeat中
    del (labels[bestFeat])  # 删除已经在选取的特征
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]  # copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


myTree = createTree(myData, labels)
print(myTree)

# 决策树运用于分类
# 构建一个决策树分类函数（决策树，属性特征标签，测试的数据
def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]  # 获取树的第一个特征属性
    secondDict = inputTree[firstStr]  # 树的分支，子集合Dict
    featIndex = featLabels.index(firstStr)  # 获取决策树第一层在featLables中的位置
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else:
        classLabel = valueOfFeat
    return classLabel

# 决策树的存储
def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()

# 决策树的读取
def grabTree(filename):
    import pickle
    fr = open(filename, 'rb')
    return pickle.load(fr)


storeTree(myTree, 'classifierStorage.txt')
grabTree('classifierStorage.txt')