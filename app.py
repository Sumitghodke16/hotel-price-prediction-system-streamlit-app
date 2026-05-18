import streamlit as st
import pandas as pd
import joblib

# ======================================
# PAGE CONFIGURATION
# ======================================

st.set_page_config(
    page_title="Hotel Price Prediction",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================
# LOAD MODEL
# ======================================

model = joblib.load("models/hotel_price_model.pkl")

model_columns = joblib.load("models/model_columns.pkl")

# ======================================
# CUSTOM CSS
# ======================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main Background */

.stApp {
    background: linear-gradient(to right, #020617, #0f172a, #1e293b);
    color: white;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: #020617;
    border-right: 3px solid #2563eb;
}

/* Sidebar Text */

section[data-testid="stSidebar"] * {
    color: #ffffff !important;
    font-size: 20px !important;
    font-weight: 700 !important;
}

/* Sidebar Navigation */

div[role="radiogroup"] label {
    background-color: #1e293b !important;
    padding: 12px !important;
    border-radius: 12px !important;
    margin-bottom: 10px !important;
    border: 2px solid #334155 !important;
}

/* Sidebar Arrow */

button[kind="header"] {
    background-color: #ffffff !important;
    border-radius: 12px !important;
    padding: 8px !important;
}

button[kind="header"] svg {
    width: 40px !important;
    height: 40px !important;
    stroke: #000000 !important;
    color: #000000 !important;
}

/* Main Title */

.main-title {
    text-align: center;
    font-size: 58px;
    font-weight: 700;
    color: #ffffff;
    margin-top: 10px;
}

/* Subtitle */

.sub-title {
    text-align: center;
    color: #f8fafc;
    font-size: 24px;
    font-weight: 500;
    margin-bottom: 40px;
}

/* Card */

.card {
    background-color: rgba(255,255,255,0.08);
    padding: 35px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0px 6px 30px rgba(0,0,0,0.5);
    margin-bottom: 25px;
}

/* Prediction Box */

.prediction-box {
    background: linear-gradient(to right, #2563eb, #0ea5e9);
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    color: white;
    font-size: 34px;
    font-weight: 700;
    margin-top: 30px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
}

/* Footer */

.footer {
    text-align: center;
    color: white;
    font-size: 18px;
    padding-top: 40px;
    padding-bottom: 10px;
}

/* Labels */

label {
    color: white !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

/* Inputs */

.stNumberInput input {
    font-size: 18px !important;
    color: black !important;
}

.stSelectbox div {
    font-size: 18px !important;
}

/* Buttons */

.stButton>button {
    background: linear-gradient(to right, #06b6d4, #2563eb);
    color: white;
    border-radius: 14px;
    border: none;
    height: 58px;
    width: 100%;
    font-size: 22px;
    font-weight: 700;
}

.stButton>button:hover {
    background: linear-gradient(to right, #0284c7, #1d4ed8);
    color: white;
}

/* General Text */

p, h1, h2, h3, h4, h5, h6, span {
    color: white !important;
}

/* About Developer */

.about-container {
    text-align: center;
    padding: 20px;
}

.about-text {
    font-size: 20px;
    line-height: 1.9;
    color: #f8fafc;
    text-align: center;
    margin-top: 20px;
}
/* Remove White Top Strip */

header {
    background-color: #020617 !important;
}

[data-testid="stHeader"] {
    background-color: #020617 !important;
}
            
            

</style>
""", unsafe_allow_html=True)

# ======================================
# HEADER
# ======================================

st.markdown(
    '<div class="main-title">🏨 Hotel Price Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Predict Total Hotel Price With GST Using AI</div>',
    unsafe_allow_html=True
)

# ======================================
# SIDEBAR
# ======================================

st.sidebar.title("📋 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Prediction",
        "Project Information",
        "About Developer"
    ]
)

# ======================================
# PREDICTION PAGE
# ======================================

if page == "Prediction":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        city = st.selectbox(
            "🌆 City",
            [
                "Agra",
                "Ahmedabad",
                "Bengaluru",
                "Chennai",
                "Goa",
                "Hyderabad",
                "Jaipur",
                "Kolkata",
                "Mumbai",
                "New Delhi"
            ]
        )

        state = st.selectbox(
            "🗺 State",
            [
                "Delhi",
                "Goa",
                "Gujarat",
                "Karnataka",
                "Maharashtra",
                "Rajasthan",
                "Tamil Nadu",
                "Telangana",
                "Uttar Pradesh",
                "West Bengal"
            ]
        )

        nights_stayed = st.slider(
            "🛏 Nights Stayed",
            1,
            10,
            3
        )

        room_rate = st.number_input(
            "💰 Room Rate",
            min_value=1000,
            max_value=50000,
            value=15000
        )

        customer_type = st.selectbox(
            "👤 Customer Type",
            [
                "Corporate",
                "Member",
                "New Guest",
                "Regular",
                "VIP"
            ]
        )

    with col2:

        hotel_category = st.selectbox(
            "🏨 Hotel Category",
            [
                "Business",
                "Luxury",
                "Resort"
            ]
        )

        booking_channel = st.selectbox(
            "📱 Booking Channel",
            [
                "Booking.com",
                "Corporate",
                "Goibibo",
                "MakeMyTrip",
                "Walk-in",
                "Website"
            ]
        )

        payment_mode = st.selectbox(
            "💳 Payment Mode",
            [
                "Cash",
                "Credit Card",
                "Debit Card",
                "Net Banking",
                "UPI"
            ]
        )

        occupancy_status = st.selectbox(
            "🏨 Occupancy Status",
            [
                "Checked-In",
                "Checked-Out",
                "Cancelled"
            ]
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # ======================================
    # PREDICTION BUTTON
    # ======================================

    if st.button("🔮 Predict Hotel Price"):

        input_data = pd.DataFrame(
            0,
            index=[0],
            columns=model_columns
        )

        # Numerical Features

        input_data['Nights_Stayed'] = nights_stayed
        input_data['Room_Rate'] = room_rate

        # Encoded Columns

        city_col = f'City_{city}'
        state_col = f'State_{state}'
        hotel_category_col = f'Hotel_Category_{hotel_category}'
        customer_col = f'Customer_Type_{customer_type}'
        booking_col = f'Booking_Channel_{booking_channel}'
        payment_col = f'Payment_Mode_{payment_mode}'

        # Activate Columns

        if city_col in input_data.columns:
            input_data[city_col] = 1

        if state_col in input_data.columns:
            input_data[state_col] = 1

        if hotel_category_col in input_data.columns:
            input_data[hotel_category_col] = 1

        if customer_col in input_data.columns:
            input_data[customer_col] = 1

        if booking_col in input_data.columns:
            input_data[booking_col] = 1

        if payment_col in input_data.columns:
            input_data[payment_col] = 1

        # Prediction

        prediction = model.predict(input_data)

        # Show Result

        st.markdown(
            f"""
            <div class="prediction-box">
            Predicted Total Price With GST <br><br>
            ₹ {prediction[0]:,.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

# ======================================
# PROJECT INFORMATION
# ======================================

elif page == "Project Information":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("📊 Project Overview")

    st.write("""
    This machine learning web application predicts hotel booking price 
    using Random Forest Regression.

    ### Features Used:
    
    - City
    - State
    - Nights Stayed
    - Room Rate
    - Customer Type
    - Booking Channel
    - Payment Mode
    - Hotel Category

    ### Technologies Used:
    
    - Python
    - Pandas
    - Scikit-learn
    - Streamlit
    - Random Forest
    - Joblib
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ======================================
# ======================================
# ABOUT DEVELOPER
# ======================================

elif page == "About Developer":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="about-container">', unsafe_allow_html=True)

    st.image(
        "Images/sumit.jpg",
        width=260
    )

    st.markdown(
        """


        <div class="about-text">

        <h2>👨‍💻 Sumit Naresh Ghodke</h2>

        My name is Sumit Naresh Ghodke, and I am based in the metro city of Pune.
        I specialize in Machine Learning, Data Analytics, and Web Development with
        strong interest in building intelligent, scalable, and data-driven solutions.

        <br>

        I work with Python, SQL, data visualization, and modern web technologies
        to develop practical applications and analytical systems. My focus is on
        solving real-world problems through AI, automation, and clean user experiences.

        <br>

        I am continuously improving my technical expertise in Machine Learning,
        Data Science, and software development while building professional projects
        that combine analytics, innovation, and modern technology.

        <br><br>

        <a href="https://www.linkedin.com/in/sumit-ghodke-a45a82205/" target="_blank" 
        style="
        color:#38bdf8;
        font-size:22px;
        font-weight:700;
        text-decoration:none;
        ">
        🔗 Connect with me on LinkedIn
        </a>

        </div>

        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)