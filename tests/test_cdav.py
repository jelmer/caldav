import datetime

import pytz
import tzlocal

from caldav.elements.cdav import _to_utc_date_string

SOMEWHERE_REMOTE = pytz.timezone('Brazil/DeNoronha')  # UTC-2 and no DST


def test_to_utc_date_string_date():
    input = datetime.date(2019, 5, 14)
    res = _to_utc_date_string(input)
    assert res == '20190514T000000Z'


def test_to_utc_date_string_utc():
    input = datetime.datetime(2019, 5, 14, 21, 10, 23, 23, tzinfo=datetime.timezone.utc)
    res = _to_utc_date_string(input.astimezone())
    assert res == '20190514T211023Z'


def test_to_utc_date_string_dt_with_pytz_tzinfo():
    input = datetime.datetime(2019, 5, 14, 21, 10, 23, 23)
    res = _to_utc_date_string(SOMEWHERE_REMOTE.localize(input))
    assert res == '20190514T231023Z'


def test_to_utc_date_string_dt_with_local_tz():
    input = datetime.datetime(2019, 5, 14, 21, 10, 23, 23)
    res = _to_utc_date_string(input.astimezone())
    exp_dt = tzlocal.get_localzone().localize(input).astimezone(datetime.timezone.utc)
    exp = exp_dt.strftime("%Y%m%dT%H%M%SZ")
    assert res == exp


def test_to_utc_date_string_naive_dt():
    input = datetime.datetime(2019, 5, 14, 21, 10, 23, 23)
    res = _to_utc_date_string(input)
    exp_dt = tzlocal.get_localzone().localize(input).astimezone(datetime.timezone.utc)
    exp = exp_dt.strftime("%Y%m%dT%H%M%SZ")
    assert res == exp
