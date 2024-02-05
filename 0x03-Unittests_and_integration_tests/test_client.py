#!/usr/bin/env python3
""" Client testing module """

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unittest class for GithubOrgClient
    """

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json', return_value={'organization': 'org'})
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        """
        github_org_client = GithubOrgClient(org_name)

        result = github_org_client.org
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(org_name))
        self.assertEqual(result, {'organization': 'org'})


if __name__ == "__main__":
    unittest.main()
