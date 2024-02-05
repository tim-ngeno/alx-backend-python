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

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=unittest.mock.PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test GithubOrgClient.public_repos method
        """
        # Mocking the get_json method to return a payload
        mock_get_json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]

        # Instantiate GithubOrgClient
        github_org_client = GithubOrgClient('example_org')

        # Call the public_repos method
        repos = github_org_client.public_repos()

        # Assert that the method returned the expected repos
        self.assertEqual(repos, ['repo1', 'repo2'])

        # Assert that the mocked property and get_json were called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            mock_public_repos_url.return_value)


if __name__ == "__main__":
    unittest.main()
