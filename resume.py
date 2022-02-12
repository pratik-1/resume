import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Pratik Nandekar
### Python Developer/Data Scientist
##### *Resume* 
''')

image = Image.open('data/dp.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- As a python developer, I have experience writing scripts that connects to the database **E**xtract data, perform aggregations or **T**ransformations and **L**oad into other databases or create reports
- Experience of working with databases such as Oracle and Postgres.
- Certified Big Data Specialist along with knowledge of data science and machine learning tools and frameworks.
''')

#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#data-science-apps">Data Science Apps</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)

@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img


#####################
st.markdown('''
## Education
''')
txt('**MSc Data Science and Analytics**, *University of Leeds*, UK', '2021-2022')
st.markdown('''
- Worked on a project in which a framework is built to analysis and visualize stocks and take informed decision. The application was entirely built in python.
''')
txt('**Bachelor of Engineering**, *G.H. Raisoni College of Engineering and Technology, Nagpur*, India', '2009-2013')
st.markdown(''' 
- Graduated with First Class Honors.
- Participated and won 1st prize in technical event in TechFest IIT-Bombay.[[certificate](https://raw.githubusercontent.com/pratik-1/resume/main/data/techfest.jpg)]
''')

#####################
st.markdown('''
## Work Experience
''')
st.markdown('''
#### **Brillio Technologies Pvt. Ltd.**
''')
txt('**Senior Engineer**, CLIENT: CIENA LTD., MONTREAL, CANADA,', '2019-2019')
st.markdown('''
- Collect and manage clients network elements data in a Big Data Cluster. 
- Automate the process to collect the data from sources and organize it in a Big Data Cluster.
- Created Apis in flask application.
''')

st.markdown('''
#### **Tata Consultancy Services Ltd.**
''')
txt('**Information Technology Analyst**, CLIENT#4: ATHENE INSURANCE, USA',  '2018-2019')
st.markdown('''
- Responsible for creating a module for agent commission reporting, sales reporting.
- We populated data in dimensions and fact tables after conforming data from multiple sources.
- We perform ETL operations using python. Created and scheduled jobs, responsible for deployment process.
- As a value-addon, created text-analytics model for generating a report from *Service Now* tool to derive top drivers \
for the frequently occurring incidents.
''')

txt('**System Engineer**, CLIENT#3: BANK OF MONTREAL, USA',  '2017-2018')
st.markdown('''
- Responsible for creating reports generation using python, shell scripts.
- Built stored procedures, functions.
- Create and schedule the jobs.
- Given training to the team members.
''')

txt('**System Engineer**, CLIENT#2: BANK OF AMERICA, UK',  '2016-2017')
st.markdown('''
- Requirement gathering, migrate application from Unix to Linux.
- Write shell and python scripts to automate the process.
- Resolve issues in existing application.
''')

txt('**Trainee**, CLIENT#1(INTERNAL): TCS - ULTIMATIX HRMS, INDIA',  '2014-2016')
st.markdown('''
- Prepare functional documents, data migration activities of Core HR module.
- Development of new reports, automate the report generation process.
- Single handedly addressed data issues and change requests of HR- international payroll activities.[[award](https://raw.githubusercontent.com/pratik-1/resume/main/data/Special_Initiative.jpg)]
''')

#####################
st.markdown('''
## Data Science Apps
''')
txt4('Iris prediction app', 'A web app predicts the species of *iris flower* based on input parameters',
     'https://iris-predsapp.herokuapp.com/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `bokeh`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`Pytorch`')
txt3('Web development', '`Django`, `Flask`')
txt3('Model deployment', '`streamlit`, `Heroku`')

#####################
st.markdown('''
## External Certifications
''')
st.markdown('''
- [Data Scientist with Python track](https://raw.githubusercontent.com/pratik-1/resume/2aa57121c825d815075e5f471c1fc2d65dbe9826/data/Data_Scientist_python_track.jpg)
- [Data Scientist with R track](https://raw.githubusercontent.com/pratik-1/resume/2aa57121c825d815075e5f471c1fc2d65dbe9826/data/Data_Scientist_R_track.jpg)
- [Big Data Specialist](data/BD_specialist.jpg)
''')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/pratik-nandekar-1b3b9a31/')
txt2('GitHub', 'https://github.com/pratik-1')
