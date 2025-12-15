import streamlit as st

st.title("SmartBus+")
st.write("Simple Bus Arrival Prediction Prototype")

route = st.selectbox(
    "Select Bus Route",
    ["45A", "27B", "13C", "82D"]
)

if st.button("Predict Arrival Time"):
    if route == "45A":
        time = 6
    elif route == "27B":
        time = 10
    elif route == "13C":
        time = 14
    else:
        time = 20

    st.success(f"Bus {route} will arrive in {time} minutes")

st.caption("Python-based prototype using sample data")
