import streamlit as st
import plotly.graph_objects as go

def plot_radar_chart(attributes):
    labels = list(attributes.keys())
    values = list(attributes.values())
    values += values[:1]
    labels += labels[:1]

    fig = go.Figure(data=[
        go.Scatterpolar(r=values, theta=labels, fill='toself', name='性能雷达')
    ])
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)