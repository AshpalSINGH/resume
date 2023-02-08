import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu  import option_menu
st.set_page_config(page_title="My resume", page_icon=":page_facing_up:",layout="wide")

with st.sidebar:
    selected=option_menu(menu_title="Main Menu", options=["Home","Contact"],icons=["house","envelope"])

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
            st.write("With a passion for computer programming and a strong desire to become a successful data analyst, I bring a unique blend of technical aptitude and analytical thinking to any project. I have a deep understanding of programming languages such as Python , as well as experience working with csv files, several data sets and creating data-driven solutions. I am committed to continuous learning and professional development, and am always seeking out new opportunities to challenge myself and enhance my skills.")
        with c2:
            st_lottie(lottie_animation,height=300)

#-----------------contact---------------
else:
    with st.container():
        st.write("---")
        st.header("Get in touch with Me!")

        contact_form="""
        <form action="https://formsubmit.co/ashpalsingh0909@gmail.com" method="POST">
            <input type="hidden" name="_capcha" value="False" required>
            <input type="text" name="name" placeholder="Your name here" required>
            <input type="email" name="email" placeholder="Your email here" required>
            <input type="text" name="message" placeholder="Your message here" required>
            <button type="submit">Submit/button>
        </form>"""

    c1,c2=st.columns(2)
    with c1:
        st.markdown(contact_form, unsafe_allow_html=True)