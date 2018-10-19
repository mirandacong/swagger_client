# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.label import Label  # noqa: F401,E501
from swagger_client.models.milestone import Milestone  # noqa: F401,E501
from swagger_client.models.pull_request_meta import PullRequestMeta  # noqa: F401,E501
from swagger_client.models.state_type import StateType  # noqa: F401,E501
from swagger_client.models.user import User  # noqa: F401,E501


class Issue(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'assignee': 'User',
        'assignees': 'list[User]',
        'body': 'str',
        'closed_at': 'datetime',
        'comments': 'int',
        'created_at': 'datetime',
        'due_date': 'datetime',
        'id': 'int',
        'labels': 'list[Label]',
        'milestone': 'Milestone',
        'number': 'int',
        'pull_request': 'PullRequestMeta',
        'state': 'StateType',
        'title': 'str',
        'updated_at': 'datetime',
        'url': 'str',
        'user': 'User'
    }

    attribute_map = {
        'assignee': 'assignee',
        'assignees': 'assignees',
        'body': 'body',
        'closed_at': 'closed_at',
        'comments': 'comments',
        'created_at': 'created_at',
        'due_date': 'due_date',
        'id': 'id',
        'labels': 'labels',
        'milestone': 'milestone',
        'number': 'number',
        'pull_request': 'pull_request',
        'state': 'state',
        'title': 'title',
        'updated_at': 'updated_at',
        'url': 'url',
        'user': 'user'
    }

    def __init__(self, assignee=None, assignees=None, body=None, closed_at=None, comments=None, created_at=None, due_date=None, id=None, labels=None, milestone=None, number=None, pull_request=None, state=None, title=None, updated_at=None, url=None, user=None):  # noqa: E501
        """Issue - a model defined in Swagger"""  # noqa: E501

        self._assignee = None
        self._assignees = None
        self._body = None
        self._closed_at = None
        self._comments = None
        self._created_at = None
        self._due_date = None
        self._id = None
        self._labels = None
        self._milestone = None
        self._number = None
        self._pull_request = None
        self._state = None
        self._title = None
        self._updated_at = None
        self._url = None
        self._user = None
        self.discriminator = None

        if assignee is not None:
            self.assignee = assignee
        if assignees is not None:
            self.assignees = assignees
        if body is not None:
            self.body = body
        if closed_at is not None:
            self.closed_at = closed_at
        if comments is not None:
            self.comments = comments
        if created_at is not None:
            self.created_at = created_at
        if due_date is not None:
            self.due_date = due_date
        if id is not None:
            self.id = id
        if labels is not None:
            self.labels = labels
        if milestone is not None:
            self.milestone = milestone
        if number is not None:
            self.number = number
        if pull_request is not None:
            self.pull_request = pull_request
        if state is not None:
            self.state = state
        if title is not None:
            self.title = title
        if updated_at is not None:
            self.updated_at = updated_at
        if url is not None:
            self.url = url
        if user is not None:
            self.user = user

    @property
    def assignee(self):
        """Gets the assignee of this Issue.  # noqa: E501


        :return: The assignee of this Issue.  # noqa: E501
        :rtype: User
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this Issue.


        :param assignee: The assignee of this Issue.  # noqa: E501
        :type: User
        """

        self._assignee = assignee

    @property
    def assignees(self):
        """Gets the assignees of this Issue.  # noqa: E501


        :return: The assignees of this Issue.  # noqa: E501
        :rtype: list[User]
        """
        return self._assignees

    @assignees.setter
    def assignees(self, assignees):
        """Sets the assignees of this Issue.


        :param assignees: The assignees of this Issue.  # noqa: E501
        :type: list[User]
        """

        self._assignees = assignees

    @property
    def body(self):
        """Gets the body of this Issue.  # noqa: E501


        :return: The body of this Issue.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Issue.


        :param body: The body of this Issue.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def closed_at(self):
        """Gets the closed_at of this Issue.  # noqa: E501


        :return: The closed_at of this Issue.  # noqa: E501
        :rtype: datetime
        """
        return self._closed_at

    @closed_at.setter
    def closed_at(self, closed_at):
        """Sets the closed_at of this Issue.


        :param closed_at: The closed_at of this Issue.  # noqa: E501
        :type: datetime
        """

        self._closed_at = closed_at

    @property
    def comments(self):
        """Gets the comments of this Issue.  # noqa: E501


        :return: The comments of this Issue.  # noqa: E501
        :rtype: int
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Issue.


        :param comments: The comments of this Issue.  # noqa: E501
        :type: int
        """

        self._comments = comments

    @property
    def created_at(self):
        """Gets the created_at of this Issue.  # noqa: E501


        :return: The created_at of this Issue.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Issue.


        :param created_at: The created_at of this Issue.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def due_date(self):
        """Gets the due_date of this Issue.  # noqa: E501


        :return: The due_date of this Issue.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Issue.


        :param due_date: The due_date of this Issue.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def id(self):
        """Gets the id of this Issue.  # noqa: E501


        :return: The id of this Issue.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Issue.


        :param id: The id of this Issue.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this Issue.  # noqa: E501


        :return: The labels of this Issue.  # noqa: E501
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Issue.


        :param labels: The labels of this Issue.  # noqa: E501
        :type: list[Label]
        """

        self._labels = labels

    @property
    def milestone(self):
        """Gets the milestone of this Issue.  # noqa: E501


        :return: The milestone of this Issue.  # noqa: E501
        :rtype: Milestone
        """
        return self._milestone

    @milestone.setter
    def milestone(self, milestone):
        """Sets the milestone of this Issue.


        :param milestone: The milestone of this Issue.  # noqa: E501
        :type: Milestone
        """

        self._milestone = milestone

    @property
    def number(self):
        """Gets the number of this Issue.  # noqa: E501


        :return: The number of this Issue.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Issue.


        :param number: The number of this Issue.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def pull_request(self):
        """Gets the pull_request of this Issue.  # noqa: E501


        :return: The pull_request of this Issue.  # noqa: E501
        :rtype: PullRequestMeta
        """
        return self._pull_request

    @pull_request.setter
    def pull_request(self, pull_request):
        """Sets the pull_request of this Issue.


        :param pull_request: The pull_request of this Issue.  # noqa: E501
        :type: PullRequestMeta
        """

        self._pull_request = pull_request

    @property
    def state(self):
        """Gets the state of this Issue.  # noqa: E501


        :return: The state of this Issue.  # noqa: E501
        :rtype: StateType
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Issue.


        :param state: The state of this Issue.  # noqa: E501
        :type: StateType
        """

        self._state = state

    @property
    def title(self):
        """Gets the title of this Issue.  # noqa: E501


        :return: The title of this Issue.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Issue.


        :param title: The title of this Issue.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def updated_at(self):
        """Gets the updated_at of this Issue.  # noqa: E501


        :return: The updated_at of this Issue.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Issue.


        :param updated_at: The updated_at of this Issue.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def url(self):
        """Gets the url of this Issue.  # noqa: E501


        :return: The url of this Issue.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Issue.


        :param url: The url of this Issue.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def user(self):
        """Gets the user of this Issue.  # noqa: E501


        :return: The user of this Issue.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Issue.


        :param user: The user of this Issue.  # noqa: E501
        :type: User
        """

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Issue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
