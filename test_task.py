import unittest
import io
import sys
import os
import datetime
from unittest.mock import patch

# Import the functions from your task manager program
from task import main, add_task, list_tasks, mark_completed, save_tasks

class test_task(unittest.TestCase):

    def setUp(self):
        self.task_file = "test_tasks.txt"
        sys.stdout = io.StringIO()  # Redirect stdout to capture print statements
        self.current_time = datetime.datetime.now()
        self.test_tasks = [{"name": "Task 1", "completed": False, "timestamp": self.current_time},
                          {"name": "Task 2", "completed": True, "timestamp": self.current_time}]

    def tearDown(self):
        sys.stdout = sys.stdout  # Restore normal stdout
        if os.path.exists(self.task_file):
            os.remove(self.task_file)

    def test_add_task(self):
        tasks = []
        input_data = "Test Task\n4"
        with patch('builtins.input', side_effect=input_data.split('\n')):
            with patch('task.datetime.datetime') as mock_datetime:
                mock_datetime.now.return_value = self.current_time
                add_task(tasks)
                self.assertEqual(tasks[0]["name"], "Test Task")

    def test_list_tasks(self):
        with patch('task.datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = self.current_time
            with patch('builtins.input', side_effect="4\n".split('\n')):
                with patch('task.sys.stdout', new_callable=io.StringIO):
                    add_task(self.test_tasks)
                    main()
        output = sys.stdout.getvalue()
        expected_output = "1. Task 1 - Not Completed (Added on {})\n2. Task 2 - Completed (Added on {})\n".format(self.current_time, self.current_time)
        self.assertEqual(output, expected_output)

    def test_mark_completed(self):
        tasks = self.test_tasks.copy()
        input_data = "1\n4"
        with patch('builtins.input', side_effect=input_data.split('\n')):
            with patch('task.datetime.datetime') as mock_datetime:
                mock_datetime.now.return_value = self.current_time
                mark_completed(tasks)
                self.assertTrue(tasks[0]["completed"])
    
    def test_save_tasks(self):
        tasks = self.test_tasks.copy()
        save_tasks(tasks)
        self.assertTrue(os.path.exists(self.task_file))
        with open(self.task_file, "r") as file:
            saved_data = file.read()
        expected_data = "Task 1,False,{}\nTask 2,True,{}\n".format(self.current_time, self.current_time)
        self.assertEqual(saved_data, expected_data)

if name == "main":
    unittest.main()