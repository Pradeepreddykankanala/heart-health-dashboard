import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import base64

st.set_page_config(page_title="Heart Health Dashboard", layout="wide")


def set_bg_image_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .main {{
            background-color: rgba(0,0,0,0.6);
            padding: 20px;
            border-radius: 10px;
        }}

        h1, h2, h3, p {{
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


set_bg_image_local("bg.jpg")


st.title(" Heart Health Analytics Dashboard")

st.write("Upload your dataset and get instant insights about heart disease data.")


uploaded_file = st.file_uploader(" Upload CSV File", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

   
    st.subheader(" Dataset Preview")
    st.write(df.head())

  
    st.subheader(" Dataset Info")
    st.write(df.describe())


    st.subheader(" Missing Values")
    st.write(df.isnull().sum())


    if "target" in df.columns:
        st.subheader(" Heart Disease Distribution")

        fig1 = plt.figure()
        sns.countplot(x="target", data=df)
        st.pyplot(fig1)

 
    if "age" in df.columns and "target" in df.columns:
        st.subheader(" Age vs Heart Disease")

        fig2 = plt.figure()
        sns.boxplot(x="target", y="age", data=df)
        st.pyplot(fig2)


    if "chol" in df.columns and "target" in df.columns:
        st.subheader(" Cholesterol vs Heart Disease")

        fig3 = plt.figure()
        sns.boxplot(x="target", y="chol", data=df)
        st.pyplot(fig3)

  
    st.subheader(" Correlation Heatmap")

    fig4 = plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    st.pyplot(fig4)

    
    st.subheader(" Key Insights")

    st.write("✔ Higher age group may have higher heart risk")
    st.write("✔ Cholesterol levels affect heart disease risk")
    st.write("✔ Target column: 1 = Disease, 0 = No disease")

else:
    st.info("Please upload a CSV file to start analysis.")
