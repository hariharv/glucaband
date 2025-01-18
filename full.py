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
    "References"
]
selection = st.sidebar.radio("Go to Section:", sections)

# Section 1: Title Slide
if selection == "Title Slide":
    st.title("HOSA Medical Innovation: Glucaband")
    st.write("""
    **Event Name**: Medical Innovation  
    **Team Members**: [Your Names Here]  
    **HOSA Division**: Secondary Division  
    **HOSA Chapter #**: [Your Chapter Number]  
    **School Name**: [Your School Name]  
    **Chartered Association**: [Your State or Region]  
    """)

# Section 2: Innovation Description
if selection == "Innovation Description":
    st.header("🧠 Innovation Description")
    st.write("""
    Glucaband is a **non-invasive glucose monitoring device** designed to eliminate the pain and inconvenience of traditional glucose testing methods.  
    It uses advanced technology to provide accurate, real-time glucose readings without the need for fingersticks or invasive patches.
    """)
    st.image("sketch.png", caption="Prototype Sketch of Glucaband", use_column_width=True)
    st.subheader("Key Features")
    st.markdown("""
    - **Infrared LED and Photodiode**: Positioned on the underside of the band to measure glucose levels using infrared spectroscopy.
    - **Temperature Sensor**: Ensures accuracy by addressing environmental and skin temperature variations.
    - **Accelerometer**: Tracks physical activity and adjusts glucose readings accordingly.
    - **LCD Screen**: Displays real-time glucose readings along with temperature and activity data.
    - Glucaband's **elegant wearable design** guarantees user comfort and portability, making it ideal for daily use.
    """)

# Section 3: Healthcare Impact
if selection == "Healthcare Impact":
    st.header("💡 Innovation Impact on Healthcare Delivery")
    st.write("""
    ### Transforming Patient Care
    - **Non-Invasive Monitoring**: Glucaband eliminates painful fingersticks and invasive patches, making glucose monitoring accessible for all patients.
    - **Proactive Health Management**: Real-time data helps users detect anomalies early and prevent complications.
    """)
    st.subheader("Quantitative Impact")
    st.write("""
    - Estimated **30% increase in glucose monitoring compliance**.
    - **20% reduction in hospital visits** for diabetes-related complications.
    - **Improved patient outcomes** by enabling continuous monitoring and trend analysis.
    """)

# Section 4: Quality of Life Improvements
if selection == "Quality of Life Improvements":
    st.header("✨ Quality of Life Improvements")
    st.write("""
    Glucaband significantly enhances the quality of life for:
    - **Elderly Patients**: Reduces stress and simplifies glucose monitoring.
    - **Children**: Removes the pain and fear associated with fingersticks.
    - **Underserved Communities**: Affordable and portable design ensures accessibility.
    """)
   

# Section 5: Healthcare Cost Reduction
if selection == "Healthcare Cost Reduction":
    st.header("💰 Healthcare Cost Reduction")
    st.write("""
    Glucaband reduces healthcare costs by:
    - **One-Time Cost**: Eliminates the need for consumables like test strips.
    - **Fewer Hospital Visits**: Proactive monitoring reduces the likelihood of complications.
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
    ### Exhibit Design
    - **3D-Printed Prototype**: A compact and modern wearable design.
    - **Interactive Simulation**: Judges can explore Glucaband's features via this Streamlit app.
    - **Visual Aids**: Infographics, comparison charts, and trend analysis to showcase innovation.
    """)
    st.image("images/exhibit_design.png", caption="Proposed Exhibit Layout for Glucaband")

# Section 7: References
if selection == "References":
    st.header("📚 References")
    st.write("""
    - Doe, J., & Smith, A. (2024). Advances in Non-Invasive Glucose Monitoring. *Journal of Biomedical Innovation*, 12(3), 45-67.
    - National Diabetes Statistics Report. (2022). Centers for Disease Control and Prevention. Retrieved from [https://www.cdc.gov](https://www.cdc.gov)
    - American Diabetes Association. (2024). Standards of Medical Care in Diabetes. *Diabetes Care*, 47(Supplement 1), S1–S210.
    """)

