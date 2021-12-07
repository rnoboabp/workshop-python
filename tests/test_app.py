import unittest
from src.utils import statics_log


class TestDemoApp(unittest.TestCase):

    def setUp(self) -> None:
        self.base_path = "resources/test-log.log"

    def tearDown(self) -> None:
        pass

    def test_given_valid_input_when_statics_log_then_ok(self):
        # GIVEN

        # WHEN
        result = statics_log(file_path=self.base_path)
        # THEN
        self.assertEqual(result.get("ErrorCount"), 3)


if __name__ == '__main__':
    unittest.main()
