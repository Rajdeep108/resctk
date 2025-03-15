# Resume Screening Toolkit README

## Overview
A comprehensive toolkit for resume analysis. It allows you to:
- Parse and extract key details from resumes
- Score individual resumes based on job descriptions
- Score and rank multiple resumes for screening and sorting
- Automate resume screening for better hiring decisions
- Create custom workflows and pipelines using modular functions to build your own resume screener and sorter

## Getting Started
You can install the library using pip:
```sh
pip install resctk
```

### Understanding the Structure
The `resctk` library consists of two main modules:
1. **resume**: Contains all the necessary functions for processing resumes.
2. **score**: Contains functions to evaluate resumes.

All processing functions are inside `resctk.resume`, while `resctk.score` currently has two key functions:
- `score_resume`: Uses predefined criteria to assess a resume and provides a score out of 5.
- `screen_all`: Processes a folder containing multiple resumes, sorts them, and returns a list of evaluations.

## Functions

### 1. **Extracting Resume Text**

#### Function: `extract_resume(resume)`
- **Input**: A PDF file containing a resume.
- **Output**: Extracted text as a string.
- **Usage**:
```python
from resctk.resume import extract_resume
resume_text = extract_resume("resume.pdf")
print(resume_text)
```
```
**Example Output:**
```
John Doe
Software Engineer
Experience: 5 years
...
```


### 2. **Parsing the Resume**

#### Function: `parse_resume(extracted_resume, extra_sections=None, regex_parse=False, merge_repetition=False)`
- **Input**: Extracted resume text.
- **Output**: A dictionary where sections of the resume are separated.
- **Features**:
  - Parses the resume based on predefined sections.
  - Can use regex-based parsing (`regex_parse=True`).
  - Supports merging repeated sections (`merge_repetition=True`).
  - Allows adding extra sections beyond the default ones.
- **Usage**:
```python
from resctk.resume import parse_resume
parsed_resume = parse_resume(resume_text, extra_sections=["volunteer work"], regex_parse=False, merge_repetition=True)
print(parsed_resume)
```

### 3. **Extracting Key Resume Information**

#### Functions:
- `get_name(resume_text)`: Extracts the name.
- `get_phone_number(resume)`: Extracts phone number(s).
- `get_email(resume)`: Extracts email address(es).
- `get_experience(resume)`: Extracts experience section.
- `get_skills(resume)`: Extracts skills section.
- `get_education(resume)`: Extracts education section.
- `get_projects(resume)`: Extracts projects section.
- `get_custom_section(resume, section_name, variations)`: Extracts custom-defined sections.

**Usage Example:**
```python
from resctk.resume import *
name = get_name(resume_text)
phone = get_phone_number(resume_text)
skills = get_skills(resume_text)
print(f"Name: {name}, Phone: {phone}, Skills: {skills}")
```

### 4. **Experience & Education Processing**

#### Function: `get_experience_years(experience_section)`
- **Input**: Experience section text.
- **Output**: Total years and months of experience.
- **Usage**:
```python
from resctk.resume import get_experience_years
experience_duration = get_experience_years(parsed_resume['experience'])
print(experience_duration)
```

#### Function: `get_company_names(info_section, spacy_model="en_core_web_md")`
- **Input**: Resume experience section.
- **Output**: List of company names detected.
- **Usage**:
```python
from resctk.resume import get_company_names
companies = get_company_names(parsed_resume['experience'])
print(companies)
```

#### Function: `get_highest_education(info_section)`
- **Input**: Education section.
- **Output**: Highest degree found.
- **Usage**:
```python
from resctk import resume
highest_degree = resume.get_highest_education(parsed_resume['education'])
print(highest_degree)
```

### 5. **Keyword Extraction & Matching**

#### Function: `get_keywords(text, tfidf=10, ner=10, ner_model="en_core_web_sm")`
- **Input**: Any text (e.g., resume or job description).
- **Output**: List of important keywords.
- **Usage**:
```python
from resctk.resume import get_keywords
keywords = get_keywords(resume_text)
print(keywords)
```

#### Function: `match_keywords(list1, list2, ignore_case=True)`
- **Input**: Two keyword lists.
- **Output**: Common keywords found in both.
- **Usage**:
```python
from resctk.resume import match_keywords
matching_keywords = match_keywords(keywords, job_description_keywords)
print(matching_keywords)
```

### 6. **Semantic Similarity Matching**

#### Function: `semantic_similarity(resume, job_description, sentence_transformer_model="paraphrase-MiniLM-L3-v2")`
- **Input**: Resume text and job description.
- **Output**: Similarity score (0 = opposite meaning, 0.5 = neutral, 1 = exact match).
- **Usage**:
```python
from resctk.resume import semantic_similarity
similarity_score = semantic_similarity(resume_text, job_description_text)
print(similarity_score)
```

### 7. **Action Verb Analysis**

#### Function: `count_action_verbs(text)`
- **Input**: Resume text.
- **Output**: Dictionary of action verbs and their frequency.
- **Usage**:
```python
from resctk.resume import count_action_verbs
action_verbs = count_action_verbs(resume_text)
print(action_verbs)
```

### 8. **Experience Comparison**

#### Function: `compare_experience(resume_experience_years, required_experience_years)`
- **Input**: Resume experience duration and required job experience duration.
- **Output**: `1` if experience matches or exceeds, otherwise `0`.
- **Usage**:
```python
from resctk.resume import compare_experience
experience_match = compare_experience("3 years and 6 months", "2 years")
print(experience_match)
```

### 9. **Resume Scoring**

#### Function: `score_resume(parsed_resume, job_description)`
- **Input**: Parsed resume and job description.
- **Output**: Resume score (0 to 5). Any score ≥ 2.4 is considered good.

| **Criteria**                          | **Score Weight** | **Range**  |
|----------------------------------------|-----------------|------------|
| **Overall Semantic Similarity**        | **15%**        | **0 - 1**  |
| **Skills & JD Similarity**             | **20%**        | **0 - 1**  |
| **Experience & JD Similarity**         | **20%**        | **0 - 1**  |
| **Experience Match**                   | **10%**        | **0 or 1** |
| **Education Match**                    | **10%**        | **0 or 1** |
| **JD Keywords Matching Skills**        | **10%**        | **0 - 1**  |
| **JD Keywords Matching Experience**    | **10%**        | **0 - 1**  |
| **Skills Present in Projects**         | **3%**         | **0 - 1**  |
| **Action Verb Repetition**             | **2%**         | **0 - 1**  |

- **Usage:**
```python
from resctk.score import score_resume
score = score_resume(parsed_resume, job_description_text)
print(f"Resume Score: {score}")
```

## Conclusion
This system provides an automated way to analyze resumes against job descriptions, extracting key information and scoring based on predefined criteria.
