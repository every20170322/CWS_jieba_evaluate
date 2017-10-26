# -*- coding: utf-8 -*-

import sys
import jieba

#配置utf-8的输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

file_test=open("/home/lwz/machine_learning_practice/nlp/CWS_jieba_evaluate/corpus_test/pku_test.utf8","rb")

file_seg=open("/home/lwz/machine_learning_practice/nlp/CWS_jieba_evaluate/corpus_seg/pku_seg.utf8","wb")

list_test=file_test.readlines()
file_test.close()
sentense_seg_total=""
for sentense_test in list_test:
    sentense_seg=jieba.cut(sentense_test)
    sentense_seg=" ".join(sentense_seg)
    sentense_seg_total=sentense_seg_total+sentense_seg

file_seg.write(sentense_seg_total)
file_seg.close()


