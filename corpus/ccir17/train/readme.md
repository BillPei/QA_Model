# train

## 1�ڱ�Ŀ¼��
    �޸����QAModelλ�ã�sys.path.append('/home/zhengxing/QAModel')

## 2�ڱ�Ŀ¼��
    filepath = '.' //Դ�ļ�λ��
    
    filename = 'train' //Դ�ļ���
    
    filename1 = filename + '1_data_version1' //�����������ļ���
    
    filename0 = filename + '0_data_version1' //�����������ļ���


## Tips:

    1.  raw data is `train.1.json`
    2.  `expand_raw_data.py` is used to expand the raw data with crawling raw
    text from the url, then generate the new raw data called 'train.1.json.new'
    3.  `prepare_train_test_data.py` is used to generate the 2/3 train data 
    and 1/3 test data
    4.  `prepare_expanded_URL_train_test_data.py` is used to generate the 2/3 
    train data (expanded with the title of the url) and 1/3 test data 
    (expanded with the title of the url)
    5.  `prepare_train_data.py` is not used.

