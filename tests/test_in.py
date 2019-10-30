import pytest

def test_answer():
    assert 1==0  # to see what was printed
def test_answer2():
    assert 1==1  # to see what was printed


heroku config:set AWS_IAM_ACCESS_KEY=AKIAT77UJVVFOGZWMZ7M
heroku config:set AWS_IAM_SECRET_KEY=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
