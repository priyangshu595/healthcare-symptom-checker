import streamlit as st
import requests

st.title("🩺 AI Healthcare Symptom Checker")

symptoms = st.text_area("Enter your symptoms:")

if st.button("Analyze"):
    response = requests.post(
        "https://healthcare-symptom-checker-49wk.onrender.com/analyze-symptoms",
        json={"symptoms": symptoms}
    )

    st.write("Raw:", response.text)

    if response.status_code != 200:
        st.error("Backend error")
        st.stop()

    try:
        data = response.json()
    except:
        st.error("Invalid response")
        st.stop()

    if data.get("emergency"):
        st.error("⚠️ Seek immediate medical help!")

    result = data.get("data", {})

    for cond in result.get("conditions", []):
        st.subheader(cond["name"])
        st.write(cond["description"])
        st.write(f"Severity: {cond['severity']}")

    st.write("### Recommendations")
    for rec in result.get("recommendations", []):
        st.write("- " + rec)

    st.warning(result.get("disclaimer", ""))
