import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

# Set up the page
st.set_page_config(
    page_title="My Journey",
    page_icon=":star2:",
    layout="wide"
)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "About Me", "Portfolio"])

# Function to display the home page
def home_page():
    st.title("Crafting My Path: A Personal and Professional Showcase")
    
    # Display the header image using the provided file path
    header_image_path = "images/header.jpeg"
    header_image = Image.open(header_image_path)
    st.image(header_image, use_column_width=True)
    
    st.write(
        """
        Hello! I am Carmelyn Nime Tse Gerali, a highly motivated, passionate, and dedicated student with hands-on experience in technical support, 
        specializing in financial software. Successfully promoted to Subject Matter Expert (SME Operations) due to demonstrated expertise, leadership skills, 
        and ability to drive customer satisfaction. Seeking opportunities to leverage technical and analytical skills in a dynamic and challenging environment. 
        Explore my portfolio to see my work, learn more about me, or get in touch.
        """
    )
    
    # Include a video (replace the link with your video URL)
    st.video("https://www.youtube.com/watch?v=UG22q7yO6ms")
    st.write(
        """
        The video above is me having an orange hair, and together with my dance group members. While being busy getting my profession, 
        I made sure to have a work-life balance. Dancing has always been my way of escape from feeling stress, drained or bored. 
        This helps me to enjoy and live life everyday.
        """
    )

    # Display key metrics in a single row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Projects Completed", value="8+")

    with col2:
        st.metric(label="Years of Work Experience", value="3+")

    with col3:
        st.metric(label="Certifications", value="5+")

    # Add a button to download a resume (replace with your actual file)
    with open("Gerali_Resume.pdf", "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="Gerali_Resume.pdf",
            mime="application/pdf"
        )


# Function to display the "About Me" page
def about_me_page():
    st.title("About Me")

    st.subheader("Biography")
    st.write(
        """
        Hello, I'm Carmelyn Nime Tse Gerali, and I am deeply committed to achieving a harmonious work-life balance while pursuing my passion for technology and personal interests. Currently, I am studying Information Technology, a field that fuels my curiosity and passion for solving complex problems through innovative technology.

        Professionally, I work as a Subject Matter Expert (SME) in a financial software account within a BPO company. My role involves not only understanding and managing intricate financial software but also ensuring that our clients receive the highest level of support and expertise. My journey in this field has been marked by a dedication to excellence and a drive to continually enhance the customer experience.

        Despite the demands of my professional life, I never lose sight of my passion for dancing. Dancing has always been more than just a hobby for me; it's a vital part of my life that helps me manage stress and maintain a sense of joy and creativity. Whether it's performing on stage or simply dancing for fun, it remains a cherished part of who I am.

        At the heart of my life is my family. I take great pride in supporting and nurturing my loved ones, and I believe that helping and giving life to my family is one of my most important roles. Their well-being and happiness are a central focus in my life, and I strive to balance my professional achievements with meaningful family moments.

        In summary, I am dedicated to my career and personal growth while ensuring that I maintain a healthy balance between work, passion, and family life. My journey has been both rewarding and challenging, it is a testament to the importance of pursuing one’s passions, excelling in one’s career, and cherishing the bonds with loved ones.
        """
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("photo9.jpg")
    with col2:
        st.image("photo5.jpg")
    
    st.subheader("Skills")
    st.write(
        """
        - **Programming Languages:** C, PHP, Python, JavaScript and SQL
        - **Technologies:** Data Analysis, Machine Learning and Advanced utilization of QuickBooks
        - **Tools:** Github, Visual Studio Code, Eclipse, Netbeans, Scrapy, TensorFlow, Keras and Streamlit
        """
    )
    
    # Add a slider to show years of experience
    years_experience = st.slider("Years of Work Experience:", 1, 10, 3)
    st.write("You have", years_experience, "years of experience.")

    # Add an expander for hobbies
    with st.expander("My Hobbies"):
        st.write("In my free time, I enjoy:")
        st.write("- Dancing")
        st.write("- Play outdoor activities")
        st.write("- Strolling with loved ones")
        st.write("- Watching Korean dramas")
        st.write("- Playing chess")
        st.write("- Binge watching to movies and series")

# Function to display the portfolio page
def portfolio_page():
    st.title("Portfolio")
    
    # Portfolio Grid
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Project 1: Shape Track")
        project1_image = Image.open("project3.png")
        st.image(project1_image, width=450)
        st.write(
            """
            ShapeTrack, a computer vision application that detects and recognizes shapes in images or live video streams. 
            It leverages trackbars to adjust color thresholds dynamically, allowing users to fine-tune the detection process for different environmental conditions and shapes.
            """
        )
    
    with col2:
        st.subheader("Project 2: FoodieFeedback")
        project2_image = Image.open("project2.png")
        st.image(project2_image, width=450)
        st.write(
            """
            An NLP project that analyzes the sentiment of user reviews. The tool uses natural language processing techniques to classify
            reviews as positive, negative, or neutral. This automation not only saves time but also provides businesses with actionable insights to improve their services.
            """
        )
    
    st.subheader("Project 3: TransitHub")
    project3_image = Image.open("project1.png")
    st.image(project3_image, width=900)
    st.write(
        """
        Our Capstone project TransitHub is to outline the requirements for the development of 
        the "Vehicle Distance and Duration Calculation" software. This software aims to provide 
        accurate calculations of the distance and duration of travel for vehicles engaged in delivery 
        or rental services.
        """
    )
    
    # Include a chart to visualize some data
    st.subheader("Project Stats")
    data = {
        "Project": ["FoodieFeedback", "ShapeTrack", "TransitHub"],
        "Lines of Code": [558, 370, 1500],

    }
    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("Project"))

    st.subheader("Project Repositories")
    st.write("[Freedom Wall](https://github.com/Zeldwyn/InformationManagement2.git) | [TransitHub](https://github.com/Zeldwyn/TransitHub.git) | [FoodieFeedback](https://github.com/Zeldwyn/FoodieFeedback.git) | [Parking System](https://github.com/Zeldwyn/ParkingSystem.git)" )

# Function to display the contact page
def contact_page():
    st.title("Contact Me")
    
    st.write(
        """
        I'd love to hear from you! Whether you have a question about my work or just want to say hi, feel free to reach out.
        """
    )
    
    # Social media links
    

    # Contact form
    st.subheader("Get in Touch")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        subscribe = st.checkbox("Subscribe to newsletter")
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.write(f"Thank you for your message, {name}! I'll get back to you soon.")
            if subscribe:
                st.write("You've been subscribed to the newsletter.")

# Page navigation logic
if page == "Home":
    home_page()
elif page == "About Me":
    about_me_page()
elif page == "Portfolio":
    portfolio_page()
elif page == "Contact":
    contact_page()
