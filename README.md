# Job Application Helper

This Streamlit app helps job applicants by analyzing job postings and generating tailored resumes, profiles, and interview materials. The app uses the CrewAI framework to define and manage agents and tasks for job application preparation.

## Features

- **Job Posting Analysis:** Extracts key skills, qualifications, and experiences from job postings.
- **Personal and Professional Profiling:** Compiles detailed profiles based on GitHub URLs and personal write-ups.
- **Resume Tailoring:** Enhances resumes to highlight relevant qualifications and experiences.
- **Interview Preparation:** Generates potential interview questions and talking points based on the tailored resume and job requirements.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/iblouse/Resume-Writer.git
    cd Resume-Writer
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the necessary API keys for OpenAI and Serper. Set them in your environment variables or use the provided utility functions.

2. Run the Streamlit app:
    ```sh
    streamlit run job_applic_app.py
    ```

3. Open your web browser and navigate to `http://localhost:8501`.

4. Enter the job posting URL, GitHub URL, and a personal write-up in the provided fields.

5. Click on the "Generate Application Materials" button to start the process.

6. The app will display the generated resume and interview materials.

## Files

- **job_applic_app.py:** Main Streamlit app file.
- **requirements.txt:** Lists the dependencies required to run the app.
- **utils.py:** Contains utility functions for fetching API keys.

## Example

Here is an example of how to use the app:

1. Enter the job posting URL:
    ```
    [https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund](https://www.linkedin.com/jobs/search/?currentJobId=3952693344&keywords=cvs%20health&origin=BLENDED_SEARCH_RESULT_NAVIGATION_JOB_CARD&originToLandingJobPostings=3958577063%2C3941885038%2C3952693344)
    ```

2. Enter the GitHub URL:
    ```
    https://github.com/iblouse
    ```

3. Enter the personal write-up:
    ```markdown
    An AWS Certified Machine Learning Specialist and seasoned Data Scientist with a Master’s in Statistics & Applied Mathematics brings a wealth of experience in data analysis, predictive modeling, and cloud technologies. With adept skills in Google Cloud services, particularly Vertex AI and BigQuery, high-impact solutions can be delivered within analytics and behavior change teams. The background aligns with the sophisticated use of Google Cloud Platform to analyze petabytes of healthcare data, complemented by certifications in machine learning and cloud platforms. Enthusiastic about employing advanced analytics and collaborative approaches to support the vision for a total approach to health and wellness through innovative data-driven strategies.
    ```

4. Click on "Generate Application Materials" to get the tailored resume and interview materials.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
