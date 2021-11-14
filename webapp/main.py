import numpy as np
import pickle
import pandas as pd
import streamlit as st
import re


st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded",
)

pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)
df = pd.read_csv('car data.csv')
# st.dataframe(df)


def predict_note_authentication(presentPrice, kms_driven, owner, car_age, petrol, diesel, seller_type, transmission):
    """Let's Predict Car Price 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: presentPrice
        in: query
        type: number
        required: true
      - name: kms_driven
        in: query
        type: number
        required: true
      - name: owner
        in: query
        type: number
        required: true
      - name: car_age
        in: query
        type: number
        required: true
      - name: petrol
        in: query
        type: number
        required: true
      - name: diesel
        in: query
        type: number
        required: true
      - name: seller_type
        in: query
        type: number
        required: true
      - name: transmission
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """
    prediction = classifier.predict(
        [[presentPrice, kms_driven, owner, car_age, petrol, diesel, seller_type, transmission]])
    print(prediction)
    return prediction


def main():
    # st.title("Vehicle Price Prediction")
    html_temp = """
        <div style="background-color:#b38600;padding:10px">
        <h2 style="color:white;text-align:center;">Vehicle Price Prediction</h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.subheader('Want to know correct price of your car?')
    st.text('Then feel free to use this web-application and help yourself with the correct\nprice of your car.')

    st.text_input('Company Name ')
    st.text_input('Car Name ')

    presentPrice = st.sidebar.text_input(
        "Your Car Present Market Price (Eg : 5.59 Lakh)", "Type Here")
    kms_driven = st.sidebar.text_input(
        "Total Distance Traveled (KM)", "Type Here")
    car_age = st.sidebar.text_input(
        "How old is your car (Example : 5)", "Type Here")
    fuel_type = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel"])
    transmission = st.sidebar.selectbox(
        "Transmission", ["Manual", "Automatic"])
    if fuel_type == "Petrol":
        petrol = 1
        diesel = 0
    else:
        diesel = 1
        petrol = 0
    if transmission == "Manual":
        var = 1
    else:
        var = 0
    result = ""

    if st.button("Predict"):
        result = predict_note_authentication(
            presentPrice, kms_driven, 0, car_age, petrol, diesel, 0, var)
    st.success('The Predicted Price : {}'.format(result))
    if st.button("Contact Me"):
        st.text("Created By Faiz Imam")
        st.markdown(
            '[Github](https://github.com/Faiziimam) [Linkdin](https://www.linkedin.com/in/faiziimam/)')


if __name__ == '__main__':
    main()
