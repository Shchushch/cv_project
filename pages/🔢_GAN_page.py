import streamlit as st
from PIL import Image
from neiro import get_digit
info=("Вставить описание")

def update_slider():
    st.session_state.slider = st.session_state.numeric
def update_numin():
    st.session_state.numeric = st.session_state.slider

if st.button("Что это такое?",type='secondary'):
    st.divider()
    info
    st.divider()


#@st.cache_data

with st.container():        
        digit = st.number_input('Введите желаемую цифру',key = 'numeric', min_value=0, max_value=9, value=7,on_change=update_slider)
        slider_value = st.slider('Можете ещё вот так выбрать', min_value = 0, 
                            value = digit, 
                            max_value = 9,
                            step = 1,
                            key = 'slider', on_change= update_numin)
        gen_pic=st.button('Генерируй',type='primary',key='gen_pic',use_container_width=True)

if gen_pic:
    f"Тут будет картинка со сгенерированной цифрой **{digit}**"      
