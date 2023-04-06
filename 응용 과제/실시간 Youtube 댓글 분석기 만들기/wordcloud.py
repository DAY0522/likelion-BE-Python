from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy as np
from comments_frequency import frequency

okt = Okt()

wc = WordCloud(font_path='NanumPen', width=400, height=400, scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(frequency)
plt.figure()
plt.imshow(gen)

wc.to_file('words_frequency.png')