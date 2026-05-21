import streamlit as st

# 1. 페이지 기본 설정 (웹 브라우저 탭에 표시될 이름과 아이콘)
st.set_page_config(
    page_title="석리송의 포켓몬 월드!",
    page_icon="⚡",
    layout="centered"
)

# 2. 화려한 타이틀과 소개글
st.title('🎈 나의 첫 멋진 웹 사이트!! 🎈')
st.subheader('by 멋쟁이 개발자 석리송 😎')

st.markdown("""
---
### 🌟 환영합니다! 🌟
이곳은 당곡고의 자랑스러운 개발자 **석리송** 학생이 처음으로 만든 마법 같은 웹 사이트입니다. 
아래의 버튼들을 눌러서 특별한 효과를 체험해 보세요!
---
""")

# 3. 클릭하면 터지는 풍선 및 눈 효과 버튼
col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button('🎉 축하 풍선 빵빵 터뜨리기! 🎉', use_container_width=True):
        st.balloons()
        st.success("축하합니다! 성공적으로 첫 웹 앱을 실행하셨습니다! 🥳")

with col_btn2:
    if st.button('❄️ 낭만 가득 눈 내리게 하기! ❄️', use_container_width=True):
        st.snow()
        st.info("시원한 눈이 내립니다! ⛄")

st.write("") # 빈 줄로 간격 넓히기

# 4. 포켓몬 이미지와 축하 메시지 팍팍 넣기!
st.markdown("### 🐾 석리송의 첫 걸음을 축하해 주는 포켓몬 친구들!")

# 3개의 열을 만들어 포켓몬 배치하기
col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png", 
        caption="피카츄 (Pikachu)", 
        use_container_width=True
    )
    st.write("⚡ *'피카피카! 첫 웹사이트 개설을 너무너무 축하해!'*")

with col2:
    st.image(
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png", 
        caption="파이리 (Charmander)", 
        use_container_width=True
    )
    st.write("🔥 *'내 꼬리의 불꽃만큼 뜨거운 열정으로 응원할게!'*")

with col3:
    st.image(
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png", 
        caption="꼬부기 (Squirtle)", 
        use_container_width=True
    )
    st.write("💧 *'앞으로도 멋진 프로그램 많이 만들어줘! 꼬북꼬북!'*")

# 5. 하단 푸터(Footer)
st.markdown("""
---
<center style="color: gray; font-size: 0.8em;">
    © 2026 석리송 개발자. All rights reserved. @당곡고등학교
</center>
""", unsafe_html=True)
