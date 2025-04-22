import streamlit as st

st.title("Unit Converter App")

st.markdown("### Convert length, weight, and time instantly.")
st.write("Welcome! Select a conversion type from the category.")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])


def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

if category == "Length":
    unit = st.selectbox("Select Conversion", ["Miles to Kilometers", "Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])


value = st.number_input("Enter the value to convert", min_value=0.0, step=1.0)


if st.button("Convert"):
    if not category:
        st.error("Please choose a category.")
    elif not unit:
        st.error("Please select a conversion unit.")
    elif value == 0.0:
        st.error("Please enter a value greater than 0.")
    else:
        result = convert_units(category, value, unit)
        st.success(f"The result is {result:.2f}")
