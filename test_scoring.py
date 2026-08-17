from src.scoring import css
def test_css_bounds():
    assert css({k:0 for k in "UKPRECXH"})==0.0
    assert css({k:4 for k in "UKPRECXH"})==1.0
