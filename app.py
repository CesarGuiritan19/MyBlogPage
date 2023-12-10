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
img_project1 = Image.open("images/workout.jpg")
img_project2= Image.open("images/every.jpg")
img_project3 = Image.open("images/gym.jpg")
img_project4 = Image.open("images/bench.jpg")
img_lottie_animation = Image.open("images/webpageImage2.png")

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
            st.title("Welcome to my Webpage")
            st.subheader("Hi :wave:, I am Cesar U. Guiritan")
            st.write("I am a Computer Engineering students from SNSU")
            st.write("To know my projects visit my github link below.")
            st.write("[Github Link Here](https://github.com/CesarGuiritan/MY-WEBPAGE/tree/main/python)")
        with column_right:
            pass

# --- Projects Section ---
elif tabs == 'Project':
    with st.container():
        st.write("---")
        st.header("My Project")
        st.write("##")
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            # insert image
            st.image(img_project1)
            st.image(img_project2)
            st.image(img_project3)
            st.image(img_project4)
        
        with text_column:
            st.subheader("Project Body")
            st.write(
                """ 
                Physical Benefits:
                Weight Management: Exercise helps in maintaining a healthy weight or achieving weight loss by burning calories and improving metabolism.

                Cardiovascular Health: Regular exercise strengthens the heart, lowers blood pressure, and improves overall cardiovascular health.

                Muscle Strength and Endurance: Physical activity helps build and maintain muscle mass, enhancing strength and endurance.

                Bone Health: Weight-bearing exercises contribute to bone density, reducing the risk of osteoporosis and fractures.

                Improved Flexibility: Stretching and flexibility exercises enhance joint range of motion and reduce the risk of injuries.

                Enhanced Immune System: Regular exercise can boost the immune system, making the body more resilient to illnesses. 
                """
                """ 
                Mental and Emotional Benefits:
                Stress Reduction: Exercise triggers the release of endorphins, which are natural mood lifters, reducing stress and anxiety.

                Improved Sleep: Regular physical activity can contribute to better sleep quality and duration.

                Increased Energy Levels: Exercise increases energy levels and reduces feelings of fatigue.

                Enhanced Cognitive Function: Physical activity is linked to improved concentration, memory, and overall cognitive function.

                Mood Regulation: Exercise can help alleviate symptoms of depression and anxiety, promoting a positive mood.
                """
                """
                Long-Term Health Benefits:
                Disease Prevention: Regular exercise is associated with a lower risk of chronic diseases such as heart disease, diabetes, and certain types of cancer.

                Improved Longevity: Leading an active lifestyle is linked to a longer and healthier life.

                Social Benefits:
                Community and Social Interaction: Group exercises or team sports provide opportunities for social interaction, fostering a sense of community.

                Self-Esteem and Confidence: Achieving fitness goals can boost self-esteem and confidence.
                """
            )
            st.markdown("[Github Link](https://github.com/CesarGuiritan/MY-WEBPAGE/tree/main/python)")
    with st.container():
        image_column, text_column = st.columns((1,2)) # (image_column size, text_column size)
        with image_column:
            st.image(img_lottie_animation)
            # insert image
        with text_column:
            st.subheader("How to add a contact form in your Streamit App")
            st.write(
                """
                Want to add a contact form to your streamlit website.
                In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service 'Form Submit'.
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
                Journey through Code: Get to know Cesar Guritan

                Introduction:
                Cesar, a passionate and ambitious computer engineering student, embarked on a remarkable journey through the realm of technology with a determination to master programming languages such as Python, Java, and beyond. Born on February 12,2004, Cesar exhibited an early interest in computers and technology that would shape the trajectory of their life.

                Early Years:
                Growing up in Antao Surigao Del Sur, Cesardiscovered a fascination for the intricate world of computers at a young age. From taking apart gadgets to exploring basic programming concepts, it was evident that a future in computer engineering awaited. The supportive environment provided by My family encouraged Cesar to pursue their dreams in the field of technology.

                Academic Pursuits:
                As Cesar transitioned into higher education, they decided to pursue a degree in computer engineering at [Your University]. The academic journey proved to be both challenging and rewarding, as Cesardelved into courses ranging from digital systems design to algorithms and data structures. The foundational knowledge gained during this period laid the groundwork for a deeper understanding of computer science.

                Passion for Programming:
                Fueling Cesar's enthusiasm for technology was an insatiable appetite for programming languages. Python, with its simplicity and versatility, became an early love. Cesarrecognized the importance of Java in the software development landscape, and with determination, they set out to master its intricacies. Beyond these languages, Cesar embraced a curiosity-driven approach, exploring new languages and frameworks to broaden their skill set.

                Extracurricular Activities:
                Outside the classroom, Cesar engaged in various extracurricular activities to complement their academic endeavors. Participating in coding competitions, hackathons, and collaborative projects, Cesar honed their problem-solving skills and gained practical experience. These experiences not only enriched Cesar's knowledge but also forged lasting connections within the tech community.

                Internships and Industry Exposure:
                To further bridge the gap between academia and industry, Cesar sought internships and practical experiences. Working at [Your Previous Internship Company], Cesar gained valuable insights into real-world software development, applying theoretical concepts to solve practical challenges. These experiences solidified Cesar's commitment to pursuing a career at the intersection of computer engineering and programming.

                Future Aspirations:
                As Cesar continues their academic journey and explores the ever-evolving landscape of technology, the future holds exciting possibilities. Cesar envisions contributing to cutting-edge projects, perhaps in artificial intelligence, cybersecurity, or software development. The unwavering commitment to continuous learning ensures that Cesar remains at the forefront of technological advancements.

                Conclusion:
                The biography of Cesar reflects a compelling narrative of passion, perseverance, and a relentless pursuit of knowledge in the field of computer engineering. As Cesarcontinues to evolve as a tech enthusiast, the story unfolds, promising an inspiring journey through code with many more chapters yet to be written.
                .
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
        <form action="https://formsubmit.co/cesarguiritan134@gmail.com" method="POST">
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