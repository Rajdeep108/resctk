# Resume Screening Toolkit

## Overview
A comprehensive AI-powered toolkit for resume analysis 🤖. It allows you to:
- Parse and extract key details from resumes
- Score individual resumes based on job descriptions
- Score and rank multiple resumes for screening and sorting
- Automate resume screening for better hiring decisions
- Create custom workflows and pipelines using modular functions to build your own resume screener and sorter

### 📢 What's New in This Version?  
✅ **Now supports `.docx` resumes along with `.pdf`** – Easily extract, parse, and score resumes in both formats!  
✅ **Improved bulk resume screening (`screen_all`)** – Automatically processes and ranks resumes from a folder, whether they are PDFs or Word documents.

## 🚀 Quick Start Guide
1. **Install the package**  
```sh
pip install resctk
```
2. **Extract Resume (optional)**
```python
from resctk.resume import extract_resume
text = extract_resume("resume.pdf")
print(text)
```
3. **Parse the extracted Resume Text (optional)**
```python
from resctk.resume import parse_resume
parsed = parse_resume(text)
print(f"Parsed Resume Dictionary: {parsed}")
```
4. **Score a single Resume**
```python
from resctk.score import score_resume
score = score_resume("path/to/resume.pdf", "Python Developer job description...")
print(f"Resume Score: {score}")
```
5. **Score entire Folder of Resumes (Bulk Scoring)**
```python
from resctk.score import screen_all
arranged_list = screen_all("folderpath/containing/resumes/", "Web Developer job description....", rename_files=False)
print(f"Sorted Resume list: {arranged_list}")
```
🔹 Now you're ready to use all the features! Read on for details.  

## 📌 Getting Started - DETAILED
You can install the library using pip:
```sh
pip install resctk
```

## Use Cases
**Who is this for?**
✔️ **Recruiters** → Automate resume screening  
✔️ **Hiring Managers** → Compare multiple applicants  
✔️ **Job Seekers** → Optimize resumes for better scoring  
✔️ **HR Tech Developers** → Build AI-based hiring solutions  

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
- **Input**: The PDF/DOCX filepath containing the resume elements. (supports PDF and DOCX)
- **Output**: Extracted text as a string.
- **Usage**:
```python
from resctk.resume import extract_resume
resume_text = extract_resume("resume.pdf")
print(resume_text)
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
  - If regex_parse is set False it will use advanced NLP techniques to parse  the resume.
  - Supports merging repeated sections (`merge_repetition=True`).
  - Allows adding extra sections beyond the default ones.
- **Usage**:
```python
from resctk.resume import parse_resume
parsed_resume = parse_resume(resume_text, extra_sections=["volunteer work"], regex_parse=False, merge_repetition=True)
print(parsed_resume)
```
**Example Output:**
```
{
  "name": "John Doe",
  "experience": "5 years at XYZ Corp",
  "skills": ["Python", "Machine Learning"]
}
```

### 3. **Extracting Key Resume Information**
| Function | Purpose |
|----------|---------|
| `get_name(resume_text)` | Extracts the applicant's name |
| `get_phone_number(resume)` | Finds phone numbers in the resume |
| `get_email(resume)` | Extracts email addresses |
| `get_experience(resume)` | Retrieves the experience section |
| `get_skills(resume)` | Extracts listed skills |
| `get_education(resume)` | Finds educational qualifications |
| `get_projects(resume)` | Retrieves project details |

**Usage Example:**
```python
from resctk.resume import *
name = get_name(resume_text)
phone = get_phone_number(resume_text)
skills = get_skills(resume_text)
print(f"Name: {name}, Phone: {phone}, Skills: {skills}")
```
**Example Output:**
```
Name: John Doe, Phone: +1-234-567-890, Skills: ['Python', 'Machine Learning']
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
**Example Output:**
```
5 year(s) 0 month(s)
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
**Example Output:**
```
["Python", "AI", "Software Engineering"]
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
**Example Output:**
```
['Python', 'finance']
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
**Example Output:**
```
0.822345712
```

#### 📊 Understanding Resume Scores  

To understand how the resume screening and scoring work, you can print the package documentation:  

```python
import resctk.info
print(resctk.info.__doc__)
```
**Output:**
```
- Score Resume: the score is calculated out of 5. Any resume with a score equal to or above 2.4 is considered a good match for the job.
- Semantic Similarity: the score is in the range 0 to 1; 0 = completely opposite meaning, 0.5 = no similarity, 1 = exactly the same.
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
**Example Output:**
```
{"Developed":1,"Created":3}
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
score = score_resume("filepath/resume.pdf", "Python Developer job description...", after_decimal=4,status_message=True)
print(f"Resume Score: {score}")
```
### 🔍 **Arguments Explained:**
| **Argument**      | **Type**  | **Default**    | **Description** |
|------------------|----------|---------------|----------------|
| `resume`        | `str`    | **Required**   | The **file path** of the resume (PDF or DOCX). |
| `job_descr`     | `str`    | **Required**   | The **job description text** to compare the resume against. |
| `after_decimal` | `int`    | `4`            | *(Optional)* Number of decimal places to round the final score. |
| `status_message` | `bool`   | `True`         | *(Optional)* If `True`, displays **"Scoring in progress!..... ⏳"** while scoring. |
---

