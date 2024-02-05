#!/usr/bin/env python3
""" Client testing module """

from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict
from unittest.mock import patch, MagicMock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
    Unittest class for GithubOrgClient
    """

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json', return_value={'organization': 'org'})
    def test_org(self, org_name: str, mock_get_json: MagicMock) -> None:
        """
        Test that GithubOrgClient.org returns the correct value
        """
        github_org_client = GithubOrgClient(org_name)

        result = github_org_client.org
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(org_name))
        self.assertEqual(result, {'organization': 'org'})

    @patch(
        'client.get_json',
        return_value={
            'repos_url':
            'https://api.github.com/orgs/test_org/repos'
        }
    )
    def test_public_repos_url(self, mock_get_json: MagicMock) -> None:
        """
        Test that GithubOrgClient._public_repos_url returns the correct
        value
        """
        # Mocking the org method to control its return value
        with patch('client.GithubOrgClient.org', return_value={
                'repos_url': 'https://api.github.com/orgs/test_org/repos'
        }):
            github_org_client = GithubOrgClient('test_org')

        # Ensure that get_json is called with the expected url
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/test_org/repos'
        )

        # Ensure the result of _public_repos_url is as expected
        expected_result: Dict = {
            'repos_url': 'https://api.github.com/orgs/test_org/repos'
        }
        self.assertEqual(github_org_client._public_repos_url,
                         expected_result['repos_url'])


if __name__ == "__main__":
    unittest.main()
