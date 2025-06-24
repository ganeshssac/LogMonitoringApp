import unittest
from readLogFile import parse_log_file
import os
import datetime

class TestParseLogFile(unittest.TestCase):
    def test_parse_log_file(self):
        parse_log_file('./testlogs.log')

        # Check if the report.txt file was created
        self.assertTrue(os.path.exists('report.txt'))

        # Read the contents of the report.txt file
        with open('report.txt', 'r') as f:
            report_contents = f.read().strip()

        # Check the contents of the report.txt file
        expected_report = """Type,Process ID,Job Description,Duration
Warning Job or Task,456,job2,0:05:00"""

        self.assertEqual(report_contents, expected_report)

        # Check if the 'Warning: No END event found' message was not printed
        with open('./testlogs.log', 'r') as f:
            log_contents = f.read()
        self.assertNotIn('Warning: No END event found', log_contents)

if __name__ == '__main__':
    unittest.main()