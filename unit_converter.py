import streamlit as st

# Set up the app title
st.title("Unit Converter")

# Select the type of conversion
conversion_type = st.selectbox("Select Conversion Type:", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    # Length conversion options
    length_units = ["Meters", "Kilometers", "Miles", "Feet"]
    from_unit = st.selectbox("From Unit:", length_units)
    to_unit = st.selectbox("To Unit:", length_units)
    value = st.number_input("Enter Value:", min_value=0.0, step=0.01)

    # Conversion logic
    length_conversion = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084
    }
    if st.button("Convert"):
        result = value * length_conversion[to_unit] / length_conversion[from_unit]
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    # Weight conversion options
    weight_units = ["Grams", "Kilograms", "Pounds", "Ounces"]
    from_unit = st.selectbox("From Unit:", weight_units)
    to_unit = st.selectbox("To Unit:", weight_units)
    value = st.number_input("Enter Value:", min_value=0.0, step=0.01)

    # Conversion logic
    weight_conversion = {
        "Grams": 1,
        "Kilograms": 0.001,
        "Pounds": 0.00220462,
        "Ounces": 0.035274
    }
    if st.button("Convert"):
        result = value * weight_conversion[to_unit] / weight_conversion[from_unit]
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    # Temperature conversion
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit:", temp_units)
    to_unit = st.selectbox("To Unit:", temp_units)
    value = st.number_input("Enter Value:", step=0.01)

    if st.button("Convert"):
        if from_unit == to_unit:
            result = value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")