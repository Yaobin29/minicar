import streamlit as st
import json
import pandas as pd
from utils import plot_radar_chart

st.set_page_config(page_title="四驱兄弟图鉴", layout="wide")

st.title("🏎️ 四驱兄弟 四驱车图鉴")
st.markdown("欢迎来到《四驱兄弟》迷你四驱车资料图鉴！")

# 加载数据
with open("data/cars.json", "r", encoding="utf-8") as f:
    cars = json.load(f)

car_names = [car["name"] for car in cars]
selected_car = st.selectbox("选择一辆四驱车", car_names)

car = next(c for c in cars if c["name"] == selected_car)

# 展示基本信息
col1, col2 = st.columns([1, 2])
with col1:
    st.image(f"images/{car['image']}", use_column_width=True)
with col2:
    st.subheader(f"{car['name']}（{car['character']}）")
    st.write(f"首次登场：{car['appearance']['anime']} - {car['appearance']['episode']}")
    st.markdown(f"**综合排名：** 🥇 {car['rank']['overall']}")
    plot_radar_chart(car["attributes"])
