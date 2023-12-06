import streamlit as st


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- Header ----
with st. container():
    st.title("Vincent's Weblog")
    st.write("Hi, I'm Vincent I. Pingol 18 years old a first year college of Surigao del Norte State University (SNSU) with a program Bachelor of Science in Computer Engineering. I am the middle child in my family, I always get what I want whenever I asked my parents about it. And I lived in Brgy. Bonifacio Purok-3 Surigao City.")

    st.image("dexiee.jpg", caption="Enjoy your life, do crazy stuft, try to be positive & smile.")
    st.write("Embarking on University career is a daunting adventure as well as a learning curve of one's life. However, there are several erratic dapples in the first year journey of University. Even the most prepared students find it difficult to cope up with the surprising challenges of the life at University. College life is changing for nearly every student. From meal plans and roommates to study abroad and college finances. College life can be difficult thing to get used to and handle. There will be a lot of time where you doubt yourself and your decision. A lot of student became overwhelm by the requirement of college, the change that took place too fast.")     
    st.write("The most frequent complaint heard from college students is that  their professors are out to fail them and ruin their chance at getting a career. But, what they need to understand is that the professors job is not to force you to do your work, they will not follow you home to make a sure that you do what you have to in order to pass the class. Responsible, that seem to be the thing a lot of freshmen students seem to lack.")    
    st.write("As a first year college of this University, Surigao del Norte State University (SNSU) S.Y 2023-2024 I would like to give advice or tips for incoming college freshmen next S.Y. First is STUDY WHAT YOU (ACTUALLY) LOVE. Second is KEEP AN OPEN MIND. Third is USE A PLANNER AND WRITE DOWN ALL OF YOUR ASSIGNMENTS AND TESTS FOR EACH CLASS FOR THE SEMESTER DURING SYLLABUS WEEK. Fourth is CONSIDER ALL POTENTIAL OPTIONS FOR YOUR MAJOR. Lastly, REMEMBER... EVERYONE IS IN THE SAME BOAT WHEN IT COMES TO FRIENDS, EVERYONE IS LOOKING TO MAKE THEM SO RELAX A BIT AND BE YOURSELF.")

    # ---- Contact ----
with st.container():
    st.write("---") 
    st.header("Get In Touch With Me!") 
    st.write("##")

# Documentation: https://formsubmit.com/!!!Change email Address!!!
    contact_form = """  
        <form_action = "https://formsubmit.com/your_@email.com", method="POST">
            <input type="hidden" name="captcha" value="false">
            <input type="text" name="name" required>
            <input type="email" name="email" required>
            <button type="Submit">Send</button>
        </form>
        """
    left_column, right_column = st.columns(2)   
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

        st.markdown("https://www.facebook.com/vincent.pingol.1048")
        