import unittest

from task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task_assigns_id_and_starts_pending(self):
        task = self.manager.add_task("Read chapter 1")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Read chapter 1")
        self.assertFalse(task.completed)

    def test_add_task_rejects_empty_or_whitespace_title(self):
        for title in ("", "  \t\n"):
            with self.subTest(title=repr(title)):
                with self.assertRaises(ValueError):
                    self.manager.add_task(title)

    def test_add_task_trims_surrounding_whitespace(self):
        task = self.manager.add_task("  Study for exam \n")
        self.assertEqual(task.title, "Study for exam")

    def test_invalid_add_does_not_consume_task_id(self):
        with self.assertRaises(ValueError):
            self.manager.add_task(" ")
        self.assertEqual(self.manager.add_task("Valid task").task_id, 1)

    def test_complete_task_marks_matching_task_complete(self):
        task = self.manager.add_task("Submit assignment")
        other_task = self.manager.add_task("Review notes")
        self.assertTrue(self.manager.complete_task(task.task_id))
        self.assertTrue(task.completed)
        self.assertFalse(other_task.completed)

    def test_complete_task_rejects_invalid_identifiers(self):
        task = self.manager.add_task("Submit assignment")
        for task_id in ("1", True, 99):
            with self.subTest(task_id=task_id):
                self.assertFalse(self.manager.complete_task(task_id))
        self.assertFalse(task.completed)

    def test_delete_task_removes_matching_task(self):
        task = self.manager.add_task("Review notes")
        self.assertTrue(self.manager.delete_task(task.task_id))
        self.assertEqual(self.manager.list_tasks(), [])

    def test_delete_task_rejects_unknown_or_invalid_identifiers(self):
        task = self.manager.add_task("Review notes")
        for task_id in ("1", True, 99):
            with self.subTest(task_id=task_id):
                self.assertFalse(self.manager.delete_task(task_id))
        self.assertEqual(self.manager.list_tasks(), [task])


if __name__ == "__main__":
    unittest.main()
