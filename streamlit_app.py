import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Vegan Hipster Coffee Orders", page_icon="☕", layout="centered")

# Custom CSS for background and container styling
custom_css = """
<style>
html, body {
    height: 100%;
    margin: 0;
}
body {
    background: linear-gradient(to bottom right, #f7e4d6, #e4cfc3);
}
.stApp {
    background-color: rgba(255,255,255,0.8);
    backdrop-filter: blur(4px);
    border-radius: 10px;
    padding: 2rem;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.title("Vegan Hipster Coffee")
st.write("Place your order using the form below.")

# Initialize session state for storing orders
if "orders" not in st.session_state:
    st.session_state["orders"] = []

# Order form
with st.form(key="order_form", clear_on_submit=True):
    name = st.text_input("Name")
    coffee = st.selectbox("Coffee type", ["Espresso", "Americano", "Latte", "Cappuccino", "Flat White", "Mocha", "Long Black"])
    milk = st.selectbox("Milk option", ["Dairy", "Soy", "Almond", "Oat", "Coconut"])
    notes = st.text_area("Additional notes (optional)")
    submit_button = st.form_submit_button(label="Place Order")

    if submit_button:
        if name:
            order = {
                "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": name,
                "Coffee": coffee,
                "Milk": milk,
                "Notes": notes,
            }
            st.session_state["orders"].append(order)
            st.success(f"Order for {name} added!")
        else:
            st.error("Please enter your name.")

# Display orders
if st.session_state["orders"]:
    st.subheader("Orders")
    st.table(st.session_state["orders"])
else:
    st.info("No orders yet. Fill in the form to add a new order.")
