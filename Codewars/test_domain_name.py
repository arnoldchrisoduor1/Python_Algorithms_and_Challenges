import unittest
from domain_name import extract_domain

class TestExtractDomain(unittest.TestCase):
    def test_extract_domain(self):
        url1 = "http://github.com/carbonfive/raygun"
        url2 = "http://www.zombie-bites.com"
        url3 = "https://www.cnet.com"

        self.assertEqual(extract_domain(url1), "github")
        self.assertEqual(extract_domain(url2), "zombie-bites")
        self.assertEqual(extract_domain(url3), "cnet")
        self.assertEqual(extract_domain("http://google.co.jp"), "google")

    def text_extract_domain_with_subdomain(self):
        url = "https://sub.domain.example.com"
        self.assertEqual(extract_domain(url), "example")

    if __name__ == "__main__":
        unittest.main()