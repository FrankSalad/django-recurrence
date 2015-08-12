from datetime import datetime
from recurrence import Recurrence, Rule
import recurrence


def test_truthiness_with_single_rrule():
    rule = Rule(
        recurrence.DAILY
    )

    object = Recurrence(
        rrules=[rule]
    )

    assert bool(object)


def test_truthiness_with_single_exrule():
    rule = Rule(
        recurrence.DAILY
    )

    object = Recurrence(
        exrules=[rule]
    )

    assert bool(object)


def test_truthiness_with_single_rdate():
    object = Recurrence(
        rdates=[datetime(2014, 12, 31, 0, 0, 0)]
    )

    assert bool(object)


def test_truthiness_with_single_exdate():
    object = Recurrence(
        exdates=[datetime(2014, 12, 31, 0, 0, 0)]
    )

    assert bool(object)


def test_truthiness_with_dtstart():
    object = Recurrence(
        dtstart=datetime(2014, 12, 31, 0, 0, 0)
    )

    assert bool(object)


def test_truthiness_with_dtend():
    object = Recurrence(
        dtend=datetime(2014, 12, 31, 0, 0, 0)
    )

    assert bool(object)


def test_falsiness_with_empty_recurrence_object():
    assert not bool(Recurrence())


def test_recurrence_rdate_subtraction():
    a = Recurrence(
        rdates=[datetime(2014, 12, 31, 0, 0, 0)]
    )
    b = Recurrence(
        rdates=[datetime(2014, 12, 31, 0, 0, 0)]
    )
    assert (a - b).count() == 0


def test_recurrence_rrule_subtraction():
    rule = Rule(
        recurrence.DAILY
    )
    a = Recurrence(
        rrules=[rule],
        dtend=datetime(2038, 12, 31, 0, 0, 0)
    )
    b = Recurrence(
        rrules=[rule]
    )
    assert (a - b).count() == 0, str(list((a - b).occurrences()))
