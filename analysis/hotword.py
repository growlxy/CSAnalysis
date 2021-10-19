import numpy as np
import pandas as pd
import jieba
import jieba.analyse
from wordcloud import WordCloud

from util.csv_name_getter import get_csv_name


def create_pic(pos):
    df = pd.read_csv('sample.csv', index_col=0, encoding='utf-8')
    features = ['positionName', 'industryField', 'firstType', 'secondType', 'thirdType']
    data = df[features]
    if '+' or '#' in pos:
        pos = pos.replace('+', '\+')
        pos = pos.replace('#', '\#')
    position = data[data['positionName'].str.contains(pos)].reset_index(drop=True)

    text = ''
    for fea in features[1:]:
        text = text + preprocessing_word(position[fea])
    hot_words_weights = jieba.analyse.extract_tags(text, topK=50, withWeight=True, allowPOS=())
    frequencies = {_[0]: _[1] for _ in hot_words_weights}

    x, y = np.ogrid[:300, :300]
    mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)
    wc = WordCloud(font_path='msyh.ttc',
                   width=600,
                   height=300,
                   scale=2,
                   background_color="white",
                   repeat=False,
                   mask=mask)
    try:
        wc.generate_from_frequencies(frequencies)
    except ValueError:
        raise Exception('数据里没有对应的关键词')

    import matplotlib.pyplot as plt
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    # wc.to_file(f'{pos}_wc.png')

def preprocessing_word(fea):
    IF = ''
    mytext_list = []
    if fea.name != 'secondType':
        for i in fea.dropna():
            IF = IF + i
        IF_cut = jieba.cut(IF)
        for seg in IF_cut:
            if len(seg) != 1:
                mytext_list.append(seg.replace(" ", ""))
        cloud_text = ','.join(mytext_list)
    else:
        fea = fea.dropna()
        cloud_text = ','.join(fea)

    return cloud_text


if __name__ == '__main__':
    # get_csv_name()
    create_pic(get_csv_name()[1])
