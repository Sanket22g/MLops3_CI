import streamlit as st

st.title("Square Calculator")
st.write("Enter a number to calculate its square:")
n=st.number_input("Number", value=0 )

if st.button("Calculate"):
    
    square = n ** 2
    st.write(f"The square of {n} is {square}.")

