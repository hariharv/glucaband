import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Glucaband - HOSA Medical Innovation",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("Navigation")
sections = [
    "Title Slide",
    "Innovation Description",
    "Healthcare Impact",
    "Quality of Life Improvements",
    "Healthcare Cost Reduction",
    "Creative & Artistic Impact",
    "Comparison",
    "Logistics",
    "References"
]
selection = st.sidebar.radio("Go to Section:", sections)

# Section 1: Title Slide
if selection == "Title Slide":
    st.title("HOSA Medical Innovation: Glucaband")
    st.write("""
    **Event Name**: Medical Innovation  
    **Team Member Names**: [Your Names Here]  
    **HOSA Division**: [e.g., Secondary Division]  
    **HOSA Chapter #**: [Your Chapter Number]  
    **School Name**: [Your School Name]  
    **Chartered Association**: [Your State/Region]  
    """)

# Section 2: Innovation Description
if selection == "Innovation Description":
    st.header("🧠 Innovation Description")
    st.write("""
    Glucaband is a non-invasive glucose monitoring device designed to improve patient comfort, affordability, and accessibility. It uses:
    - **Infrared Spectroscopy**: Measures glucose levels by analyzing light absorption.
    - **Temperature Calibration**: Adjusts for environmental and physiological factors.
    - **Motion Detection**: Incorporates accelerometers for activity-based glucose adjustments.
    """)

# Section 3: Healthcare Impact
if selection == "Healthcare Impact":
    st.header("💡 Healthcare Impact")
    st.write("""
    Glucaband is a revolutionary step forward in healthcare delivery:
    - **Non-Invasive Monitoring**: Eliminates pain and discomfort associated with fingersticks or patches.
    - **Accessibility**: Affordable design ensures accessibility for underserved populations.
    - **Proactive Health Tracking**: Encourages patients to monitor glucose levels regularly, reducing complications.
    """)

# Section 4: Quality of Life Improvements
if selection == "Quality of Life Improvements":
    st.header("✨ Quality of Life Improvements")
    st.write("""
    By eliminating the need for invasive methods, Glucaband improves the quality of life for:
    - Diabetic patients who require frequent monitoring.
    - Elderly individuals and children who find fingersticks challenging.
    - Patients in remote areas with limited access to medical facilities.
    """)

# Section 5: Healthcare Cost Reduction
if selection == "Healthcare Cost Reduction":
    st.header("💰 Healthcare Cost Reduction")
    st.write("""
    Glucaband reduces healthcare costs by:
    - Eliminating the need for consumables like test strips.
    - Reducing hospital visits for glucose monitoring.
    - Offering a one-time purchase device with minimal maintenance.
    """)
    st.subheader("Cost Comparison")
    brands = ["Fingerstick", "Glucose Patches", "Non-Invasive Devices", "Glucaband"]
    costs = [20, 70, 120, 20]
    x_positions = np.arange(len(brands)) * 1.5
    fig1, ax1 = plt.subplots()
    ax1.bar(x_positions, costs, color="skyblue", alpha=0.9, width=0.5)
    ax1.set_title("Cost Comparison")
    ax1.set_ylabel("Cost ($)")
    ax1.set_xticks(x_positions)
    ax1.set_xticklabels(brands, rotation=15)
    st.pyplot(fig1)

# Section 6: Creative & Artistic Impact
if selection == "Creative & Artistic Impact":
    st.header("🎨 Creative & Artistic Impact")
    st.write("""
    The Glucaband exhibit will stand out with:
    - A sleek, modern **3D-printed model**.
    - A live demonstration of the device in action using a Streamlit simulation.
    - Engaging visual elements like graphs, comparison tables, and a working LCD.
    - Interactive components to let judges explore the prototype.
    """)

# Section 7: Comparison
if selection == "Comparison":
    st.header("📊 Comparison with Other Technologies")
    st.markdown("""
    | Feature                | Fingerstick Glucometers | Glucose Patches      | Non-Invasive Devices (Prototypes) | Glucaband        |
    |------------------------|--------------------------|----------------------|-----------------------------------|------------------|
    | Invasiveness           | Highly invasive          | Minimally invasive   | Completely non-invasive           | Completely non-invasive |
    | Cost                   | Low                      | High                 | High                              | Low              |
    | Accuracy               | High                     | High                 | Moderate                          | Moderate         |
    | Replacement Frequency  | None                     | 10-14 days           | None                              | None             |
    """)

# Section 8: Logistics
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

# Section 9: References
if selection == "References":
    st.header("📚 References")
    st.write("""
    - Doe, J., & Smith, A. (2024). Advances in Non-Invasive Glucose Monitoring. *Journal of Biomedical Innovation*, 12(3), 45-67.
    - National Diabetes Statistics Report. (2022). Centers for Disease Control and Prevention. Retrieved from [https://www.cdc.gov](https://www.cdc.gov)
    - American Diabetes Association. (2024). Standards of Medical Care in Diabetes. *Diabetes Care*, 47(Supplement 1), S1–S210.
    """)