**Example Output:**
```
Scoring in progress!..... ⏳

Resume Score: 3.81
```

### 10. **Screening Multiple Resumes**
```python
from resctk.score import screen_all
ranked_resumes = screen_all(folder_path = "/path/to/folder_containing_resumes", job_descr = "job_description_text", rename_files= False, status_message=True)
print(ranked_resumes)
```
### 🔍 **Arguments Explained:**
| **Argument**      | **Type**  | **Default**  | **Description** |
|------------------|----------|--------------|----------------|
| `folder_path`   | `str`    | **Required** | The **path to the folder** containing resumes (PDF/DOCX files). |
| `job_descr`     | `str`    | **Required** | The **job description text** to compare against. |
| `rename_files`  | `bool`   | `False`      | *(Optional)* If `True`, renames files directly in the parent folder by prefixing them with their score. |
| `status_message` | `bool`   | `False`      | *(Optional)* If `True`, displays **"🔍 Screening all resumes... Please wait, this may take a few minutes!..."** while screening. |
---

**Example Output:**
```
🔍 Screening all resumes... Please wait, this may take a few minutes!
☕ Grab a coffee in the meantime! ☕


✅ Screening completed! Here are the results:
[
  ('resume_sample.pdf', 2.693), ('Student Athlete Resume.pdf', 2.2015), ('Bad-Resume.pdf', 1.901), ('functionalsample.pdf', 1.497)
]
```

## Creating a Custom Resume Screener
Users can customize the screening process by defining their own scoring rules, keyword matches, or evaluation criteria. By combining functions from `resctk.resume` and `resctk.score`, they can build procedural workflows tailored to specific hiring needs.

### Example: Custom Resume Screener
```python
from resctk.resume import extract_resume, parse_resume, get_keywords, semantic_similarity, match_keywords
from resctk.score import score_resume
import os

def custom_screener(folder_path, job_description):
    results = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            filepath = os.path.join(folder_path, filename)
            text = extract_resume(filepath)
            parsed = parse_resume(text)
            similarity_score = semantic_similarity(parsed, job_description)
            score_2 = semantic_similarity(text, job_description)
            keywords = get_keywords(text)
            keyscore = match_keywords(keywords, get_keywords(job_description))
            final_score = keyscore + similarity_score + score_2
            results.append({"name": parsed.get("name", filename), "score": final_score, "keywords": keywords})
    return results

# Example usage
job_desc = "Looking for a Python developer with experience in AI."
results = custom_screener("/path/to/resumes", job_desc)
print(results)
```
**Example Output:**
```
[
  {'name': 'John Doe', 'score': 3.9, 'keywords': ['Python', 'AI', 'Software Engineering']},
  {'name': 'Jane Smith', 'score': 4.1, 'keywords': ['Machine Learning', 'Deep Learning', 'Python']}
]
```

This modular approach allows users to tweak and extend the scoring system beyond the built-in functions for more accurate and specific hiring decisions.

## Conclusion
This system provides an automated way to analyze resumes against job descriptions, extracting key information and scoring based on predefined criteria and customized.