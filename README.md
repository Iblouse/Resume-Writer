# Job Application Helper

This repository contains a Streamlit application designed to assist job applicants in tailoring their resumes, creating professional profiles, and preparing for interviews. By leveraging the power of AI agents and various tools, the app streamlines the job application process.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Repository Structure](#repository-structure)
- [Agents and Tasks](#agents-and-tasks)
- [License](#license)
- [Acknowledgements](#Acknowledgements)

## Introduction

The Job Application Helper app utilizes a set of AI agents to perform the following tasks:
1. Research job postings to identify key requirements.
2. Compile detailed personal and professional profiles from various sources.
3. Tailor resumes to highlight the most relevant skills and experiences.
4. Generate interview questions and talking points based on the tailored resume and job requirements.

## Installation

To install and run the application, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/iblouse/Resume-Writer.git
    cd Resume-Writer
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the necessary API keys:
    - Add your OpenAI API key to the environment.
    - Add your SERPER API key to the environment.

## Usage

To start the Streamlit application, run the following command in your terminal:
```bash
streamlit run job_applic_app.py
```

You will be prompted to enter the job posting URL, GitHub URL, and a personal write-up. The application will generate a tailored resume and interview materials based on the provided inputs.

## Repository Structure

- `job_applic_app.py`: Main application file for Streamlit.
- `requirements.txt`: File containing the list of dependencies.
- `utils.py`: Utility functions for fetching API keys.
- `base_resume.md`: Template for the resume.
- `tailored_resume.md`: File where the tailored resume is saved.
- `interview_materials.md`: File where the interview materials are saved.

## Agents and Tasks

### Agents

1. **Tech Job Researcher**
   - Role: Analyze job postings to help job applicants.
   - Tools: ScrapeWebsiteTool, SerperDevTool.

2. **Personal Profiler for Engineers**
   - Role: Research job applicants to help them stand out in the job market.
   - Tools: ScrapeWebsiteTool, SerperDevTool, FileReadTool, MDXSearchTool.

3. **Resume Strategist for Engineers**
   - Role: Tailor resumes to highlight relevant skills and experiences.
   - Tools: ScrapeWebsiteTool, SerperDevTool, FileReadTool, MDXSearchTool.

4. **Engineering Interview Preparer**
   - Role: Create interview questions and talking points based on the resume and job requirements.
   - Tools: ScrapeWebsiteTool, SerperDevTool, FileReadTool, MDXSearchTool.

### Tasks

1. **Research Task**
   - Description: Analyze the job posting URL to extract key skills, experiences, and qualifications.
   - Agent: Tech Job Researcher.

2. **Profile Task**
   - Description: Compile a detailed personal and professional profile.
   - Agent: Personal Profiler for Engineers.

3. **Resume Strategy Task**
   - Description: Tailor the resume to highlight the most relevant areas.
   - Agent: Resume Strategist for Engineers.

4. **Interview Preparation Task**
   - Description: Create interview questions and talking points based on the tailored resume and job requirements.
   - Agent: Engineering Interview Preparer.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Acknowledgements

- Special thanks to the `crewai` and `openai` teams for their incredible tools and APIs.
