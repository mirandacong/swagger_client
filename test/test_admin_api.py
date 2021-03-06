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
from swagger_client.api.admin_api import AdminApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.admin_api.AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_create_org(self):
        """Test case for admin_create_org

        Create an organization  # noqa: E501
        """
        pass

    def test_admin_create_public_key(self):
        """Test case for admin_create_public_key

        Add a public key on behalf of a user  # noqa: E501
        """
        pass

    def test_admin_create_repo(self):
        """Test case for admin_create_repo

        Create a repository on behalf a user  # noqa: E501
        """
        pass

    def test_admin_create_user(self):
        """Test case for admin_create_user

        Create a user  # noqa: E501
        """
        pass

    def test_admin_delete_user(self):
        """Test case for admin_delete_user

        Delete a user  # noqa: E501
        """
        pass

    def test_admin_delete_user_public_key(self):
        """Test case for admin_delete_user_public_key

        Delete a user's public key  # noqa: E501
        """
        pass

    def test_admin_edit_user(self):
        """Test case for admin_edit_user

        Edit an existing user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
