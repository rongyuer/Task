'''
第一步：
pip install baidu-aip
'''

from aip import AipNlp

def login2baidu():
	'''
	统一登录到baidu
	'''
	APP_ID = ''
	API_KEY = ''
	SECRET_KEY = ''
	client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
	return client


def sentiment_analysis():
	'''
	情感分析
	'''
	client = login2baidu()
	text = "苹果是一家伟大的公司"
	answer = client.sentimentClassify(text)

	if answer['items'][0]['sentiment'] == 2:
		print("这句话表达了正向感情")
	elif answer['items'][0]['sentiment'] == 0：
		print("这句话表达了负面感情")
	else:
		print("这句话表达了中性感情")

def short_text_similarity():
	'''
	短文本相似度接口用来判断两个文本的相似度得分
	'''
	client = login2baidu()
	text1 = "浙富股份"
	text2 = "万事通自考网"
	answer = client.simnet(text1, text2)
	print("两段文本的相似度评分为：", answer['score']*100, "%")

def word_similarity():
	'''
	单词相似度
	'''
	client = login2baidu()
	word1 = "北京"
	word2 = "上海"
	answer =client.wordSimEmbedding(word1, word2)
	print(word1+"与"+word2+"相似度评分为：", answer['score']*100, "%")

def word_representation():
	'''
	词向量表示
	'''
	client = login2baidu()
	word = "张飞"
	answer = client.wordEmbedding(word)
	print(answer['vec'])
