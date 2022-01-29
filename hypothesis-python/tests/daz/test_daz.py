import daz
import pytest
from hypothesis import HealthCheck, given, settings, strategies as st


negative_floats = st.floats(max_value=0, exclude_max=True)
positive_floats = st.floats(min_value=0, exclude_min=True)
negative_floats_no_subnormal = st.floats(max_value=0, exclude_max=True, allow_subnormal=False)
positive_floats_no_subnormal = st.floats(min_value=0, exclude_min=True, allow_subnormal=False)


@pytest.fixture
def with_daz():
    try:
        daz.set_daz()
        yield
    finally:
        # assumes daz was unset originally
        daz.unset_daz()


@pytest.fixture
def with_ftz():
    try:
        daz.set_ftz()
        yield
    finally:
        # assumes ftz was unset originally
        daz.unset_ftz()


@given(d=st.data())
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
@pytest.mark.parametrize("allow_subnormal", [True, False], ids=["allow-subnormal", "no-subnormal"])
def test_negative_floats_work_with_daz_set(d, with_daz, allow_subnormal):
    f = d.draw(negative_floats) if allow_subnormal else d.draw(negative_floats_no_subnormal)
    assert f < 0


@given(d=st.data())
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
@pytest.mark.parametrize("allow_subnormal", [True, False], ids=["allow-subnormal", "no-subnormal"])
def test_positive_floats_work_with_daz_set(d, with_daz, allow_subnormal):
    f = d.draw(positive_floats) if allow_subnormal else d.draw(positive_floats_no_subnormal)
    assert f > 0


@given(d=st.data())
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
@pytest.mark.parametrize("allow_subnormal", [True, False], ids=["allow-subnormal", "no-subnormal"])
def test_negative_floats_work_with_ftz_set(d, with_ftz, allow_subnormal):
    f = d.draw(negative_floats) if allow_subnormal else d.draw(negative_floats_no_subnormal)
    assert f < 0


@given(d=st.data())
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
@pytest.mark.parametrize("allow_subnormal", [True, False], ids=["allow-subnormal", "no-subnormal"])
def test_positive_floats_work_with_ftz_set(d, with_ftz, allow_subnormal):
    f = d.draw(positive_floats) if allow_subnormal else d.draw(positive_floats_no_subnormal)
    assert f > 0


@given(f=negative_floats)
def test_negative_floats_work_without_daz_or_ftz(f):
    assert f < 0


@given(f=positive_floats)
def test_positive_floats_work_without_daz_or_ftz(f):
    assert f > 0
