import unittest

from fastapi.testclient import TestClient

from day6.ch02_basemodel.main import app


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_home_and_stylesheet(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('lang="ko"', response.text)
        self.assertIn('action="/calculate"', response.text)
        self.assertEqual(self.client.get("/static/style.css").status_code, 200)

    def test_operations(self):
        cases = [
            ("7", "3", "add", "10"),
            ("7", "3", "subtract", "4"),
            ("7", "3", "multiply", "21"),
            ("7", "2", "divide", "3.5"),
            ("0.1", "0.2", "add", "0.3"),
            ("-5", "2", "multiply", "-10"),
            ("0", "2", "divide", "0"),
            (" 2.5 ", ".5", "subtract", "2"),
            ("1000000000000", "1000000000000", "multiply", "1000000000000000000000000"),
            ("0.000000000001", "0.000000000001", "divide", "1"),
        ]
        for a, b, operation, expected in cases:
            with self.subTest(a=a, b=b, operation=operation):
                response = self.client.post("/calculate", data={"a": a, "b": b, "operation": operation})
                self.assertEqual(response.status_code, 200)
                self.assertIn(f'= {expected}</p>', response.text)

    def test_rounding_is_disclosed(self):
        cases = [("1", "3", "divide", "0.333333333333"),
                 ("0.000000000001", "0.5", "multiply", "0.000000000001"),
                 ("-0.000000000001", "0.1", "multiply", "0")]
        for a, b, operation, expected in cases:
            with self.subTest(a=a, b=b):
                response = self.client.post("/calculate", data={"a": a, "b": b, "operation": operation})
                self.assertEqual(response.status_code, 200)
                self.assertIn(f'≈ {expected}</p>', response.text)
                self.assertIn("반올림한 결과", response.text)

    def test_invalid_inputs(self):
        cases = [
            ("1", "0", "divide", "0으로 나눌 수 없습니다"),
            ("1", "-0.0", "divide", "0으로 나눌 수 없습니다"),
            ("", "2", "add", "첫 번째 수를 입력"),
            ("1", " ", "add", "두 번째 수를 입력"),
            ("abc", "2", "add", "숫자만 입력"),
            ("NaN", "2", "add", "숫자만 입력"),
            ("Infinity", "2", "add", "숫자만 입력"),
            ("1e10", "2", "add", "숫자만 입력"),
            ("1000000000001", "2", "add", "1조까지"),
            ("0.1234567890123", "2", "add", "최대 12자리"),
            ("1", "2", "unknown", "올바른 연산"),
        ]
        for a, b, operation, expected in cases:
            with self.subTest(a=a, b=b, operation=operation):
                response = self.client.post("/calculate", data={"a": a, "b": b, "operation": operation})
                self.assertEqual(response.status_code, 400)
                self.assertIn(expected, response.text)

    def test_html_is_escaped(self):
        response = self.client.post("/calculate", data={"a": '<script>alert(1)</script>', "b": "2", "operation": "add"})
        self.assertEqual(response.status_code, 400)
        self.assertNotIn("<script>", response.text)
        self.assertIn("&lt;script&gt;", response.text)

    def test_missing_form_fields(self):
        self.assertEqual(self.client.post("/calculate", data={}).status_code, 400)


if __name__ == "__main__":
    unittest.main(verbosity=2)
