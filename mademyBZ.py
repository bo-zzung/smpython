import streamlit as st
import requests
import json
from datetime import datetime, timedelta
#제목(이모티콘을 추가해 귀여움을 추가함)
st.title('주간 날씨 ☀️⛅🌧️')

# 현재 날짜 가져오기
current_date = datetime.now().date()

# 현재 날짜부터 일주일간의 날짜 리스트 생성
dates = [current_date + timedelta(days=i) for i in range(7)]

# 특정 날짜의 날씨 데이터를 가져오는 함수 생성
def get_weather(date):
    date_str = date.strftime("%Y-%m-%d")
    response = requests.get(f'https://api.weatherapi.com/v1/forecast.json?key=c8a4a4ab89864d49b7211713230906&q=Busan&dt={date_str}')
    jsonObj = json.loads(response.text)
    temperature = (jsonObj['forecast']['forecastday'][0]['day']['avgtemp_c'])
    condition = (jsonObj['forecast']['forecastday'][0]['day']['condition']['text'])
    return temperature, condition

# 각 날짜의 날씨 데이터를 저장하는 변수 생성
weather_data = {}

# 각 날짜에 대한 날씨 데이터를 가져와 변수에 저장
for date in dates:
    temperature, condition = get_weather(date)
    weather_data[date] = {
        'temperature': temperature,
        'condition': condition
    }

# 달력을 생성하고 날짜를 클릭할 때 날씨를 표시
for date in dates:
    date_str = date.strftime("%Y-%m-%d")
    st.divider()
    if st.button(date_str, key=date_str, help="날씨를 알고 싶다면👇"):
        weather = weather_data[date]
        st.write(f"오늘은 {date_str} 입니다. 기온은 {weather['temperature']}°C 이며, 하늘은 {weather['condition']} 하겠습니다! 오늘도 좋은 하루 되세요😘")

temperature1 = st.slider('오늘의 기온은?', -10, 40, 25)
st.write(temperature1, '°C')

clothing_recommendation = '기온 별 옷차림 '
if temperature1 <= 4:
    clothing_recommendation = '핫팩 필수!!😵‍💫 \n 패딩, 두꺼운 코드, 누빔 옷, 기모, 목도리를 추천합니다!'
elif temperature1 <= 8:
    clothing_recommendation = '많이 추워요🥶 \n 울 코드, 히트텍, 가죽 옷, 기모를 추천합니다!'
elif temperature1 <= 11:
    clothing_recommendation = '감기 조심하세요~🤒\n 트렌치 코트, 야상, 얇은 잠바 등을 추천합니다! '
elif temperature1 <= 16:
    clothing_recommendation = '아직 쌀쌀해요!! \n 니트, 청바지, 자켓, 가디건을 추천합니다!'
elif temperature1 <= 19:
    clothing_recommendation = '따뜻해지고 있어요🤗 \n 얇은 가디건, 맨투맨, 후드, 긴바지를 추천합니다!'
elif temperature1 <= 22:
    clothing_recommendation = '봄이 왔어요🌸 \n 블라우스, 긴팔 티, 면바지, 슬랙스를 추천합니다!'
elif temperature1 <= 27:
    clothing_recommendation = '선크림 필수!☀️ \n 반팔, 얇은 셔츠, 반바지, 면바지를 추천합니다!'
else:
    clothing_recommendation = '핫뜨핫뜨 더워주거용🥵 \n 민소매, 반팔, 반바지, 린넨을 추천합니다!'

st.write("오늘은", clothing_recommendation)
