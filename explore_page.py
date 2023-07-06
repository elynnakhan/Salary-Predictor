import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearlyYearly"]]
    df = df.rename({"ConvertedCompYearlyYearly": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)
    country_map = shorten_categories(df.Country.value_counts(), 500)
    df['Country'] = df['Country'].map(country_map)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df['Country'] != 'Other']
    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    df['EdLevel'] = df['EdLevel'].apply(clean_education)

    
    return df

df = load_data()

def show_explore_page():
   # st.title("Explore Software Engineer Salaries")
    st.title(
        """
    Visualization of Stack Overflow Developer Survey 2022
    """
    )
    tab1, tab2, tab3 = st.tabs(["Chart 1", "Chart 2", "Chart 2"])

    

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    explode = (0.1, 0.1, 0.1, 0.1, 0.1 ,0.1 ,0.1 ,0.1 ,0.2 ,0.3 ,0.3 ,0.3 ,0.3)
    labels='USA','India','UK','Germany','Canada','Brazil','France','Spain','Australia','Netherlands','Poland','Italy','Sweden'

    ax1.pie(data, labels=labels,explode=explode, autopct="", shadow=False, startangle=90, labeldistance=2, radius=1)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    
    tab1.write("""#### Number of Data from different countries""")

    tab1.pyplot(fig1)
    
    tab2.write(
        """
    #### Mean Salary Based On Country
    """
    )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    tab2.line_chart(data)

    tab3.write(
        """
    #### Mean Salary Based On Experience
    """
    )

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    tab3.line_chart(data)
