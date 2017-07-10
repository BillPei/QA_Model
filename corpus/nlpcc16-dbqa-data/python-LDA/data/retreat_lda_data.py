__author__ = 'xing'
#coding = utf-8
'''
prepare_lda_data.py �ڴ���train����ʱ���п�������ĳЩ���Ϸ���������������ɵ�lda���ݳ���ȱʧ����
retreat_lda_data.py ����ȱʧ������(default 0.01)
'''
import os,sys,codecs

sys.path.append('/home/zhengxing/QAModel')

from util.word_segment import *


def generate_default_data(dim, single_s):
    s = ''
    for i in range(dim):
        if s == '':
            s += single_s
        else:
            s += '\t' + single_s
    return s


if __name__ == '__main__':
    model_filepath = 'tmp'
    train_filepath = '.'
    model_filename = 'model_theta.dat'
    train_filename = 'train'

    model_dim = 300
    full_version_model_filepath = 'tmp'
    full_version_model_filename = model_filename + '-' + train_filename + '-' + str(model_dim)

    fw = codecs.open(os.path.join(full_version_model_filepath, full_version_model_filename), 'w', encoding='utf-8')

    with codecs.open(os.path.join(train_filepath, train_filename), 'r', encoding='utf-8') as train_fr:
        model_fr = codecs.open(os.path.join(model_filepath, model_filename), 'r', encoding='utf-8')
        line_no = 0
        for line in train_fr:
            line_no += 1
            print line_no, '...'
            line = line.strip()
            flag = 0
            if line is not None and line != '':
                items = line.split('\t')
                if len(items) == 3:
                    question = items[0]
                    answer = items[1]
                    label = items[2]
                    word_list = get_filtered_segment_word_list(answer, None)
                    words_record = ''
                    for w in word_list:
                        if words_record == '':
                            words_record = w
                        else:
                            words_record += ' ' + w
                    if words_record != '':
                        words_record += '\n'
                        #fw.write(words_record)
                        flag = 1
            #�����Ե�����
            if flag == 0:
                fw.write(generate_default_data(model_dim, '0.01') + '\n')
            else:
                fw.write(model_fr.readline())
    fw.close()
    model_fr.close()