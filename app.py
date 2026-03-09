import streamlit as st

st.set_page_config(page_title="AI Career Recommendation System", page_icon="🎓")

st.title("🎓 AI Career Recommendation System")

course = st.text_input("Enter your Course (Example: Computer Science / BA English)")
skills_input = st.text_input("Enter your Skills (comma separated)")
interest = st.text_input("Enter your Interest")
percentage = st.number_input("Enter your Percentage",0,100)

user_skills = [s.strip().lower() for s in skills_input.split(",")]

career_data = {

"computer science":{
"jobs":[("Software Developer","₹4L-₹10L"),("Data Analyst","₹4L-₹9L")],
"private_jobs":[("Full Stack Developer","₹6L-₹14L"),("App Developer","₹4L-₹10L")],
"gov_special":[("NIC Scientist","₹8L-₹15L"),("ISRO Scientist","₹10L-₹20L")],
"skills":["python","java","data structures"],
"books":["Python Crash Course","Clean Code"]
},

"information technology":{
"jobs":[("Network Engineer","₹3L-₹8L"),("System Administrator","₹3L-₹7L")],
"private_jobs":[("Cloud Engineer","₹5L-₹12L"),("IT Support Engineer","₹3L-₹6L")],
"gov_special":[("Railway IT Officer","₹6L-₹10L")],
"skills":["networking","linux","cloud"],
"books":["Networking Basics","Linux Command Line"]
},

"data science":{
"jobs":[("Data Scientist","₹6L-₹15L"),("Machine Learning Engineer","₹8L-₹18L")],
"private_jobs":[("Data Engineer","₹8L-₹16L"),("AI Developer","₹7L-₹15L")],
"gov_special":[("Government Data Analyst","₹7L-₹12L")],
"skills":["python","machine learning","statistics"],
"books":["Hands-On Machine Learning","Python for Data Analysis"]
},

"artificial intelligence":{
"jobs":[("AI Engineer","₹7L-₹16L"),("ML Engineer","₹8L-₹18L")],
"private_jobs":[("AI Developer","₹7L-₹14L"),("Deep Learning Engineer","₹8L-₹18L")],
"gov_special":[("DRDO AI Scientist","₹10L-₹18L")],
"skills":["python","deep learning","ai"],
"books":["Artificial Intelligence Basics"]
},

"cyber security":{
"jobs":[("Cyber Security Analyst","₹6L-₹15L"),("Security Engineer","₹7L-₹14L")],
"private_jobs":[("Ethical Hacker","₹8L-₹16L"),("Security Consultant","₹7L-₹15L")],
"gov_special":[("Cyber Crime Officer","₹7L-₹13L")],
"skills":["network security","ethical hacking"],
"books":["Cyber Security Essentials"]
},

"mathematics":{
"jobs":[("Statistician","₹4L-₹9L"),("Actuary","₹8L-₹20L")],
"private_jobs":[("Financial Analyst","₹5L-₹12L"),("Risk Analyst","₹6L-₹14L")],
"gov_special":[("RBI Officer","₹8L-₹15L")],
"skills":["statistics","excel"],
"books":["Practical Statistics"]
},

"statistics":{
"jobs":[("Statistician","₹4L-₹9L"),("Research Analyst","₹4L-₹9L")],
"private_jobs":[("Market Analyst","₹4L-₹8L"),("Business Analyst","₹5L-₹12L")],
"gov_special":[("Government Statistician","₹7L-₹12L")],
"skills":["statistics","data analysis"],
"books":["Statistics for Data Science"]
},

"physics":{
"jobs":[("Research Assistant","₹3L-₹6L"),("Lab Technician","₹2L-₹5L")],
"private_jobs":[("Quality Control Analyst","₹3L-₹7L"),("Technical Consultant","₹4L-₹8L")],
"gov_special":[("ISRO Scientist","₹10L-₹18L")],
"skills":["research","mathematics"],
"books":["Concepts of Physics"]
},

"chemistry":{
"jobs":[("Chemical Analyst","₹3L-₹7L"),("Production Chemist","₹4L-₹9L")],
"private_jobs":[("Pharma Analyst","₹4L-₹9L"),("Quality Control Chemist","₹4L-₹8L")],
"gov_special":[("Drug Inspector","₹8L-₹12L")],
"skills":["lab skills","analysis"],
"books":["Organic Chemistry"]
},

"biochemistry":{
"jobs":[("Biochemist","₹3L-₹8L"),("Clinical Lab Analyst","₹3L-₹7L")],
"private_jobs":[("Pharma Researcher","₹4L-₹9L"),("Clinical Analyst","₹4L-₹8L")],
"gov_special":[("Forensic Scientist","₹7L-₹11L")],
"skills":["biochemistry","lab analysis"],
"books":["Biochemistry Basics"]
},

"biotechnology":{
"jobs":[("Biotech Researcher","₹4L-₹9L"),("Clinical Research Associate","₹3L-₹8L")],
"private_jobs":[("Genetic Engineer","₹6L-₹14L"),("Biotech Analyst","₹5L-₹10L")],
"gov_special":[("ICMR Scientist","₹8L-₹14L")],
"skills":["biology","lab research"],
"books":["Biotechnology Basics"]
},

"microbiology":{
"jobs":[("Microbiologist","₹3L-₹8L"),("Food Safety Officer","₹3L-₹7L")],
"private_jobs":[("Lab Technician","₹2L-₹5L"),("Medical Lab Scientist","₹4L-₹8L")],
"gov_special":[("Food Safety Officer","₹5L-₹9L")],
"skills":["microbiology","lab techniques"],
"books":["Medical Microbiology"]
},

"botany":{
"jobs":[("Botanist","₹3L-₹7L"),("Plant Researcher","₹3L-₹6L")],
"private_jobs":[("Agriculture Consultant","₹4L-₹8L"),("Plant Scientist","₹4L-₹9L")],
"gov_special":[("Forest Officer","₹6L-₹10L")],
"skills":["plant biology","research"],
"books":["Plant Biology"]
},

"zoology":{
"jobs":[("Zoologist","₹3L-₹7L"),("Wildlife Biologist","₹4L-₹8L")],
"private_jobs":[("Animal Care Specialist","₹2L-₹5L"),("Wildlife Researcher","₹4L-₹8L")],
"gov_special":[("Wildlife Officer","₹6L-₹10L")],
"skills":["animal biology","research"],
"books":["Zoology Basics"]
},

"environmental science":{
"jobs":[("Environmental Scientist","₹4L-₹8L"),("Climate Analyst","₹5L-₹10L")],
"private_jobs":[("Sustainability Consultant","₹5L-₹11L"),("Environmental Analyst","₹4L-₹9L")],
"gov_special":[("Pollution Control Officer","₹6L-₹11L")],
"skills":["environmental analysis","research"],
"books":["Environmental Science Basics"]
},

"ba english":{
"jobs":[("Content Writer","₹3L-₹7L"),("Editor","₹4L-₹8L")],
"private_jobs":[("Copywriter","₹4L-₹9L"),("Digital Content Creator","₹3L-₹6L")],
"gov_special":[("Information Officer","₹6L-₹10L")],
"skills":["writing","communication"],
"books":["Elements of Style"]
},

"ba economics":{
"jobs":[("Economist","₹6L-₹12L"),("Policy Analyst","₹5L-₹11L")],
"private_jobs":[("Financial Analyst","₹6L-₹12L"),("Market Research Analyst","₹5L-₹10L")],
"gov_special":[("Economic Officer","₹7L-₹13L")],
"skills":["analysis","statistics"],
"books":["Economics Basics"]
},

"ba history":{
"jobs":[("Historian","₹3L-₹6L"),("Archivist","₹3L-₹7L")],
"private_jobs":[("Museum Curator","₹4L-₹8L"),("Research Writer","₹3L-₹6L")],
"gov_special":[("Archaeological Officer","₹6L-₹11L")],
"skills":["research","writing"],
"books":["World History"]
},

"ba psychology":{
"jobs":[("Psychologist","₹4L-₹8L"),("Counsellor","₹3L-₹7L")],
"private_jobs":[("HR Specialist","₹4L-₹9L"),("Behavior Analyst","₹5L-₹10L")],
"gov_special":[("Clinical Psychologist Govt","₹7L-₹12L")],
"skills":["communication","analysis"],
"books":["Introduction to Psychology"]
},

"ba sociology":{
"jobs":[("Social Researcher","₹3L-₹7L"),("NGO Officer","₹3L-₹6L")],
"private_jobs":[("CSR Manager","₹6L-₹12L"),("Social Program Coordinator","₹4L-₹8L")],
"gov_special":[("Social Welfare Officer","₹6L-₹10L")],
"skills":["research","analysis"],
"books":["Sociology Basics"]
},

"ba tamil":{
"jobs":[("Tamil Teacher","₹3L-₹6L"),("Tamil Translator","₹3L-₹7L")],
"private_jobs":[("Tamil Content Writer","₹3L-₹6L"),("Tamil News Editor","₹4L-₹8L")],
"gov_special":[("Tamil Lecturer Govt College","₹6L-₹12L"),("Tamil Development Officer","₹6L-₹10L")],
"skills":["tamil writing","literature knowledge","communication"],
"books":["Thirukkural","Sangam Literature","Tholkappiyam"]
}

}

common_gov = [
("UPSC Officer","₹10L-₹20L"),
("SSC Officer","₹5L-₹10L"),
("Bank PO","₹6L-₹12L"),
("Railway Officer","₹5L-₹9L"),
("TNPSC Officer","₹6L-₹11L")
]

if st.button("Get Career Recommendation"):

    course = course.lower()

    for key in career_data:

        if key in course:

            data = career_data[key]

            st.subheader("Recommended Jobs")
            for job,salary in data["jobs"]:
                st.write(job,"-",salary)

            st.subheader("Private Jobs (PJ)")
            for job,salary in data["private_jobs"]:
                st.write(job,"-",salary)

            st.subheader("Special Government Jobs")
            for job,salary in data["gov_special"]:
                st.write(job,"-",salary)

            st.subheader("Common Government Jobs")
            for job,salary in common_gov:
                st.write(job,"-",salary)

            st.subheader("Missing Skills")
            for skill in data["skills"]:
                if skill not in user_skills:
                    st.write(skill)

            st.subheader("Book Recommendations")
            for book in data["books"]:
                st.write(book)

            break