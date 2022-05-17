import streamlit as st
import time

if __name__ == "__main__":
    st.title("This is a test Return Calculator")
    p = st.number_input("I want to invest (in INR)", min_value=1000, step=500)
    f = st.radio("I want to do it",("One time","Monthly"))
    r = st.number_input("Yearly Interest Rate", min_value=0.5, step=0.1)
    t = st.slider("I want to invest for (in years)", min_value=1,max_value=10)
    if st.button("Calculate"):
        if f == "Monthly":
            p = p*12
        with st.spinner('computing ...'):
            time.sleep(1)
            st.write(f"You will get INR {round(p*(1+r/100)**t,3)} in total")
