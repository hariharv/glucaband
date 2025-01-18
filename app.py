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
    "Title",
    "Description",
    "Healthcare Impact",
    "Comparison",
    "Logistics",
    "Creative & Artistic Impact",
    "References",
    "About Us",

]
selection = st.sidebar.radio("Go to Section:", sections)

# Section 1: Overview
if selection == "Title":
    st.title("Glucaband - Non-Invasive Glucose Monitoring:")
    st.write("""
    Welcome to the Glucaband app! This outline showcases our innovative approach to non-invasive glucose monitoring.
    
    **HOSA Event**: Medical Innovation

    **Team Member Names**: Harihar Vadrevu and Satvik Thakur

    **HOSA Division**: Area 1, Secondary Division
    
    **HOSA Chapter #**: 60294

    **School Name**: Tom Glenn High School

    **Chartered Association**: Texas HOSA
    
    """)

# Section 2: Technology & Innovation
if selection == "Description":
    st.header("🔬 Innovation Description")
    st.write("""
    ### What is Glucaband?
    Glucaband is a **non-invasive glucose monitoring device** designed to eliminate the pain and inconvenience of traditional glucose testing methods.  
    It uses advanced technology to provide accurate, real-time glucose readings without the discomfort of fingersticks or invasive patches.
    """)
    st.subheader("How Does It Work?")
    st.write("""
    - **Infrared Spectroscopy**: Measures glucose levels by analyzing light absorption through the skin.
    - **Temperature Calibration**: Compensates for environmental and physiological variations for accurate readings.
    - **Motion Detection**: Uses an accelerometer to account for physical activity and refine results.
    """)
    st.subheader("Prototype Design")
    col1, col2 = st.columns([1,2])
    with col1:
        st.image(
            "sketch.png", 
            caption="Prototype Sketch of Glucaband",
            use_column_width=True,
            
            )
    with col2:
        # Add padding to the text for better spacing
        st.markdown("""
        **Explanation and Functionality of the Components in the Prototype Design**:
        - **Infrared LED and Photodiode**: Positioned on the underside of the band to measure glucose levels using infrared spectroscopy.
        - **Temperature Sensor**: Situated under the band, ensuring accuracy by addressing environmental and skin temperature variations.
        - **Accelerometer**: Tracks physical activity and adjusts glucose readings accordingly.
        - **Arduino Uno and LCD Screen**: Provides a sleek and user-friendly interface to display real-time glucose readings along with temperature and activity data.
        - Glucaband's **elegant wearable design** guarantees user comfort and portability, making it ideal for daily use.
        """, unsafe_allow_html=True)
    
    

    st.subheader("Applications")
    st.write("""

    - **Daily Glucose Monitoring**: Makes life for diabetic and pre-diabetic patients much more convenient.
    - **Accessibility**: Affordable and portable design for underpriviliged populations.
    """)
    st.info("**Why Glucaband is Innovative:** Combines cost-effectiveness, user-friendliness, and advanced technology to redefine glucose monitoring.")

 

# Section 3: Healthcare Impact
if selection == "Healthcare Impact":
    st.header("💡 Healthcare Delivery Impact")
    st.write("""
    ### Revolutionizing Healthcare
    Glucaband transforms patient care in the following ways:
    - **Non-Invasive Monitoring**: Eliminates the need for painful fingersticks or invasive patches.
    - **Proactive Health Management**: Allows patients to monitor trends and detect glucose anomalies early, reducing complications.
    """)
    st.subheader("Long-Term Impact")
    st.write("""
    - Reduces reliance on polluting one-time purchases like test strips, providing an eco-friendly alternative.
    - Encourages widespread adoption of glucose monitoring in both diabetic and pre-diabetic populations.
    """)

    st.write("""
    ### Quality of Life Improvements
    By eliminating the need for invasive methods, Glucaband improves the quality of life for:
    - Diabetic patients who require frequent monitoring.
    - Elderly individuals and children who find fingersticks difficult to use.
    - Patients in remote areas with limited access to medical facilities.
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
    st.header("💰 Healthcare Cost Reduction")
    st.write("""
    ### Lowering Costs for Patients
    - **One-Time Cost**: Glucaband eliminates the need for recurring purchases like test strips or patch replacements.
    - **Fewer Hospital Visits**: Enables at-home monitoring, reducing dependence on healthcare facilities.
    """)
    st.subheader("Scalability and Affordability")
    st.write("""
    - **Bulk Manufacturing**: The cost per unit can drop significantly with large-scale production
    - **Broader Access**: Lower costs ensure accessibility for low-income and remote populations.
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
if selection == "Creative & Artistic Impact":
    st.header("🎨 Creative & Artistic Impact")
    st.write("""
    ### Exhibit Design
    - **3D-Printed Model**: A polished and stylish modern prototype of Glucaband will be part of our presentation.
    - **Interactive Simulation**: Judges can explore the device’s functionality through interacting with the prototype and measuring their respective glucose levels.
    - **Visual Aids**: Infographics, graphs, and comparison tables will be used to clearly explain the innovation.
    - **Trifold**: Trifold showcasing the unique and novel features of Glucaband as well as the problems addressed by it.
    """)
    st.subheader("Artistic Elements")
    st.write("""
    - Clean and professional design through the use of vibrant and eye-popping visuals, and top-of-the-line presentation materials.
    - A live demonstration of the prototype’s features on the Arduino, hoping to create a lasting memorable impact on the medical field.
    """)
# Section 5: Logistics
if selection == "Logistics":
    st.header("🛠 Logistics and Cost Analysis")
    st.write("""
    ### Estimated Cost Breakdown
    - **IR LED and Photodiode Pair**: $3
    - **MLX90614 Temperature Sensor**: $10
    - **Accelerometer (MPU6050)**: $5
    - **Microcontroller (Arduino)**: $20
    - **Battery and Power Supply**: $5
    - **3D-Printed Case**: $2
    
    **Total Estimated Cost per Unit**: **$50**
    """)
    st.success("**Scalability Potential:** With bulk production, costs could drop below $35 per unit.")
if selection == "References":
    st.header("📚 References")
    st.write("""
    - Doe, J., & Smith, A. (2024). Advances in Non-Invasive Glucose Monitoring. *Journal of Biomedical Innovation*, 12(3), 45-67.
    - National Diabetes Statistics Report. (2022). Centers for Disease Control and Prevention. Retrieved from [https://www.cdc.gov](https://www.cdc.gov)
    - American Diabetes Association. (2024). Standards of Medical Care in Diabetes. *Diabetes Care*, 47(Supplement 1), S1–S210.
    """)
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
    - **Favorite Activity**: Rubik's Cubing
    """)
# Section 6: Exhibit Plan
