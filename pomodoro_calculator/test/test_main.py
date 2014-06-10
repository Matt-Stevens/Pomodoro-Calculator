import unittest
from datetime import datetime
from freezegun import freeze_time
from pomodoro_calculator import PomodoroCalculator


class PomodoroTest(unittest.TestCase):

    def setUp(self):
        self.calculator = PomodoroCalculator()

    def test_retriever_class_exists(self):
        """
        Does the `PomodoroCalculator` class exist?
        """
        self.assertTrue('PomodoroCalculator' in globals())

    @freeze_time('2014-01-01 00:00:00')
    def test_create_datetime_with_hours(self):
        """
        Does `_create_datetime` work correctly with only hours provided?
        """
        self.assertEqual(
            self.calculator._create_datetime('15'),
            datetime(2014, 1, 1, 15),
        )

    @freeze_time('2014-01-01 00:00:00')
    def test_create_datetime_with_hours_and_minutes(self):
        """
        Does `_create_datetime` work correctly with hours and minutes?
        """
        self.assertEqual(
            self.calculator._create_datetime('15:30'),
            datetime(2014, 1, 1, 15, 30),
        )

    @freeze_time('2014-01-01 00:00:00')
    def test_create_datetime_with_hours_minutes_and_seconds(self):
        """
        Does `_create_datetime` work correctly with hours, minutes and seconds?
        """
        self.assertEqual(
            self.calculator._create_datetime('15:30:25'),
            datetime(2014, 1, 1, 15, 30, 25),
        )

    @freeze_time('2014-01-02 00:00:00')
    def test_create_datetime_with_different_day(self):
        """
        Does `_create_datetime` add another day is `tomorrow` is passed?
        """
        self.assertEqual(
            self.calculator._create_datetime('15:30:25', tomorrow=True),
            datetime(2014, 1, 2, 15, 30, 25),
        )
