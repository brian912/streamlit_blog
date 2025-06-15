import streamlit as st

# 페이지 설정
st.set_page_config(page_title="라멘 블로그", layout="wide")

# 사이드바 메뉴 정의
menu = st.sidebar.selectbox("📂 탐색할 주제를 선택하세요", [
    "라멘이란 무엇인가?",
    "지역별 라멘 스타일 소개",
    "최근 주목받는 라멘 트렌드",
    "한국에서의 라멘 문화"
])

# 1. 라멘이란 무엇인가?
if menu == "라멘이란 무엇인가?":
    st.title("🍜 라멘이란 무엇인가?")
    st.markdown("""
    라멘은 단순한 한 끼 식사를 넘어서, 재료와 조리자의 철학, 그리고 지역적 배경이 혼합된 '음식의 서사'입니다.

    - **기원**: 중국에서 유입된 국수 문화가 일본에서 현지화되며 탄생
    - **핵심**: 국물, 면, 고명 세 가지 축이 만드는 무한한 조합
    - **정체성**: 지방, 기후, 철학, 심지어 셰프의 정서까지 반영
    
    라멘은 기술이자 예술이며, 하나의 그릇에 담긴 이야기입니다.
    """)
    st.image("707c879dd9414.png", caption="정제된 쇼유 라멘 - 깊고 섬세한 맛의 정점")

# 2. 지역별 라멘 스타일 소개
elif menu == "지역별 라멘 스타일 소개":
    st.title("🗾 일본 지역별 라멘 스타일")
    st.markdown("일본 각지의 지역성과 식재료가 깃든 대표적인 라멘 스타일들을 소개합니다.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🍶 도쿄 쇼유")
        st.markdown("닭육수 기반에 간장을 더한 맑고 깔끔한 국물. 가장 기본이 되는 라멘.")
        st.image("Soy_ramen.png", caption="도쿄 쇼유 라멘")

        st.subheader("🌶 삿포로 미소")
        st.markdown("추운 지역 특성상 미소(된장)로 짜고 진하게. 고소하고 두텁다.")
        st.image("cts1008_0.png", caption="삿포로 미소 라멘")

        st.subheader("🍜 하카타 돈코츠")
        st.markdown("하얗고 뽀얀 돼지뼈 국물. 빠른 조리와 중독적인 풍미가 특징.")
        st.image("DanboRamenDazaifu.png", caption="하카타 돈코츠 라멘")

    with col2:
        st.subheader("💧 키타카타")
        st.markdown("시원한 간장 국물과 넓은 납작면. 후쿠시마현의 명물.")
        st.image("big_n202203073u4ahs113337422637.png", caption="키타카타 라멘")

        st.subheader("🍢 와카야마")
        st.markdown("돈코츠와 간장이 절묘하게 섞인 진한 스프. 두 개의 조화.")
        st.image("big_n20220307i79iee114321650603.png", caption="와카야마 라멘")

        st.subheader("🧊 아사히카와")
        st.markdown("표면에 라드(돼지기름) 층이 형성돼 뜨거움이 오래 유지됨. 쇼유 기반.")
        st.image("big_n20220307383jyf113328550599.png", caption="아사히카와 라멘")

# 3. 최근 주목받는 라멘 트렌드
elif menu == "최근 주목받는 라멘 트렌드":
    st.title("🔥 최근 유행하는 라멘 스타일")

    st.subheader("🥩 지로계 라멘 (Jiro-kei)")
    st.markdown("""
    - 극단적인 양과 조합의 폭발
    - 산처럼 쌓인 숙주와 강한 마늘맛
    - 규칙을 깨는 자유로운 라멘
    """)
    st.image("20240606＿085413.png", caption="지로계 라멘")

    st.subheader("🥚 이에케 라멘 (Ie-kei)")
    st.markdown("""
    - 요코하마발 진한 돈코츠+쇼유의 결합
    - 김과 시금치, 굵은 면발이 상징
    - 짠맛과 육향의 극대화
    """)
    st.image("2e8ac9e6fdee38fb487b887bfa77af29-1920x1080.png", caption="이에케 라멘")

    st.subheader("🧪 창케 라멘 (창작계)")
    st.markdown("""
    - 정해진 틀이 없는 실험적 라멘
    - 트러플, 해산물, 중화식, 서양식 등 변주
    - 셰프의 창의성으로 빛나는 그릇
    """)
    st.image("image.png", caption="창작 라멘 (창케)")

# 4. 한국에서의 라멘 문화
elif menu == "한국에서의 라멘 문화":
    st.title("🇰🇷 한국에서 라멘은 어떻게 소비되고 있을까?")
    st.markdown("""
    한국에서도 라멘은 일식의 대표주자로 자리잡았지만, 여전히 라멘의 본질을 놓치고 있는 경우도 많습니다.

    ### ✅ 인기 배경
    - 일본 여행 후 입맛의 기억
    - 유튜브, SNS로 퍼지는 '덕후 콘텐츠'
    - 가성비보단 '가심비'를 추구하는 세대

    ### ⚠️ 현주소
    - 대형 프랜차이즈의 표준화된 맛
    - 직접 우려내지 않고 공급받은 농축 스프 사용
    - 셰프의 철학보단 비즈니스 모델이 중심

    그럼에도 불구하고 '진짜 라멘'을 만들고자 하는 셰프들과 덕후들은 꾸준히 움직이고 있습니다.
    """)
    st.image("824e34dc29b32.png", caption="함께라멘데이 2022 - 전국의 라멘 스탬프 투어")

    st.success("🙌 라멘에 대한 진정성과 실력, 둘 다 갖춘 셰프들이 점점 늘고 있습니다.")
    st.markdown("---")
    st.markdown("> 🧠 _라멘은 국물의 깊이만큼 사람의 진심이 담긴 그릇이다._")