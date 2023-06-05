import streamlit as st
from PIL import Image



st.write('# ★체질량 계산기★')

st.info("체질량 지수는 자신의 몸무게를 키의 제곱으로 나눈 값 입니다.")

height = st.number_input('키를 입력해주세요. (cm)',value = 160, step=1)
st.write(height,'cm')

weight = st.number_input('체중을 입력해주세요 (kg)',value = 50, step=1)
st.write(weight,'kg')

bmi = weight/((height/100)**2)

def bmi_range(bmi):
    if bmi>=25:
        st.error('비만입니다')
    elif bmi>= 23:
        st.warning('과체중입sl다.')
    elif bmi>= 18.5:
        st.success('정상입니다.')
    else:
        st.warning('저체중입니다')
        

if st.button('계산'):
    st.write('당신의 체질량 지수는', round(bmi,2),'입니다. ')
    bmi_range(bmi)
    
    

st.balloons()


image = Image.open('/home/ubuntu/바탕화면/sm_python/dolphin.jpg')

st.image(image, caption='Happy and Cute dolphin')