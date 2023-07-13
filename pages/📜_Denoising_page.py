import streamlit as st
from PIL import Image
from neiro import get_denoised
info=("Вставить описание")

if st.button("Что это такое?",type='secondary'):
    st.divider()
    info
    st.divider()

uploaded_file=st.file_uploader('# Загрузи сюда картинку c зашумленным текстом',type=["jpg", "jpeg", "png"])
col1, col2 = st.columns([1,1])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    col1.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button('Чисть',use_container_width=True,type='primary'):
        #st.write(image)
        #st.write(image)
        col2.success("Вывод очищенной картинки")