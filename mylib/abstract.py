#coding:utf-8
from textrank4zh import TextRank4Keyword, TextRank4Sentence
def getKeyword(text, keywords_num=20):
    """对text提取关键词，关键词个数为keywords_num, 关键短语也顺便提取。
    关键短语在文中的最少出现次数为 phrase_min_num=5,没有再减。
    返回关键字的列表（item.word, item.weight）和关键短语列表
    """
    tr4w = TextRank4Keyword()
    # 对文本进行分析，设定窗口大小为2，并将英文单词小写
    tr4w.analyze(text=text, lower=True, window=2)
    kw = tr4w.get_keywords(num=keywords_num, word_min_len=1)
    mon = 5
    while(mon>0):
        kp = tr4w.get_keyphrases(keywords_num=keywords_num, min_occur_num=mon)
        if len(kp) > 0:
            print(mon)
            break
        mon -= 1
    return kw, kp
    # for item in tr4w.get_keywords(num=20, word_min_len=1):
    #     print(item.word, item.weight)
    # print("\n关键短语") #不一定能凑出来。
    # for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num=1):
    #     print(phrase)

def getAbstarct(text, sentencesNum = 3, lists = False):
    """对text提取摘要，内容为sentencesNum个高权重句子，
    返回结果默认为一个字符串，也可以是N个句子的列表"""
    if sentencesNum <2:
        sentencesNum = 2
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')
    # print('摘要为：')
    ss = []
    for item in tr4s.get_key_sentences(num=sentencesNum):
        # 打印句子的索引、权重和内容
        # print(item.index, item.weight, item.sentence)
        ss.append(item.sentence)
    if lists:
        return ss       #n个句子列表
    return "。".join(ss)  #默认一个字符串

def compress(text, sentencesNum=3, onestr = False):
    """对text压缩，结果为为sentencesNum个高权重句子，
    返回结果默认为一个字符串，也可以是摘要和关键短语分开，参数保持默认即可"""
    kw, kp = getKeyword(text)
    temp = 0
    for i in text:
        if i == "。" :
            temp += 1
        if temp>5:  #出现5个句号以上，进行压缩
            text = getAbstarct(text, sentencesNum)
            break
    if onestr:
        m = "{"
        for i in kp:
            m = m + i + ";"
        return m+"}"+text
    return text, kp[:5] #默认返回最多3个关键短语




if __name__ == '__main__':
    text = """
社会主义加速回归——化学反应背后——习近平要告诉官僚体系什么

“全盘西化”不是世界上所有国家实现现代化的唯一路径，西方化也不代表现代化。对于中国而言，1840年甲午战争后，最重要的时代命题只有两个，一是“什么是现代化、怎么实现现代化”，二是“什么是社会主义、怎么建设社会主义”。清政府洋务派、以孙中山为代表的民族资产阶级、五四运动衍生出来的极端西化派，原教旨与本土化的共产主义者，甚至无政府主义者以及纳粹主义，在中国接连“各领风骚”、你方唱罢我登场。他们有的失败了，有的开始走入歧途，而习近平的历史使命就是“正本清源”。这种“正本清源”绝不是如西方舆论与中国自由派所认为，中国将重回文革，重回极权。

中共，作为世界上党员人数最多的执政党，在即将迎来建党一百年之时，有且只有一个议题：过去一百年这个政党的工作是否与其建党“初心”一致？他会交上怎样一份成绩单？这是习近平作为这个红色政权接班人的历史使命。浏览更多文章：【多维CN/TW频道】

于2019年10月召开的中共十九届四中全会，势将成为中国国家主席习近平执政后又一个重要的历史节点。

据8月31日中央政治局会议公开信息，其主要议程是政治局报告工作、研究坚持和完善中国特色社会主义制度，以及推进国家治理体系和治理能力现代化若干重大问题。

约两个月前的7月5日，北京召开了“深化党和国家机构改革总结会议”，也即中共推进国家治理体系和治理能力现代化的一次阶段性总结会议。习近平当时表示，完成组织架构重建、实现机构职能调整，只是解决了“面”上的问题，真正要发生“化学反应”，还有大量工作要做。

那么，本届四中全会所涉及的“若干重大问题”，应该就与习近平所说的“化学反应”有关。而这也将是习近平在在“世界百年未有之大变局”的判断之下，基于“社会主义”的政治底色，推进实践“第五个现代化”的关键一步。

何为“化学反应”。
"""
    # kw, kp = getKeyword(text, 20)
    # print("keywords:")
    # for item in kw:
    #     print(item.word, item.weight)
    # print("\nkey phrase:")
    # print(kp)

    # SaveWordCloud((kw, kp), 'test')
    # print("abstract: ",getAbstarct(text, 3))
    # print("\n")

    #usage 1
    print("compress:", compress(text, onestr=True)) #摘要和关键短语放在一起

    #usage 2
    text, kp = compress(text)   #摘要，关键短语分开
    print("compress abstract:", text)
    for phrase in kp:   #关键短语
        print(phrase)
