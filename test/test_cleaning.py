# test_cleaning.py
import pytest
import pandas as pd
from utils.cleaning_helpers import _normalize_id, _validate_required_columns, _clean_text_fields, _parse_and_validate_dates
import os


def test_normalize_id_pubmed_generates_ids():
    df = pd.DataFrame({"id": ["1", None, "  ", "3"]})
    df = _normalize_id(df,source_name="test")
    assert df["id"].notnull().all()
    assert df["id"].apply(lambda x: isinstance(x, str)).all()

def test_normalize_id_clinical_generates_ids():
    df = pd.DataFrame({"id": ["NCT001", None, ""]})
    df = _normalize_id(df,source_name="test")
    assert df["id"].notnull().all()
    assert df["id"].apply(lambda x: isinstance(x, str)).all()

def test_validate_required_columns_raises():
    df = pd.DataFrame({"id": [1], "title": ["test"]})
    required = {"id", "title", "journal"}
    with pytest.raises(ValueError):
        _validate_required_columns(df, required, source_name="test")

def test_clean_text_fields_removes_nulls(tmp_path):
    log_path = tmp_path / "test_log.csv"
    df = pd.DataFrame({"title": ["titre ", None], "journal": [" journal ", " "]})
    cleaned = _clean_text_fields(df.copy(), "title", "journal", str(log_path))
    assert cleaned.shape[0] == 1
    assert os.path.exists(log_path)

def test_parse_and_validate_dates(tmp_path):
    log_path = tmp_path / "bad_dates.csv"
    df = pd.DataFrame({"date": ["2020-01-01", "not a date"]})
    cleaned = _parse_and_validate_dates(df.copy(), "date", str(log_path))
    assert len(cleaned) == 1
    assert os.path.exists(log_path)




