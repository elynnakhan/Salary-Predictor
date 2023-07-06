import streamlit as st
from PIL import Image



def show_explore_page():
   # st.title("Explore Software Engineer Salaries")
    st.title(
        """
    Visualization of Stack Overflow Developer Survey 2022
    """
    )
    tab1, tab2, tab3 = st.tabs(["Chart 1", "Chart 2", "Chart 2"])

    

    
    tab1.write("""#### Number of Data from different countries""")
    image1 = Image.open('np1.png')

    tab1.image(image1, caption='Data against Country')

    
    tab2.write(
        """
    #### Mean Salary Based On Country
    """
    )
    image2 = Image.open('np2.png')

    tab2.image(image2, caption='Salary against Country')


    tab3.write(
        """
    #### Mean Salary Based On Experience
    """
    )
    
    image3 = Image.open('np3.png')

    tab3.image(image3, caption='Salary against Experience')
