# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.organization_api import OrganizationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.organization_api.OrganizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_org_repo(self):
        """Test case for create_org_repo

        Create a repository in an organization  # noqa: E501
        """
        pass

    def test_org_add_team_member(self):
        """Test case for org_add_team_member

        Add a team member  # noqa: E501
        """
        pass

    def test_org_add_team_repository(self):
        """Test case for org_add_team_repository

        Add a repository to a team  # noqa: E501
        """
        pass

    def test_org_conceal_member(self):
        """Test case for org_conceal_member

        Conceal a user's membership  # noqa: E501
        """
        pass

    def test_org_create_hook(self):
        """Test case for org_create_hook

        Create a hook  # noqa: E501
        """
        pass

    def test_org_create_team(self):
        """Test case for org_create_team

        Create a team  # noqa: E501
        """
        pass

    def test_org_delete_hook(self):
        """Test case for org_delete_hook

        Delete a hook  # noqa: E501
        """
        pass

    def test_org_delete_member(self):
        """Test case for org_delete_member

        Remove a member from an organization  # noqa: E501
        """
        pass

    def test_org_delete_team(self):
        """Test case for org_delete_team

        Delete a team  # noqa: E501
        """
        pass

    def test_org_edit(self):
        """Test case for org_edit

        Edit an organization  # noqa: E501
        """
        pass

    def test_org_edit_hook(self):
        """Test case for org_edit_hook

        Update a hook  # noqa: E501
        """
        pass

    def test_org_edit_team(self):
        """Test case for org_edit_team

        Edit a team  # noqa: E501
        """
        pass

    def test_org_get(self):
        """Test case for org_get

        Get an organization  # noqa: E501
        """
        pass

    def test_org_get_hook(self):
        """Test case for org_get_hook

        Get a hook  # noqa: E501
        """
        pass

    def test_org_get_team(self):
        """Test case for org_get_team

        Get a team  # noqa: E501
        """
        pass

    def test_org_is_member(self):
        """Test case for org_is_member

        Check if a user is a member of an organization  # noqa: E501
        """
        pass

    def test_org_is_public_member(self):
        """Test case for org_is_public_member

        Check if a user is a public member of an organization  # noqa: E501
        """
        pass

    def test_org_list_current_user_orgs(self):
        """Test case for org_list_current_user_orgs

        List the current user's organizations  # noqa: E501
        """
        pass

    def test_org_list_hooks(self):
        """Test case for org_list_hooks

        List an organization's webhooks  # noqa: E501
        """
        pass

    def test_org_list_members(self):
        """Test case for org_list_members

        List an organization's members  # noqa: E501
        """
        pass

    def test_org_list_public_members(self):
        """Test case for org_list_public_members

        List an organization's public members  # noqa: E501
        """
        pass

    def test_org_list_repos(self):
        """Test case for org_list_repos

        List an organization's repos  # noqa: E501
        """
        pass

    def test_org_list_team_members(self):
        """Test case for org_list_team_members

        List a team's members  # noqa: E501
        """
        pass

    def test_org_list_team_repos(self):
        """Test case for org_list_team_repos

        List a team's repos  # noqa: E501
        """
        pass

    def test_org_list_teams(self):
        """Test case for org_list_teams

        List an organization's teams  # noqa: E501
        """
        pass

    def test_org_list_user_orgs(self):
        """Test case for org_list_user_orgs

        List a user's organizations  # noqa: E501
        """
        pass

    def test_org_publicize_member(self):
        """Test case for org_publicize_member

        Publicize a user's membership  # noqa: E501
        """
        pass

    def test_org_remove_team_member(self):
        """Test case for org_remove_team_member

        Remove a team member  # noqa: E501
        """
        pass

    def test_org_remove_team_repository(self):
        """Test case for org_remove_team_repository

        Remove a repository from a team  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
