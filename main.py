import streamlit as st

# 🎨 앱 제목과 소개
st.title("💡 MBTI 기반 진로 추천기")
st.markdown("당신의 성격유형(MBTI)에 따라 어울리는 진로를 추천해드릴게요! 🔍")
st.markdown("MBTI를 선택하고 아래에서 결과를 확인하세요! 😄")

# 📌 사용자 MBTI 선택
mbti_types = [
    "ISTJ 🧭", "ISFJ 🧸", "INFJ 🌌", "INTJ 🧠",
    "ISTP 🛠️", "ISFP 🎨", "INFP 📖", "INTP 🧬",
    "ESTP 🏍️", "ESFP 🎤", "ENFP 🌈", "ENTP 🧪",
    "ESTJ 📋", "ESFJ 🧑‍🤝‍🧑", "ENFJ 🎓", "ENTJ 🦁"
]

selected_mbti = st.selectbox("당신의 MBTI 유형을 선택해주세요! 👇", mbti_types)

# 🎁 추천 진로 딕셔너리
mbti_careers = {
    "ISTJ": ["🔧 엔지니어", "📊 회계사", "👮 경찰", "🧑‍⚖️ 판사"],
    "ISFJ": ["🧑‍⚕️ 간호사", "🍳 셰프", "👩‍🏫 교사", "🧘 상담사"],
    "INFJ": ["🧙 작가", "🌿 환경운동가", "👩‍🎨 디자이너", "🧠 심리학자"],
    "INTJ": ["💻 프로그래머", "🧪 연구원", "📈 전략기획가", "🔬 과학자"],
    "ISTP": ["🛠️ 정비사", "🏎️ 레이서", "🔧 기술자", "🕵️ 탐정"],
    "ISFP": ["🎨 예술가", "📸 사진작가", "🧑‍🍳 요리사", "🌍 여행가"],
    "INFP": ["✍️ 시인", "🎭 배우", "📚 에디터", "🌈 NGO 활동가"],
    "INTP": ["🧬 데이터 분석가", "🖥️ 개발자", "📚 학자", "🚀 스타트업 창업자"],
    "ESTP": ["🧗 운동선수", "📣 마케터", "🎬 영화감독", "🧑‍🚒 구조대원"],
    "ESFP": ["🎤 MC", "🕺 연예인", "📷 유튜버", "🎡 이벤트 기획자"],
    "ENFP": ["🌍 사회활동가", "📢 홍보전문가", "🧑‍🏫 교사", "🎨 창작자"],
    "ENTP": ["🧪 혁신가", "🚀 창업가", "🎙️ 방송인", "🧠 전략가"],
    "ESTJ": ["👨‍💼 관리자", "🧾 행정가", "📋 프로젝트 매니저", "🏛️ 공무원"],
    "ESFJ": ["👩‍🏫 교사", "💼 HR매니저", "🏥 간호사", "🛍️ 서비스직"],
    "ENFJ": ["🧑‍🏫 멘토", "🧭 코치", "🎓 교육자", "💬 상담가"],
    "ENTJ": ["📈 CEO", "📊 기획자", "🧠 리더십 트레이너", "⚖️ 경영컨설턴트"]
}

# 🎯 추천 결과 출력
pure_mbti = selected_mbti.split(" ")[0]
careers = mbti_careers.get(pure_mbti, [])

st.markdown("---")
st.subheader(f"🎉 {pure_mbti} 유형에게 어울리는 진로는?")
for job in careers:
    st.markdown(f"- {job}")

# 🎨 꾸미기
st.markdown("---")
st.markdown("📌 **MBTI 진로 추천**은 참고용입니다. 진짜 진로는 당신이 만들어가는 것이에요! ✨")
st.markdown("💬 궁금한 점이 있다면 아래 댓글을 남겨주세요!")

