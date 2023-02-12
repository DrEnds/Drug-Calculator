#---Dose calculator web app

import streamlit as st

#Default page setup
st.set_page_config(page_title='Drug calculator', page_icon="💊")

#title of an app
st.title("Veterinary Drug 💊 Calculator")
st.info("Only valid if the drug is in solution.",icon="⚠️")

#formula to calculate dose
def calculate(wt, ds, fm):
    x = round((wt*ds)/fm,3)
    y = round(wt*ds)
    st.subheader(f"{x} ml")
    st.text(f"Amount {y} mg")

#setting up two columns
col1,col2 = st.columns([4,2])

with col1:
    #setting up variables using streamlit input functions
    weight = st.number_input("Enter the animal's weight",value=15)
    dose = st.number_input("Enter the necessary Dose per weight",value=1)
    formulation = st.number_input("Enter the drug Formulation",value=20)

with col2:
    #setting up the units
    weight_unit = st.selectbox('Choose on the weight unit',('kg', 'lbs', 'gm'), index=0)
    dose_unit = st.selectbox('Choose the dose unit',('µg', 'mg', 'gm'), index=1)
    formulation_unit = st.selectbox('Choose the formulation unit',('mg/ml', 'gm/ml'),index=0)

#convert every unit to kilograms
if weight_unit == "lbs":
    weight = weight * 0.454
elif weight_unit == "gm":
    weight = weight/1000
else:
    weight = weight

#convert every unit to miligrams
if dose_unit == "µg":
    dose = dose/1000
elif dose_unit == "gm":
    dose = dose * 1000

#convert every unit to miligrams per mililiter
if formulation_unit == "gm/ml":
    formulation = formulation * 1000


#button pressed, calls the calculate function
if st.button("Calculate"):
    st.subheader("Amount")
    calculate(weight,dose,formulation)

expander = st.expander("How it's done ?", expanded=False)

with expander:
    st.latex(r'''
    required_{ml} = 
    \left(\frac{weight*dose}{formulation}\right)
    ''')
    st.write("Weight = You can weigh an animal using a scale or the heart-girth technique.")
    st.write("Dose = You must be aware of the dosage of medication necessary for the animal.")
    st.write("Formulation = Drug formulation as specified by the manufacturer. To find it, look at the labels or other sources.")

st.markdown("---")    
st.text("Created by DrEnds")
