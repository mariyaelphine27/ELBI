import streamlit as st

st.title("BSc Career Recommendation System")

course = st.text_input("Enter your course")
skills_input = st.text_input("Enter your skills (comma separated)")
interest = st.text_input("Enter your interest")
percentage = st.text_input("Enter your percentage")

career_data = {

"computer science":{
"jobs":[
("Software Developer","₹4L-₹10L"),
("Web Developer","₹3L-₹8L"),
("Data Analyst","₹4L-₹9L"),
("System Administrator","₹3L-₹7L")
],
"skills":["python","java","sql","data structures"],
"books":["Python Crash Course","Clean Code"]
},

"data science":{
"jobs":[
("Data Scientist","₹6L-₹15L"),
("Machine Learning Engineer","₹8L-₹18L"),
("AI Engineer","₹7L-₹16L")
],
"skills":["python","machine learning","statistics"],
"books":["Hands-On Machine Learning","Python for Data Analysis"]
}

}

private_jobs = [
("HR Executive","₹3L-₹7L"),
("Marketing Executive","₹3L-₹8L"),
("Digital Marketing Executive","₹4L-₹10L")
]

government_jobs = [
("UPSC Officer","₹10L-₹20L"),
("SSC Officer","₹5L-₹10L"),
("Bank PO","₹6L-₹12L"),
("TNPSC Officer","₹6L-₹11L")
]

if st.button("Get Career Recommendation"):

    user_skills = [s.strip() for s in skills_input.lower().split(",")]
    found=False

    for key in career_data:

        if key in course.lower():

            data = career_data[key]

            st.subheader("Recommended Jobs")
            for job,salary in data["jobs"]:
                st.write(job,"-",salary)

            st.subheader("Missing Skills")
            for skill in data["skills"]:
                if skill not in user_skills:
                    st.write(skill)

            st.subheader("Book Recommendations")
            for book in data["books"]:
                st.write(book)

            found=True
            break

    if not found:
        st.write("Course not found. Showing general jobs.")

    st.subheader("Private Jobs")
    for job,salary in private_jobs:
        st.write(job,"-",salary)

    st.subheader("Government Jobs")
    for job,salary in government_jobs:
        st.write(job,"-",salary)