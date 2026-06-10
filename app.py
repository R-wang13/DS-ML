import streamlit as st

st.set_page_config(page_title="MyApp", layout="wide")

st.title(''':rainbow[R-Wang 13 T]''')
st.title("🏠 หน้าหลัก ")
st.write("### Boot Camp: Data Science and Machine Learning")
st.info("7 Day Intensive Hands-on Workshop")
st.write("##### Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

if st.button(''':rainbow[ระบบคำนวณส่วนลดตามยอดซื้อ]'''):
    st.switch_page("pages/app1_discount_calc.py")
elif st.button(''':rainbow[ทำความสะอาดข้อมูล]'''):
    st.switch_page("pages/clean_app.py")
elif st.button(''':rainbow[การแปลงข้อมูล]'''):
    st.switch_page("pages/transform_app.py")
elif st.button(''':rainbow[การวิเคราะห์ข้อมูลเชิงสำรวจ]'''):
    st.switch_page("pages/EDA_app.py")
elif st.button(''':rainbow[การพยากรณ์ยอดขายแบบง่าย]'''):
    st.switch_page("pages/sale_predict.py")
elif st.button(''':rainbow[การพยากรณ์ระยะเวลาการให้บริการขนส่ง]'''):
    st.switch_page("pages/truck_predict.py") 
elif st.button(''':rainbow[การจำแนกประเภทข้อมูลยอดขาย]'''):
    st.switch_page("pages/classify_redbull_sale.py")
elif st.button(''':rainbow[การจัดกลุ่มข้อมูล]'''):
    st.switch_page("pages/clustering_segment.py")    
elif st.button(''':rainbow[ระบบแนะนำสินค้าจาก Market Basket Analysis]'''):
    st.switch_page("pages/association_items.py")
elif st.button(''':rainbow[ TCP Behavioral Association Recommendation]'''):
    st.switch_page("pages/association_recommend.py")
