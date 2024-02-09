#!/usr/bin/env python3
""" Client testing module """

from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from parameterized import parameterized, parameterized_class
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

    def test_license(self):
        """
        Tests GithubOrgClient.has_license
        """
        test_cases = [
            ({'license': {'key': 'my_license'}}, 'my_license', True),
            ({'license': {'key': 'other_license'}}, 'my_license', False)
        ]

        for repo, license_key, expected_result in test_cases:
            github_client = GithubOrgClient()
            github_client.get_repo_info = MagicMock(return_value=repo)

            # Test the method a set of parameters
            result = github_client.has_license(license_key)
            self.assertEqual(result, expected_result)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos',
     [(org_payload, repos_payload, expected_repos, apache2_repos)]))
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    An integration test class for the fixtures module
    """
    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class with mock values
        """
        # Patching requests.get to return examples payloads
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Mocking side_effect to return the correct fixtures
        cls.mock_get.side_effect = [
            unittest.mock.MagicMock(json=lambda: cls.org_payload),
            unittest.mock.MagicMock(json=lambda: cls.repos_payload),
            unittest.mock.MagicMock(json=lambda: cls.expected_repos),
            unittest.mock.MagicMock(json=lambda: cls.apache2_repos)
        ]

        @classmethod
        def tearDownClass(cls):
            """
            Tears down the test class and all mock values
            """
            cls.get_patcher.stop()

        def test_public_repos(self):
            """
            Tests integration of public_repos
            """
            github_org_client = GithubOrgClient('test_org')
            repos = github_org_client.public_repos()
            self.assertEqual(repos, self.expected_repos)

        def test_public_repos_with_license(self):
            """
            Test public repos integration with license
            """
            github_org_client = GithubOrgClient('test_org')
            repos = github_org_client.public_repos(license='apache-2.0')
            self.assertEqual(repos, apache2_repos)


if __name__ == "__main__":
    unittest.main()
