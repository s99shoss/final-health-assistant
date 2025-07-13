import streamlit as st
import requests
import json

st.set_page_config(page_title="AI Health Assistant", layout="centered")

st.title("🤖 Multimodal AI Health Assistant")
st.markdown("Ask anything about your health, nutrition, fitness, or weather!")

# ورودی کاربر
query = st.text_input("💬 Enter your query:", "")
lat = st.number_input("🌍 Latitude", value=35.7)
lon = st.number_input("🌍 Longitude", value=51.4)
user = st.text_input("👤 User ID", value="u1")
health_data = st.text_area("🩺 Optional Health Data (JSON)", placeholder='{"blood_pressure": "120/80", "pulse": 72}')

# دکمه ارسال درخواست
if st.button("Send"):
    try:
        json_payload = {
            "query": query,
            "location": {"lat": lat, "lon": lon},
            "user": user
        }
        if health_data:
            try:
                json_payload["health_data"] = json.loads(health_data)
            except:
                st.warning("⚠️ Invalid health data JSON format")

        # ارسال درخواست به API لوکال
        response = requests.post("http://127.0.0.1:8000/query/", json=json_payload)
        result = response.json()

        # نمایش پاسخ
        st.success(result["response"])
        st.markdown("**Agents used:** " + ", ".join(result["agents_used"]))
    except Exception as e:
        st.error("❌ Error: " + str(e))
