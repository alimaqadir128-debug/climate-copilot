import os
import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Climate Copilot 🌍",
    page_icon="🌱",
    layout="centered"
)

# ---------- HEADER ----------
st.markdown(
    "<h1 style='text-align: center;'>🌍 Climate Copilot</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; font-size:18px;'>Your personalized AI assistant for sustainable living</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------- SIDEBAR ----------
st.sidebar.header("⚙️ Your Daily Lifestyle")
st.sidebar.write("Fill in your details below")

km_driven = st.sidebar.number_input(
    "🚗 Kilometers driven per day",
    min_value=0.0,
    step=1.0
)

ac_hours = st.sidebar.number_input(
    "❄️ AC usage (hours/day)",
    min_value=0.0,
    step=0.5
)

diet = st.sidebar.selectbox(
    "🥗 Diet type",
    ["Vegetarian", "Mixed", "Non-Vegetarian"]
)

location = st.sidebar.selectbox(
    "📍 Select your location",
    ["Urban (City)", "Semi-Urban", "Rural", "Coastal", "Hilly"]
)

st.divider()

# ---------- MAIN ----------
st.subheader("📊 Climate Impact Analysis")

if st.button("🌱 Analyze My Climate Impact"):

    # ---------- CALCULATIONS ----------
    driving_emission = km_driven * 0.21
    ac_emission = ac_hours * 1.5

    if diet == "Non-Vegetarian":
        diet_emission = 2
    elif diet == "Mixed":
        diet_emission = 1
    else:
        diet_emission = 0

    total_carbon = driving_emission + ac_emission + diet_emission

    # ---------- METRICS ----------
    st.subheader("🌍 Carbon Footprint Breakdown")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🚗 Driving", f"{driving_emission:.2f} kg CO₂")

    with col2:
        st.metric("❄️ AC Usage", f"{ac_emission:.2f} kg CO₂")

    with col3:
        st.metric("🌱 Total", f"{total_carbon:.2f} kg CO₂")

    # ---------- BAR CHART ----------
    chart_data = {
        "Source": ["Driving", "AC Usage", "Diet"],
        "kg CO₂/day": [driving_emission, ac_emission, diet_emission]
    }

    st.bar_chart(chart_data, x="Source", y="kg CO₂/day")

    # ---------- LOCATION-BASED CLIMATE TIPS ----------
    st.subheader("📍 Location-Based Climate Tips")

    if location == "Urban (City)":
        st.info("🚇 Use public transport, carpooling, or cycling to reduce traffic emissions.")
        st.info("🌱 Install energy-efficient appliances and rooftop solar panels.")

    elif location == "Semi-Urban":
        st.info("🚲 Prefer bicycles or shared transport for short distances.")
        st.info("💡 Switch to LED lighting and energy-efficient fans.")

    elif location == "Rural":
        st.info("🌾 Avoid burning crop residue; compost organic waste.")
        st.info("🌳 Plant native trees and use solar-powered pumps.")

    elif location == "Coastal":
        st.info("🌊 Reduce plastic usage to protect marine life.")
        st.info("🌬️ Use natural ventilation to minimize AC consumption.")

    elif location == "Hilly":
        st.info("🏔️ Improve insulation to reduce heating needs.")
        st.info("🔥 Use clean heating methods and avoid deforestation.")

    # ---------- PERSONALIZED SUGGESTIONS ----------
    st.subheader("💡 Personalized Recommendations")

    if km_driven > 10:
        st.write("🚍 Try reducing driving by carpooling at least twice a week.")

    if ac_hours > 5:
        st.write("❄️ Reduce AC usage by 1 hour daily to save energy.")

    if diet == "Non-Vegetarian":
        st.write("🥦 Try adding more plant-based meals to lower your carbon footprint.")

    # ---------- IMPACT REDUCTION ----------
    st.subheader("🔁 What If You Reduce Your Impact?")

    reduced_km = km_driven * 0.7
    reduced_ac = ac_hours * 0.8
    reduced_carbon = (reduced_km * 0.21) + (reduced_ac * 1.5) + diet_emission

    savings = total_carbon - reduced_carbon

    st.success(f"🌱 You could reduce **{savings:.2f} kg CO₂ per day** with small changes.")
    st.success("✅ Analysis Complete")
