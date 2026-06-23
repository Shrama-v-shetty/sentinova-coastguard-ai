import cv2
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from email_alert import send_email_alert
from weekly_report import send_weekly_report
from streamlit_geolocation import streamlit_geolocation
import datetime
import pandas as pd
import folium
from streamlit_folium import st_folium

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Dam Monitoring System", layout="wide")

model = load_model("crack_model.h5")

# ---------------- CSS (DAM THEME) ----------------
st.markdown("""
<style>

/* ---------------- GLOBAL ---------------- */
.stApp {
    background: #f7f9fb;
    font-family: 'Segoe UI', sans-serif;
}

/* ---------------- NAV BAR ---------------- */
.navbar {
    background: #2b6f9c;
    padding: 12px 20px;
    border-radius: 12px;
    color: white;
    font-weight: 800;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    font-size:25px;
    height:50px;
}

/* ---------------- TITLE ---------------- */
.hero-title {
    font-size:60px;
    font-weight: 1000;
    color: #1f3b4d;
    height:30px;
}

.hero-sub {
    font-size: 50px;
    color: #5b6b7a;
    margin-bottom: 60px;
}

/* ---------------- CARD ---------------- */
.card {
    background: #ffffff;
    padding: 22px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.07);
    border: 1px solid #e6e9ed;
    margin-bottom: 18px;
}

/* ---------------- FEATURE ---------------- */
.feature {
    background: #eef5fa;
    padding: 10px;
    border-left: 4px solid #2b6f9c;
    border-radius: 10px;
    margin-bottom: 8px;
    color: #2f3b4a;
    font-size:15px;
}

/* ---------------- BUTTONS ---------------- */
.stButton>button {
    background: #2b6f9c;
    color: white;
    border-radius: 8px;
    padding: 9px 16px;
    border: none;
    font-weight: 600;
}

.stButton>button:hover {
    background: #1f567a;
}

/* ---------------- INPUTS ---------------- */
input, textarea {
    border-radius: 8px !important;
    border: 1px solid #d0d7de !important;
}

/* ---------------- MAP ---------------- */
[data-testid="stMap"] {
    border-radius: 12px;
}

/* ---------------- ALERT ---------------- */
.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

st.markdown("""
<div class="navbar">
    <div>Dam  Crack Detection System</div>
    <div>AI-Based Crack Detection</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

if col1.button("Home"):
    st.session_state.page = "Home"
if col2.button("Detection"):
    st.session_state.page = "Detection"
if col3.button(" About"):
    st.session_state.page = "About"

# ---------------- HOME PAGE ----------------
if st.session_state.page == "Home":

    st.markdown('<p class="hero-title"> Dam Crack Detection System</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">AI-powered crack detection for infrastructure safety</p>', unsafe_allow_html=True)

   

    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.image(
            "dam image.png",
            width=600
        )

    with col2:
        st.markdown("### Features")
        st.markdown("""
        <div class='feature'> AI Crack Detection (CNN Model)</div>
        <div class='feature'> Severity Analysis System</div>
        <div class='feature'> GPS + Manual Location Tracking</div>
        <div class='feature'> Instant Emergency Alerts</div>
        <div class='feature'> Weekly Report Generation</div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DETECTION PAGE ----------------
elif st.session_state.page == "Detection":

    st.markdown('<p class="hero-title">🔍 Crack Detection Dashboard</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        dam_name = st.text_input("Dam Name")
        user_email = st.text_input("Email")

    with col2:
        address = st.text_input("Location")

    maps_link = ""
    if address:
        maps_link = f"https://www.google.com/maps/search/{address.replace(' ', '+')}"
        st.markdown(f"📍 Open Map: [Click Here]({maps_link})")

    # ----------- LAT/LONG INPUT (NEW) -----------
    st.subheader("📍 Enter Exact Coordinates (from Google Maps)")

    coords = st.text_input("Enter Coordinates (lat, lon)")

    manual_latlon_link = ""

    if coords:
        try:
            lat, lon = map(float, coords.split(","))

            st.success(f"Exact Location: {lat}, {lon}")

            df = pd.DataFrame({'lat': [lat], 'lon': [lon]})
            st.map(df)

            manual_latlon_link = f"https://www.google.com/maps?q={lat},{lon}"

        except:
            st.error("Invalid format. Use: 12.9716, 77.5946")

    # ----------- MAP CLICK (NEW) -----------
    st.subheader("📍 Or Select Location from Map")

    m = folium.Map(location=[12.97, 77.59], zoom_start=10)
    map_data = st_folium(m, height=400, width=700)

    selected_location = ""

    if map_data and map_data["last_clicked"]:
        lat = map_data["last_clicked"]["lat"]
        lon = map_data["last_clicked"]["lng"]

        st.success(f"Selected Location: {lat}, {lon}")

        selected_location = f"https://www.google.com/maps?q={lat},{lon}"

    # ----------- LIVE LOCATION -----------
    

        if location and location["latitude"] and location["longitude"]:
            lat = location["latitude"]
            lon = location["longitude"]

            live_maps_link = f"https://www.google.com/maps?q={lat},{lon}"
            st.success("📍 Location Captured")

            df = pd.DataFrame({'lat': [lat], 'lon': [lon]})
            st.map(df)

    st.markdown('</div>', unsafe_allow_html=True)

    # ----------- FINAL LOCATION LOGIC (UPDATED) -----------
    if manual_latlon_link:
        final_location = manual_latlon_link
    elif selected_location:
        final_location = selected_location
    elif maps_link:
        final_location = maps_link
    else:
        final_location = "Location not provided"

    # ---------------- UPLOAD ----------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📤 Upload Dam Image")

    uploaded_file = st.file_uploader("Choose Image")

    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        image_path = "temp.jpg"
        cv2.imwrite(image_path, img)

        col1, col2 = st.columns(2)

        with col1:
            st.image(img, caption="Original Image", width="stretch")

        resized = cv2.resize(img, (128, 128)) / 255.0
        resized = np.expand_dims(resized, axis=0)

        prediction = model.predict(resized)[0][0]

        if prediction < 0.2:
            st.error("Invalid concret Image")
            st.stop()

        if prediction > 0.5:
            st.error("🚨 Crack Detected")

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150)

            highlight = img.copy()
            highlight[edges > 0] = [0, 0, 255]

            with col2:
                st.image(highlight, caption="Detected Crack", width="stretch")

            severity = np.sum(edges > 0)

            level = "LOW" if severity < 1000 else "MEDIUM" if severity < 3000 else "HIGH"

            st.markdown(f"### ⚠ Severity: **{level}**")

            if level in ["LOW", "MEDIUM"]:
                with open("reports.txt", "a") as f:
                    f.write(f"{datetime.datetime.now()} | {dam_name} | {level} | {final_location}\n")

            if level == "HIGH":
                send_email_alert(
    dam_name,
    level,
    user_email,
    address,
    final_location,
    image_path,
    lat=lat if 'lat' in locals() else None,
    lon=lon if 'lon' in locals() else None,
    selected_location=selected_location if 'selected_location' in locals() else None
)
                st.success("🚨 Alert Sent")

        else:
            st.success("✅ No Crack Detected")

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- REPORT ----------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Weekly Report")

    if st.button("Send Weekly Report"):
        send_weekly_report()
        st.success("Report Sent!")

    st.markdown('</div>', unsafe_allow_html=True)

   

# ---------------- ABOUT PAGE ----------------
elif st.session_state.page == "About":

    st.markdown('<p class="hero-title"> About System</p>', unsafe_allow_html=True)


    st.write("""
    AI-based Concrete Monitoring System using CNN for crack detection.

    ✔ Image-based crack detection  
    ✔ Severity classification  
    ✔ Emergency alerts via email  
    ✔ GPS-based location tracking  
    ✔ Weekly automated reports  

    Built for infrastructure safety and disaster prevention.
    """)

    st.markdown("</div>", unsafe_allow_html=True)