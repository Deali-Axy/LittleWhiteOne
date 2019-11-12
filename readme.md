# LittleWhite One
魔改chatterbot框架实现的新版小白~

## 简介
- core：核心框架，魔改版chatterbot
- corpus：英文和中文训练语料
- nltk_data：需要用到的nltk数据集

## 文本相似度算法
- LevenshteinDistance
- SpacySimilarity
- JaccardSimilarity

### Levenshtein Distance算法
中文名：莱文斯坦距离
参考资料：[https://en.wikipedia.org/wiki/Levenshtein_distance](https://en.wikipedia.org/wiki/Levenshtein_distance)

>Levenshtein distance是表征或度量两段字符串的差异度的概念,以单词kitten和sitting为例，定义：替换(substitution)、插入(insert)和删除(delete)三种标准编辑手段来消除这两个词之间的差异，每经过1次标准编辑手段，Levenshtein distance增计一次，则kitten需经过2次替换、1次插入新字符，来得到sitting这个单词，因此所谓的Levenshtein distance应为3。按照其定义，该距离和字符串差异度呈正比关系。

**定义**：
两个字符串a，b之间的莱文斯坦距离
![](https://upload-images.jianshu.io/upload_images/8869373-78cbcc8897912b52.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

编辑距离是NLP基本的度量文本相似度的算法，可以作为文本相似任务的重要特征之一，其可应用于诸如拼写检查、论文查重、基因序列分析等多个方面。但是其缺点也很明显，算法基于文本自身的结构去计算，并没有办法获取到语义层面的信息。

###  SpacySimilarity算法 

 SpacySimilarity属于语义相似度的计算方法。 

参考资料： https://spacy.io/api/doc/#similarity 

先将句子的词向量求平均，获取句子的语义表示，然后计算两个句子的语义表示的余弦相似度。

###  JaccardSimilarity算法 
参考资料：[https://en.wikipedia.org/wiki/Jaccard_index](https://en.wikipedia.org/wiki/Jaccard_index)

给定两个集合A,B，Jaccard 系数定义为A与B交集的大小与A与B并集的大小的比值，定义如下：

![](https://upload-images.jianshu.io/upload_images/8869373-f187538fdff080e0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

当集合A，B都为空时，J(A,B)定义为1。

与Jaccard 系数相关的指标叫做Jaccard 距离，用于描述集合之间的不相似度。Jaccard 距离越大，样本相似度越低。公式定义如下：

![](https://upload-images.jianshu.io/upload_images/8869373-dd02f73baef5f3ef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## todo

### 算法优化

- [ ] 试用另外的基于词向量的几种计算文本相似度方法 ：
  - [ ] 使用词向量求平均计算相似度
  - [ ] 词向量tfidf加权求平均计算相似度
  - [ ] 词向量加权-PCA计算相似度
- [ ]  基于深度学习的方式，计算句子的语义相似度 

### 训练优化

- [ ] 使用新的大容量语料训练
- [ ] 接入tai套取聊天语料
- [ ] 结合LittleWhite v3的双引擎从用户对话中学习

