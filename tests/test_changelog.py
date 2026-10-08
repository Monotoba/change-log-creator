"""Exercise real Git history and command-line behavior."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest

from git import Repo
from change_log_creator._app import main
from change_log_creator.change_log_creator import create_change_log_from_repo


class ChangelogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)
        self.repo = Repo.init(self.path / "repo", initial_branch="main")
        self.addCleanup(self.repo.close)
        with self.repo.config_writer() as config:
            config.set_value("user", "name", "Demo Tester")
            config.set_value("user", "email", "tester@example.invalid")
        for i in range(3):
            file = Path(self.repo.working_tree_dir) / "file.txt"
            file.write_text(str(i))
            self.repo.index.add(["file.txt"])
            self.repo.index.commit(f"Main change {i}")
        self.repo.create_head("feature").checkout()
        file.write_text("feature")
        self.repo.index.add(["file.txt"])
        self.repo.index.commit("Feature-only change")
        self.repo.heads.main.checkout()
        self.args = ["-r", self.repo.working_tree_dir]

    def test_supplied_repo_defaults_to_head(self):
        text = create_change_log_from_repo(self.repo.working_tree_dir)
        self.assertIn("Main change 2", text)
        self.assertNotIn("Feature-only change", text)

    def test_explicit_branch_and_count(self):
        text = create_change_log_from_repo(self.repo.working_tree_dir, 1, "feature")
        self.assertIn("Feature-only change", text)
        self.assertNotIn("Main change", text)

    def test_missing_repo_and_invalid_counts(self):
        with self.assertRaises(ValueError):
            create_change_log_from_repo()
        for count in [0, -1, True]:
            with self.subTest(count=count), self.assertRaises(ValueError):
                create_change_log_from_repo(self.repo.working_tree_dir, count)

    def test_cli_passes_branch_and_count(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            main(self.args + ["-b", "feature", "-c", "1"])
        self.assertIn("Feature-only change", output.getvalue())
        self.assertNotIn("Main change", output.getvalue())

    def test_file_output_and_force(self):
        target = self.path / "CHANGELOG.md"
        args = self.args + ["-o", str(target)]
        main(args)
        self.assertIn("Main change 2", target.read_text())
        target.write_text("existing content")
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
            main(args)
        self.assertEqual(error.exception.code, 2)
        self.assertEqual(target.read_text(), "existing content")
        main(args + ["-f"])
        self.assertIn("Main change 2", target.read_text())

    def test_invalid_repo_branch_and_count_report_cli_errors(self):
        cases = [["-r", str(self.path / "missing")], self.args + ["-b", "missing"],
                 self.args + ["-c", "0"]]
        for args in cases:
            with self.subTest(args=args), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                main(args)
            self.assertEqual(error.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
