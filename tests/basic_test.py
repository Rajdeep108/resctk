import pytest
from resctk.resume import (
    extract_resume, parse_resume, get_name, get_experience_years, get_keywords, 
    match_keywords, semantic_similarity, count_action_verbs, get_company_names
)
from resctk.score import score_resume


@pytest.fixture
def sample_resume_text():
    return """
    John Doe
    Data Scientist | Machine Learning Engineer
    Email: john.doe@example.com | Phone: +1-234-567-890
    Experience:
    - Worked at Google as a Software Engineer from 2018 to 2023
    - Previously at Microsoft as a Data Analyst from 2015 to 2018
    Skills: Python, Machine Learning, Deep Learning, NLP, TensorFlow, PyTorch
    Education: M.Sc. in Artificial Intelligence, Stanford University, 2015
    Projects: Built an AI chatbot, Developed a fraud detection system
    """

def test_get_experience_years():
    experience_section = "Worked at Google as a Software Engineer from 2018 to 2023"
    total_years = get_experience_years(experience_section)
    assert total_years.startswith("5 year") 

def test_match_keywords():
    list1 = ["Python", "Machine Learning", "AI"]
    list2 = ["AI", "Deep Learning", "Python"]
    
    matched = match_keywords(list1, list2, ignore_case=True)

    expected = ["Python", "AI"]
    assert sorted(matched) == sorted([word.lower() for word in expected])

def test_count_action_verbs(sample_resume_text):
    action_verbs = count_action_verbs(sample_resume_text)
    normalized_verbs = {k.lower(): v for k, v in action_verbs.items()}
    assert "developed" in normalized_verbs or "built" in normalized_verbs

def test_semantic_similarity():
    resume_text = "Experienced Machine Learning Engineer proficient in AI and Python."
    job_description = "Looking for an AI expert with Python skills."
    similarity_score = semantic_similarity(resume_text, job_description)
    assert 0.7 <= similarity_score <= 1.0  # Should be a strong match

def test_get_company_names():
    experience_section = "Worked at Google as a Software Engineer from 2018 to 2023"
    companies = get_company_names(experience_section)
    assert "Google" in companies

def test_semantic_search():
    score = semantic_similarity("I have Python skills", "Looking for Python developer")
    assert isinstance(score, (int, float))  # Ensure it returns a number
    assert 0 <= score <= 1  # Score should be between 0 and 1
