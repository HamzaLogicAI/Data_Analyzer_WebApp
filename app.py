### Importing Libraries
import warnings 
warnings.filterwarnings("ignore")
import streamlit as st
import pandas as pd

### Title & Subheader
st.set_page_config(page_title="Data Analyzer")
st.markdown("""
    <style>
        .title {
            color: #1B53A6;
            text-align: center;
            align-items: center;
            justify-content: center;
            margin-bottom: 2px;
        }
        .subheader {
            font-size: 20px;
        }       
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'><img width='64px',height='64', src='https://cdn-icons-png.freepik.com/512/5341/5341076.png?uid=R140683934&ga=GA1.1.2115474961.1709795892&'> Data Analyzer Web App</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subheader'>Decode your business's success with actionable insights...</h3>",unsafe_allow_html=True)

### Upload the Dataset
upload = st.file_uploader("Upload Your Dataset (in CSV Format)")
if upload is not None:
    data = pd.read_csv(upload)
    
### Showing the Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        view = st.radio("Select Portion of the Dataset to View", options=(None, "Head", "Tail"))
        if view == "Head":
             st.write(data.head())
        if view == "Tail":
             st.write(data.tail())

### Checking the Datatypes of each Column
if upload is not None:
    if st.checkbox("Datatype of Each Column"):
        st.text("Datatypes")
        st.write(data.dtypes)

### Finding the Shape of the Dataset
if upload is not None:
        if st.checkbox("Shape of the Dataset"):
            if st.markdown("<button class='hot-pink-button'>No. of Rows</button>", unsafe_allow_html=True):
                st.write(data.shape[0]) 
            if st.markdown("<button class='hot-pink-button'>No. of Columns</button>", unsafe_allow_html=True):    
                st.write(data.shape[1])
                
### Checking & Handling the Null Values
if upload is not None:
    if st.checkbox("Null Values in the Dataset"):
        v2 = data.isnull().any()
        if v2.any():  # Checking if any element in v2 is True
            st.warning("Dataset has some Null Values")
            null = st.selectbox("Do You want to Fill Null Values:-", ("Select One", "Yes", "No"))
            if null == "Yes":
                data = data.interpolate()
                st.success("Congratulations! Null Values have been Filled by Appropriate Values")
            if null=="No":
                st.text("Okay! No Problem")
        else:
            st.text("Congratulations! Dataset has no Null Values")
                              
### Finding the Duplicate Values in the Dataset
if upload is not None:
    if st.checkbox("Duplicates of the Dataset"):
        v3 = data.duplicated().any()
        if v3.any():
            st.warning("Dataset has some Duplicates")
            dup = st.selectbox("Do You want to Remove Duplicates:-", ("Select One", "Yes", "No"))
            if dup == "":
                st.text("Please Select One...")
            if dup == "Yes":
                data = data.drop_duplicates()
                st.success("Congratulations! Duplicates are Removed")
            if dup == "No":
                st.text("Okay! No Problem")    
        else:
             st.success("Congratulations! Dataset has no Duplicates")
            
### Getting the Overall Statistics of the Dataset            
if upload is not None:
   if st.checkbox("Summary of the Dataset"):
        st.write(data.describe())
        
### About Section
if st.button("About App"):
    st.text("Built with Streamlit")
    st.text("Thanks to Streamlit")

    

