import streamlit as st  # Import Streamlit for building the web application
import warnings
warnings.filterwarnings('ignore')

from crewai import Agent, Task, Crew

import os
from utils import get_openai_api_key, get_serper_api_key

# Set environment variables for API keys and model name
openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
os.environ["SERPER_API_KEY"] = get_serper_api_key()

from crewai_tools import (
    FileReadTool,
    ScrapeWebsiteTool,
    MDXSearchTool,
    SerperDevTool
)

# Initialize the tools for the agents
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
read_resume = FileReadTool(file_path='base_resume.md')
semantic_search_resume = MDXSearchTool(mdx='base_resume.md')

# Define agents for different tasks
researcher = Agent(
    role="Tech Job Researcher",
    goal="Make sure to do amazing analysis on job posting to help job applicants",
    tools=[scrape_tool, search_tool],
    verbose=True,
    backstory=(
        "As a Job Researcher, your prowess in navigating and extracting critical "
        "information from job postings is unmatched. Your skills help pinpoint the "
        "necessary qualifications and skills sought by employers, forming the foundation "
        "for effective application tailoring."
    )
)

profiler = Agent(
    role="Personal Profiler for Engineers",
    goal="Do incredible research on job applicants to help them stand out in the job market",
    tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
    verbose=True,
    backstory=(
        "Equipped with analytical prowess, you dissect and synthesize information from diverse "
        "sources to craft comprehensive personal and professional profiles, laying the groundwork "
        "for personalized resume enhancements."
    )
)

resume_strategist = Agent(
    role="Resume Strategist for Engineers",
    goal="Find all the best ways to make a resume stand out in the job market.",
    tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
    verbose=True,
    backstory=(
        "With a strategic mind and an eye for detail, you excel at refining resumes to highlight the "
        "most relevant skills and experiences, ensuring they resonate perfectly with the job's requirements. "
        "Highlight only the skills, training, and experience directly relevant to the specific job or opportunity."
    )
)

interview_preparer = Agent(
    role="Engineering Interview Preparer",
    goal="Create interview questions and talking points based on the resume and job requirements",
    tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
    verbose=True,
    backstory=(
        "Your role is crucial in anticipating the dynamics of interviews. With your ability to formulate key "
        "questions and talking points, you prepare candidates for success, ensuring they can confidently address "
        "all aspects of the job they are applying for."
    )
)

# Define tasks for the agents
research_task = Task(
    description=(
        "Analyze the job posting URL provided ({job_posting_url}) to extract key skills, experiences, and qualifications "
        "required. Use the tools to gather content and identify and categorize the requirements."
    ),
    expected_output=(
        "A structured list of job requirements, including necessary skills, qualifications, and experiences."
    ),
    agent=researcher,
    async_execution=True
)

profile_task = Task(
    description=(
        "Compile a detailed personal and professional profile using the GitHub ({github_url}) URLs, and personal write-up "
        "({personal_writeup}). Utilize tools to extract and synthesize information from these sources."
    ),
    expected_output=(
        "A comprehensive profile document that includes skills, project experiences, contributions, interests, and "
        "communication style."
    ),
    agent=profiler,
    async_execution=True
)

resume_strategy_task = Task(
    description=(
        "Using the profile and job requirements obtained from previous tasks, tailor the resume to highlight the most "
        "relevant areas. Employ tools to adjust and enhance the resume content. Make sure this is the best resume ever but "
        "don't make up any information. Update every section, including the initial summary, work experience, skills, "
        "and education. All to better reflect the candidate's abilities and how it matches the job posting."
    ),
    expected_output=(
        "An updated resume that effectively highlights the candidate's qualifications and experiences relevant to the job."
    ),
    output_file="tailored_resume.md",
    context=[research_task, profile_task],
    agent=resume_strategist
)

interview_preparation_task = Task(
    description=(
        "Create a set of potential interview questions and talking points based on the tailored resume and job requirements. "
        "Utilize tools to generate relevant questions and discussion points. Make sure to use these questions and talking points "
        "to help the candidate highlight the main points of the resume and how it matches the job posting."
    ),
    expected_output=(
        "A document containing key questions and talking points that the candidate should prepare for the initial interview."
    ),
    output_file="interview_materials.md",
    context=[research_task, profile_task, resume_strategy_task],
    agent=interview_preparer
)

# Create a crew that handles all tasks
job_application_crew = Crew(
    agents=[researcher, profiler, resume_strategist, interview_preparer],
    tasks=[research_task, profile_task, resume_strategy_task, interview_preparation_task],
    verbose=True
)

# Streamlit UI for user inputs and displaying results
st.title("Job Application Helper")

st.header("Enter Job Details")

job_posting_url = st.text_input('Job Posting URL', 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund')
github_url = st.text_input('GitHub URL', 'https://github.com/joaomdmoura')
personal_writeup = st.text_area('Personal Write-up', 
                                """Noah is an accomplished Software Engineering Leader with 18 years of experience, 
                                specializing in managing remote and in-office teams, and expert in multiple programming 
                                languages and frameworks. He holds an MBA and a strong background in AI and data science. 
                                Noah has successfully led major tech initiatives and startups, proving his ability to drive 
                                innovation and growth in the tech industry. Ideal for leadership roles that require a strategic 
                                and innovative approach.""")

if st.button('Generate Application Materials'):
    # Gather inputs and kickoff the tasks
    job_application_inputs = {
        'job_posting_url': job_posting_url,
        'github_url': github_url,
        'personal_writeup': personal_writeup
    }

    # Execute the tasks and display a loading message
    with st.spinner('Generating application materials...'):
        result = job_application_crew.kickoff(inputs=job_application_inputs)

    st.success('Application materials generated successfully!')

    # Display the results
    st.header("Generated Resume")
    

    st.header("Interview Materials")
