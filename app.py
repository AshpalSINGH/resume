import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu  import option_menu
from PIL import Image
st.set_page_config(page_title="My resume", page_icon=":page_facing_up:",layout="wide")

with st.sidebar:
    selected=option_menu(menu_title="main menu", options=["Home","About Me","Contact"],icons=["house","person","envelope"])

def load_lottie(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#------load asserts----
# https://www.webfx.com/tools/emoji-cheat-sheet
lottie_animation=load_lottie("https://assets6.lottiefiles.com/packages/lf20_49rdyysj.json")

#--------------Header section-----------------
if selected=="Home":
    with st.container():
        st.subheader("Hi, I am Ashpal :wave:")
        st.title("An aspiring data analyst")


    with st.container():
        st.write("---")
        c1,c2=st.columns(2)
        with c1:
            st.header("About Me")
            st.info("With a passion for computer programming and a strong desire to become a successful data analyst, I bring a unique blend of technical aptitude and analytical thinking to any project. I have a deep understanding of programming languages such as Python , as well as experience working with csv files, several data sets and creating data-driven solutions. I am committed to continuous learning and professional development, and am always seeking out new opportunities to challenge myself and enhance my skills.")
            btn1= st.button("More about Me")
            if btn1:
                with st.container():
                    selected="About Me"


        with c2:
            st_lottie(lottie_animation,height=300)
if selected=="About Me":
    st.write("---")
    with st.container():
        c1,c2=st.columns(2)
        with c1:
            st.subheader("More About Me")
            st.write("Name: Ashpal Singh")
            st.write("Age: 19")
            st.write("Email: ashpalsingh0909@gmail.com")
            st.write("Contact No.: +61 0499195301")
            st.write("Skills: ")
        c11,c22=st.columns(2)
        with c11:
            st.info("Python")
            st.info("SQL")
            st.info("Numpy")
            st.info("Matplotlib")
            st.info("Streamlit")
            st.info("Web Scraping")

        with c22:
            st.info("Microsoft Power Bi")
            st.info("Data Analytics")
            st.info("Pandas")
            st.info("Plotly")
            st.info("HTML")
# ------------certifications----------


#-----------------contact---------------
if selected=="Contact":
    with st.container():
        st.write("---")
        st.header("Get in touch with Me!")

        contact_form="""
        <form action="https://formsubmit.co/ashpalsingh0909@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Enter your name" required>
        <input type="email" name="email" placeholder="Enter your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    c1,c2=st.columns(2)
    with c1:
        st.markdown(contact_form, unsafe_allow_html=True)
