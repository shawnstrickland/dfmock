import pytest
import pandas as pd
from dfmock.dfmock import DFMock
from datetime import datetime

def test_mock_datetime_simple():
    mock = DFMock()
    
    stamps = mock._mock_datetime(count=1)
    
    assert len(stamps) == 1
    assert isinstance(stamps[0], pd.Timestamp)

def test_mock_datetime_past():
    mock = DFMock()
    stamps = mock._mock_datetime(count=100, allow_future=False)
    in_future = False
    for stamp in stamps:
        if stamp > pd.Timestamp(ts_input = datetime.now().isoformat() + " +4"):
            in_future = True
    assert not in_future 

def test_mock_datetime_many():
    mock = DFMock()
    count = 10000
    stamps = mock._mock_datetime(count=count)
    assert len(stamps) == count

def test_mock_datetime_very_old():
    mock = DFMock()
    stamps = mock._mock_datetime(year_start=1800, count=1000)
    is_very_old = False
    for stamp in stamps:
        if stamp.year < 1900:
            is_very_old = True
    assert is_very_old

def test_mock_string():
    pass

def test_mock_integer():
    pass

def test_mock_float():
    pass

def test_mock_bool():
    pass

def test_mock_category():
    pass

def test_mock_timedelta():
    pass
