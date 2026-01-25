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
location = st.selectbox(
    "📍 Select your location",
    ["Urban (City)", "Semi-Urban", "Rural", "Coastal", "Hilly"]
)

# ---------- MAIN ACTION ----------
st.divider()

st.subheader("📊 Climate Impact Analysis")
st.subheader("📍 Your Location")

location = st.selectbox(
    "Select your region",
    ["Urban City", "Coastal Area", "Mountain Region", "Hot Climate", "Cold Climate"]
)

if st.button("🌱 Analyze My Climate Impact"):

    # Carbon calculations
    driving_emission = km_driven * 0.21
    ac_emission = ac_hours * 1.5
    total_carbon = driving_emission + ac_emission

    st.subheader("🌍 Carbon Footprint Breakdown")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🚗 Driving", f"{driving_emission:.2f} kg CO₂")

    with col2:
        st.metric("❄️ AC Usage", f"{ac_emission:.2f} kg CO₂")

    with col3:
        st.metric("🌱 Total", f"{total_carbon:.2f} kg CO₂")
   
    st.subheader("🌱 Personalized Climate Tips")

if location == "Urban City":
    st.info("🚲 Use public transport or cycle for short distances. Urban emissions are transport-heavy.")

elif location == "Coastal Area":
    st.info("🌊 Reduce plastic use and save energy — coastal regions are vulnerable to climate change.")

elif location == "Mountain Region":
    st.info("🏔️ Use clean heating methods and avoid deforestation to protect fragile ecosystems.")

elif location == "Hot Climate":
    st.info("☀️ Use energy-efficient ACs and maximize natural ventilation.")

elif location == "Cold Climate":
    st.info("❄️ Insulate homes properly to reduce heating emissions.")

    carbon = (km_driven * 0.21) + (ac_hours * 1.5)

    st.subheader("🔁 What If You Reduce Your Impact?")

    reduced_km = km_driven * 0.7      # 30% less driving
    reduced_ac = ac_hours * 0.8       # 20% less AC use

    reduced_carbon = (reduced_km * 0.21) + (reduced_ac * 1.5)

    savings = carbon - reduced_carbon

    st.write(f"🌍 **Current footprint:** {carbon:.2f} kg CO₂/day")
    st.write(f"🌱 **After small changes:** {reduced_carbon:.2f} kg CO₂/day")

    st.success(f"💚 You could save **{savings:.2f} kg CO₂ per day**")
    st.success("✅ Analysis Complete")

    st.metric(
        label="🌎 Estimated Daily Carbon Footprint",
        value=f"{carbon:.2f} kg CO₂/day"
    )

    # ---------- CARBON BREAKDOWN ----------
    st.subheader("📈 Carbon Footprint Breakdown")

    driving_emission = km_driven * 0.21
    ac_emission = ac_hours * 1.5

    if diet == "Non-Vegetarian":
        diet_emission = 2
    elif diet == "Mixed":
        diet_emission = 1
    else:
        diet_emission = 0

    chart_data = {
        "Source": ["Driving", "AC Usage", "Diet"],
        "kg CO₂/day": [driving_emission, ac_emission, diet_emission]
    }

    st.bar_chart(chart_data, x="Source", y="kg CO₂/day")

    st.divider()

    st.subheader("💡 Personalized Recommendations")
st.markdown("### 📍 Location-Based Climate Tips")

if location == "Urban (City)":
    st.write("🚇 Prefer metro, buses, or carpooling to reduce traffic emissions.")
    st.write("🌱 Use energy-efficient appliances and rooftop solar if possible.")

elif location == "Semi-Urban":
    st.write("🚲 Use bicycles or shared transport for short distances.")
    st.write("💡 Switch to LED lighting to save electricity.")

elif location == "Rural":
    st.write("🌾 Use solar pumps and avoid burning crop waste.")
    st.write("🌳 Plant native trees around homes and farms.")

elif location == "Coastal":
    st.write("🌊 Conserve water and avoid plastic waste near beaches.")
    st.write("🌬️ Use natural ventilation to reduce AC usage.")

elif location == "Hilly":
    st.write("🏔️ Insulate homes properly to reduce heating needs.")
    st.write("🚶 Prefer walking for short distances on slopes.")

    if km_driven > 10:
        st.write("🚍 Try public transport or carpool at least 2 days a week.")

    if ac_hours > 5:
        st.write("❄️ Reduce AC usage by 1 hour per day to save energy.")

    if diet == "Non-Vegetarian":
        st.write("🥦 Try adding more plant-based meals to your diet.")

    st.info("Small daily changes create a big climate impact 🌱")
