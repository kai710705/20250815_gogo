import numpy as np
import pandas as pd
import streamlit as st  

st.title("Demo PAGE")
st.write("123")
st.write("##123")

arr1=np.array([1, 2,3,4,5,6])
st.write(arr1)

df1=pd.DataFrame([[11,22,33,44],[50,60,70,80]])
st.write(df1)
st.table(df1)

st.write("### 核取方塊")
r1=st.checkbox("外帶")
if r1:
    st.write("您選擇了外帶") 
else:
    st.write("您沒有選擇外帶")

checks=st.columns(3)
txt=''
with checks[0]:
    c1=st.checkbox("選項1")
    if c1:
        txt+="選項1 "
with checks[1]:
    c2=st.checkbox("選項2")
    if c2:
        txt+="選項2 "
with checks[2]:
    c3=st.checkbox("選項3")
    if c3:
        txt+="選項3 "
st.write(txt)

st.write("### 單選按鈕")
r4=st.radio("選擇一個飲料",("選項A咖啡","選項B果汁","選項C奶茶"))
st.write("您選擇了:",r4)
r5=st.radio("選擇一個飲料",("選項A咖啡","選項B果汁","選項C奶茶"),key="radio2")
st.write("您選擇了:",r5)

st.info("### 滑桿")
num=st.slider("選擇一個數字",min_value=1,max_value=100,value=50,step=1)
st.write("您選擇的數字是:",num)

st.sidebar.info("### 下拉選單")    
city=st.sidebar.selectbox("選擇一個城市",("台北","台南","其他"))
if city == "台北":
    st.sidebar.info("您選擇的城市是: 台北")
elif city == "台南":
    st.sidebar.info("您選擇的城市是: 台南")
elif city == "其他":
    st.sidebar.info("您選擇的城市是: 其他")

