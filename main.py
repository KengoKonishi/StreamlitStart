from turtle import pd
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

# st.write('◆プログレスバーの表示')

# latest_iteration = st.empty()
# bar = st.progress(0)


# for i in range(100):
#     latest_iteration.text(f'準備中... {i+1}%')
#     bar.progress(i+1)
#     time.sleep(0.01)
# '準備できました！'


st.write('◆カラムの分割')
left_column, right_column = st.columns(2)
button = left_column.button('ボタンを押してみよう！')
if button:
    right_column.write('Hello!!')

st.write('◆expanderの活用')
expander = st.expander('1+1=')
expander.write('2')

expander_size = st.expander('日本の府は？')
expander_size.write('大阪府')
expander_size.write('京都府')


st.write('◆sliderの活用')
condition = st.slider('あなたの今の調子は？',0, 100, 50)
'コンディション：', condition

st.write('◆TextBox')
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味は、',text

st.write('◆SelectBox')
option = st.selectbox(
    '好きな数字を教えて！',
    list(range(1,11))
)
'あなたの好きな数字は、', option, 'です！'

st.write('◆Image')
if st.checkbox('画像を表示させる'):
    sake_img = Image.open('kawadesake_nnbaeyaq57.jpg')
    st.image(sake_img, caption='日本酒', use_column_width=True)

st.write('◆DataFrame')
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0))

st.write('◆MarkDown記法')
"""
# 章
## 節
### 頂
```python
import pandas as pd
```
# """
st.write('◆Chartmap～新宿周辺のチャート～')
df_chart = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

st.map(df_chart)