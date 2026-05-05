from LangSC import GPF
import json

gpf = GPF()
sentence = "北京大学的学生在图书馆里认真地阅读专业书籍"

# 分词与词性标注
Ret = gpf.Parse(sentence, Structure="POS")
tokens = json.loads(Ret)
print(tokens)