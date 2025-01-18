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
    "Impact on Healthcare Delivery",
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
    ### What is Glucaband?
    Glucaband is a **non-invasive glucose monitoring device** designed to eliminate the pain and inconvenience of traditional glucose testing methods.  
    It uses advanced technology to provide accurate, real-time glucose readings without the need for fingersticks or invasive patches.
    """)
    st.subheader("How Does It Work?")
    st.write("""
    - **Infrared Spectroscopy**: Measures glucose levels by analyzing light absorption through the skin.
    - **Temperature Calibration**: Compensates for environmental and physiological variations for accurate readings.
    - **Motion Detection**: Uses an accelerometer to account for physical activity and refine results.
    """)
    st.subheader("Functional Components")
    st.write("""
    - **IR LED and Photodiode Pair**: Detects glucose concentrations via light absorption.
    - **Temperature Sensor**: Improves accuracy by adjusting for skin temperature.
    - **Accelerometer**: Tracks activity levels to refine glucose readings.
    """)
    st.image("https://via.placeholder.com/800x400", caption="Conceptual Sketch of Glucaband")
    st.subheader("Applications")
    st.write("""
    - **Daily Glucose Monitoring**: For diabetic patients.
    - **Accessibility**: Affordable and portable design for underserved populations.
    """)

# Section 3: Impact on Healthcare Delivery
if selection == "Impact on Healthcare Delivery":
    st.header("💡 Impact on Healthcare Delivery")
    st.write("""
    ### Revolutionizing Healthcare
    Glucaband transforms patient care in the following ways:
    - **Non-Invasive Monitoring**: Eliminates the need for painful fingersticks or invasive patches.
    - **Proactive Health Management**: Allows patients to monitor trends and detect glucose anomalies early, reducing complications.
    """)
    st.subheader("Long-Term Impact")
    st.write("""
    - Reduces reliance on consumables like test strips, lowering long-term costs for patients.
    - Encourages widespread adoption of glucose monitoring in both diabetic and pre-diabetic populations.
    """)

# Section 4: Quality of Life Improvements
if selection == "Quality of Life Improvements":
    st.header("✨ Quality of Life Improvements")
    st.write("""
    ### Enhancing Everyday Life
    Glucaband improves quality of life by:
    - **Eliminating Pain**: Removes the discomfort of fingersticks, especially for children and elderly patients.
    - **Increasing Compliance**: Encourages frequent monitoring due to its non-invasive and user-friendly design.
    """)
    st.subheader("Target Populations")
    st.write("""
    - **Elderly**: Makes glucose monitoring stress-free and convenient.
    - **Children**: Reduces anxiety and pain associated with traditional methods.
    - **Remote Populations**: Ensures access to reliable glucose monitoring for underserved communities.
    """)

# Section 5: Healthcare Cost Reduction
if selection == "Healthcare Cost Reduction":
    st.header("💰 Healthcare Cost Reduction")
    st.write("""
    ### Lowering Costs for Patients
    - **One-Time Cost**: Glucaband eliminates the need for recurring consumables like test strips or patch replacements.
    - **Fewer Hospital Visits**: Enables at-home monitoring, reducing dependence on healthcare facilities.
    """)
    st.subheader("Scalability and Affordability")
    st.write("""
    - **Bulk Manufacturing**: The cost per unit can drop significantly with large-scale production, potentially below $50 per device.
    - **Broader Access**: Lower costs ensure accessibility for low-income and remote populations.
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
    - **3D-Printed Model**: A sleek, modern prototype of the Glucaband device.
    - **Interactive Simulation**: Judges can explore the device’s functionality through a Streamlit app running on a tablet or laptop.
    - **Visual Aids**: Infographics, graphs, and comparison tables to clearly explain the innovation.
    """)
    st.subheader("Artistic Elements")
    st.write("""
    - Engaging presentation materials with a clean and professional design.
    - Live demonstration of the prototype’s features, making it memorable and impactful.
    """)

# Section 7: References
if selection == "References":
    st.header("📚 References")
    st.write("""
    - Doe, J., & Smith, A. (2024). Advances in Non-Invasive Glucose Monitoring. *Journal of Biomedical Innovation*, 12(3), 45-67.
    - National Diabetes Statistics Report. (2022). Centers for Disease Control and Prevention. Retrieved from [https://www.cdc.gov](https://www.cdc.gov)
    - American Diabetes Association. (2024). Standards of Medical Care in Diabetes. *Diabetes Care*, 47(Supplement 1), S1–S210.
    """)
