#step_2_4.py


from pathlib import Path

import streamlit as st

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_3 import OUT_2_3, read_text_and_draw_line, read_text_from_image
from live_helper import translate_libre

st.title("✌ 인식률 체크 문자 인식 웹 앱")  # 웹 앱 제목

uploaded = st.file_uploader("인식할 이미지를 선택하세요.")  # 파일 업로더 위젯
if uploaded is not None:  # 파일이 업로드되면, 다음 코드를 실행
    tmp_path = OUT_DIR / f"{Path(__file__).stem}.tmp"  # 임시 파일 경로
    tmp_path.write_bytes(uploaded.getvalue())  # 업로드한 이미지 저장

    col_left, col_right = st.columns(2)  # 두 개의 열 생성
    with col_left:  # 첫 번째 열
        st.subheader("원본 이미지")  # 부제목
        st.image(tmp_path.as_posix())  # 원본 이미지 출력
    with col_right:  # 두 번째 열
        st.subheader("문자 인식 결과")  # 부제목
        with st.spinner(text="문자를 인식하는 중입니다..."):  # 진행 상황 표시
            read_text_and_draw_line(tmp_path)  # 문자 인식 및 박스 그리기
        st.image(OUT_2_3.as_posix())  # 결과 이미지 출력

    st.subheader("📝 인식된 텍스트 및 번역 결과")
    with st.spinner("텍스트를 번역하는 중입니다..."):
        texts = read_text_from_image(tmp_path)
        if texts:
            # for text in texts:
            #     translated = translate_libre(text, source="en", target="ko")  # 필요에 따라 source/target 변경
            #     st.markdown(f"🔹 {text}<br/>➡️ {translated}", unsafe_allow_html=True)

            full_text = " ".join(texts)  # 모든 인식된 텍스트를 공백으로 합침
            translated = translate_libre(full_text, source="en", target="ko")
            st.markdown(f"🔹 {full_text}<br/>➡️ {translated}", unsafe_allow_html=True)
        else:
            st.info("문자를 인식하지 못했습니다.")