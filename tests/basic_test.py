import pytest
from resctk.resume import semantic_search

def test_semantic_search():
    score = semantic_search("I have Python skills", "Looking for Python developer")
    assert isinstance(score, (int, float))  # Ensure it returns a number
    assert 0 <= score <= 1  # Score should be between 0 and 1

