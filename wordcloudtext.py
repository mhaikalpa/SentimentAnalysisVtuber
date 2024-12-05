import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
os.chdir(sys.path[0])

# read text
text = open('PositiveComment.txt', mode='r', encoding='utf-8').read()
stopwords = STOPWORDS

wc = WordCloud(
        background_color='white',
        stopwords=stopwords,
        height=600,
        width=600
)

wc.generate(text)

# Save File
wc.to_file('PositiveComment.png')