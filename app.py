from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local Css

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style/style.css")

# --- Load Assets ---
lottie_coding = load_lottieurl("https://lottie.host/ccd351fa-6625-4172-9082-8133922133d6/V9YuUtgXl2.json")
lottie_email = load_lottieurl("https://lottie.host/cf262121-a926-4935-b875-de2f0c5e1443/egpAV4JoPj.json")
img_project1 = Image.open("images/software.jpg")
img_project2 = Image.open("images/hardware.jpg")

# --- Side Bar Section ---
with st.sidebar:
        tabs = on_hover_tabs(tabName=['Home', 'Project' ,'About', 'Feedback'], 
                             iconName=['home', 'link', 'info', 'mail'],
                             styles = {'navtab': {'background-color':'#1e7aea',
                                                  'color': '#fcfcfc',
                                                  'font-size': '18px',
                                                  'transition': '1s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'
                                                  },
                                       'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}
                                                          },
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'
                                                   },
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'
                                                    }
                                        },
                             key="1" ,default_choice=0)

# --- Home Section ---
if tabs =='Home':
    with st.container():
        column_left, column_right = st.columns((2,1))
        with column_left:
            st.write("---")
            st.title("Engineering Student in SNSU.")
            st.subheader("Hi :wave:, I am Shan Wine Sanchez.")
            st.write("In theory, theory and practice are the same. In practice, they are not.")
            st.write("Creativity is what we speak, Vision for better building, Simplify Engineering.")
            st.write("Turning ideas into reality, Innovation for life, Make dreams for life,  Make it happen.")
            st.write("Innovation that works, Making it easy for you, Solution for all.")
            st.write("Be alone, that is the secret of invention; be alone, that is when ideas are born.")
            st.write("[click my link](https://github.com/Shanwine13/shan13)")
        with column_right:
            pass

# --- Projects Section ---
elif tabs == 'Project':
    with st.container():
        st.write("---")
        st.header("Property of Shan Wine")
        st.write("##")
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            # insert image
            st.image(img_project1)
        with text_column:
            st.subheader("World of Software's")
            st.write(
                """ 
                Software is a great combination between artistry and engineering. 
                """
                """ 
                Controlling complexity is the essence of computer programming. 
                """
                """
                Programming is the art of telling another human being what one wants the computer to do. 
                """
                """"""
            )
            st.markdown("[click my link](https://github.com/Shanwine13/shan13)")
    with st.container():
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            st.image(img_project2) # insert image
        with text_column:
            st.subheader("World of Hardware's")
            st.write(
                """
                Never before in the history of mankind has the pace of innovation and technological acceleration been faster than its today.
                """
            )
            st.markdown("[Watch Here](https://youtu.be/FOULV9Xij_8)")

# --- About Section ---
elif tabs == 'About':
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((2,1))
        with left_column:
            st.header("About Me")
            st.write("##")
            st.write("""
                I am a computer engineering student in Surigao del Norte State University.
                - I am currently studying Python, Java, Html and Css.
                - All of my projects will success.
                - My project is finally finish.
            """)
            st.write("For the meantime you can watch this youtube video to learn more about how to make a webpage!")
            st.write("[Youtube](https://youtube.com/c/CodingIsFun)")
        with right_column:
            st_lottie(lottie_coding, height=500, key="coding")

# --- Feedback form Section ---
elif tabs == 'Feedback':
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Get in touch with me!")
        st.write("##")
        contact_form = """
        <form action="https://formsubmit.co/sanchezshanwine9@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_email, height=200, key="email")
