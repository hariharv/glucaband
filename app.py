import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Glucaband - HOSA Medical Innovation:",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("Slides")
sections = [
    "Overview",
    "Technology & Innovation",
    "Healthcare Impact",
    "Comparison",
    "Logistics",
    "About Us",

]
selection = st.sidebar.radio("Go to Section:", sections)

# Section 1: Overview
if selection == "Overview":
    st.title("Glucaband - Non-Invasive Glucose Monitoring:")
    st.write("""
    Welcome to the Glucaband app! This portfolio showcases our innovative approach to non-invasive glucose monitoring,
    designed for the HOSA Medical Innovation competition.
    """)

# Section 2: Technology & Innovation
if selection == "Technology & Innovation":
    st.header("🔬 Technology Behind Glucaband")
    st.write("""
    Glucaband leverages innovative technologies:
    - **Infrared Spectroscopy**: Non-invasive glucose detection using IR light absorption.
    - **Temperature Calibration**: Adjusts readings for accuracy in varying conditions.
    - **Motion Detection**: Uses accelerometers to monitor activity and adjust readings accordingly.
    """)
    st.info("**Why Glucaband is Innovative:** Combines cost-effectiveness, user-friendliness, and advanced technology to redefine glucose monitoring.")

# Section 3: Healthcare Impact
if selection == "Healthcare Impact":
    st.header("💡 Healthcare Impact")
    st.write("""
    Glucaband addresses critical challenges in glucose monitoring:
    - **Improves Patient Comfort**: Eliminates the pain and inconvenience of invasive methods like fingersticks.
    - **Enhances Accessibility**: Affordable design makes glucose monitoring accessible to underserved populations.
    - **Promotes Proactive Health Monitoring**: Encourages regular glucose tracking to prevent complications.
    """)

# Section 4: Comparison
if selection == "Comparison":
    st.header("📊 Comparison with Other Technologies")
    st.write("Here's how Glucaband compares to other glucose monitoring methods:")

    # Comparison Table
    st.markdown("""
    | Feature                | Fingerstick Glucometers | Glucose Patches      | Non-Invasive Devices (Prototypes) | Glucaband        |
    |------------------------|--------------------------|----------------------|-----------------------------------|------------------|
    | Invasiveness           | Highly invasive          | Minimally invasive   | Completely non-invasive           | Completely non-invasive |
    | Cost                   | Low                      | High                 | High                              | Low              |
    | Accuracy               | High                     | High                 | Moderate                          | Moderate         |
    | Replacement Frequency  | None                     | 10-14 days           | None                              | None             |
    | Usability              | Manual                  | Automated             | Limited                           | User-friendly    |
    """)

    # Cost Comparison Graph
    brands = ["Fingerstick", "Glucose Patches", "Non-Invasive Devices", "Glucaband"]
    costs = [20, 70, 120, 45]
    x_positions = np.arange(len(brands)) * 1.5

    st.write("### Cost Comparison")
    fig1, ax1 = plt.subplots()
    ax1.bar(x_positions, costs, color="skyblue", alpha=0.9, width=0.5)
    ax1.set_title("Cost Comparison")
    ax1.set_ylabel("Cost ($)")
    ax1.set_xticks(x_positions)
    ax1.set_xticklabels(brands, rotation=15)
    st.pyplot(fig1)

    # Invasiveness Comparison Graph
    invasiveness = [4, 2, 0, 0]  # 0 = Non-invasive, 5 = Highly invasive

    st.write("### Invasiveness Level Comparison")
    fig2, ax2 = plt.subplots()
    ax2.plot(brands, invasiveness, color="red", marker="o", linestyle="-")
    ax2.set_title("Invasiveness Level Comparison")
    ax2.set_ylabel("Invasiveness Level (0=Low, 5=High)")
    ax2.set_ylim(-0.5, 5.5)
    st.pyplot(fig2)

# Section 5: Logistics
if selection == "Logistics":
    st.header("🛠 Logistics and Cost Analysis")
    st.write("""
    ### Estimated Cost Breakdown
    - **IR LED and Photodiode Pair**: $5
    - **MLX90614 Temperature Sensor**: $15
    - **Accelerometer (MPU6050)**: $10
    - **Microcontroller (Arduino)**: $25
    - **Battery and Power Supply**: $10
    - **3D-Printed Case**: $5
    
    **Total Estimated Cost per Unit**: **$70**
    """)
    st.success("**Scalability Potential:** With bulk production, costs could drop below $50 per unit.")
if selection == "About Us":
    st.header("About Us")
    st.write("""
    ### Harihar
    - **Favorite Food**: Chipotle Burrito Bowl
    - **Favorite Movie**: Oppenheimer
    - **Favorite Activity**: Playing Pickleball
    """)
    st.write("""
    ### Satvik
    - **Favorite Food**: Pasta
    - **Favorite Movie**: Baahubali 2
    - **Favorite Activity**: Rubix Cubing
    """)
# Section 6: Exhibit Plan
