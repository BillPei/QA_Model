# backup train
Tips�����ԭ����train������Ŀ¼������������Ǿ����˹�ɾѡ�������ݣ���ʽͬԭ����train��ͬ

## 1�ڱ�Ŀ¼��

    �޸����QAModelλ�ã�sys.path.append('/home/zhengxing/QAModel')

## 2�ڱ�Ŀ¼��
    filepath = '.' //Դ�ļ�λ��
    
    filename = 'train' //Դ�ļ���
    
    filename1 = filename + '1_data_version1' //�����������ļ���
    
    filename0 = filename + '0_data_version1' //�����������ļ���


## Tips:

    1. ԭʼ���ݣ�`train`
    2. `expand_tfidf.py` ���`train`�е�ÿһ�������е�answer���м�������ÿ�������idf,
    ����idfֵǰtop_k�Ĳ�����answerĩβ���������3���ļ���
        train.word-idf��ÿ�������idfֵ // word:score
        train.expand-top_k-idf:�µ�train�ļ�����ʽͬtrain
        train.expand-top_k-idf-bk:��Ӧtrain�ļ��е�ÿһ�У�ÿһ�е�ÿ�����ʵ�idfֵ 
    
    3. `prepare_train_data.py` �������ϸ�ʽ����train����