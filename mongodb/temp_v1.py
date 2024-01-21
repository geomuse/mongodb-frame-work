import nltk
from nltk.corpus import reuters
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from gensim import corpora, models

# 下载 Reuters 新闻语料库
# nltk.download('reuters')
# 获取所有文档的 ID 列表
documents = reuters.fileids()

# 选择一些文档进行演示，可以根据需要选择更多文档
doc_ids = ['test/14826', 'test/14828', 'test/14829']

# 读取文档内容
corpus = [reuters.raw(doc_id) for doc_id in doc_ids]

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# 下载停用词
# nltk.download('stopwords')

# 获取停用词列表
stop_words = set(stopwords.words('english'))

# 初始化 PorterStemmer 用于词干提取
porter = PorterStemmer()

# 文本预处理函数
def preprocess_text(text):
    # 小写化
    text = text.lower()
    # 标记化
    tokens = word_tokenize(text)
    # 去除停用词和标点符号
    tokens = [porter.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return tokens

# 对每个文档进行预处理
preprocessed_corpus = [preprocess_text(doc) for doc in corpus]

# 创建词典和文档-词频矩阵
dictionary = corpora.Dictionary(preprocessed_corpus)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in preprocessed_corpus]

# 使用 LDA 模型进行主题建模
lda_model = models.LdaModel(doc_term_matrix, num_topics=3, id2word=dictionary, passes=15)

# 打印每个主题的关键词
for idx, topic in lda_model.print_topics(-1):
    print(f'Topic {idx}: {topic}')
