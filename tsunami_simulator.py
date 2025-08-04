import streamlit as st
import math
import plotly.graph_objects as go

G = 9.81  # gravity (m/s²)

def tsunami_speed(depth):
    return math.sqrt(G * depth)

def arrival_time(distance, speed):
    return (distance / (speed * 3.6)) * 60  # minutes

st.set_page_config(page_title="Tsunami Simulator", page_icon="🌊")
st.title("🌊 Tsunami Simulator 🏝️")

st.subheader("Tsunami Parameters")
depth = st.slider("Ocean Depth (meters)", 100, 8000, 4000, 100)
distance = st.slider("Distance from Earthquake to Coast (km)", 10, 1000, 200, 10)

speed = tsunami_speed(depth)
speed_kmh = speed * 3.6
arrival = arrival_time(distance, speed)

st.info(f"Tsunami speed: **{speed_kmh:.1f} km/h** ({speed:.1f} m/s)")
st.info(f"Will reach the coast in **{arrival:.1f} minutes**")

# Plot 1: Speed vs Depth
depths = list(range(100, 8001, 100))
speeds = [tsunami_speed(d) * 3.6 for d in depths]
fig1 = go.Figure(go.Scatter(x=depths, y=speeds, mode='lines+markers', line=dict(color='#2e8fff')))
fig1.update_layout(title="Tsunami Speed vs Ocean Depth",
                  xaxis_title="Ocean Depth (meters)",
                  yaxis_title="Tsunami Speed (km/h)",
                  height=320)
st.plotly_chart(fig1, use_container_width=True)

# Plot 2: Arrival Time vs Distance
distances = list(range(10, 1001, 10))
times = [arrival_time(d, speed) for d in distances]
fig2 = go.Figure(go.Scatter(x=distances, y=times, mode='lines+markers', line=dict(color='#fba01b')))
fig2.update_layout(title="Tsunami Arrival Time vs Distance",
                   xaxis_title="Distance from Source (km)",
                   yaxis_title="Arrival Time (minutes)",
                   height=320)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Evacuation Simulator")
evac_dist = st.slider("Distance you need to reach safety (km)", 0.1, 5.0, 1.0, 0.1)
evac_speed = st.slider("Your evacuation speed (km/h)", 2, 15, 5, 1)
your_time = (evac_dist / evac_speed) * 60

if your_time < arrival:
    st.success(f"🎉 You escaped in **{your_time:.1f} minutes**! You’re safe! ⛰️")
else:
    st.error(f"💀 You needed **{your_time:.1f} minutes**, but the tsunami arrived in {arrival:.1f} minutes. Try running faster or starting closer to safety! 🌊")

st.markdown("""
**Tips:**
- Don’t wait to see the wave! Evacuate immediately if you feel an earthquake or see the sea recede quickly.
- Practice evacuation routes with your family and friends.
- Stay calm and help others, especially kids and elderly.
""")