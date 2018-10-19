# coding: utf-8

# flake8: noqa

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.admin_api import AdminApi
from swagger_client.api.issue_api import IssueApi
from swagger_client.api.miscellaneous_api import MiscellaneousApi
from swagger_client.api.organization_api import OrganizationApi
from swagger_client.api.repository_api import RepositoryApi
from swagger_client.api.user_api import UserApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.add_collaborator_option import AddCollaboratorOption
from swagger_client.models.add_time_option import AddTimeOption
from swagger_client.models.attachment import Attachment
from swagger_client.models.branch import Branch
from swagger_client.models.comment import Comment
from swagger_client.models.create_email_option import CreateEmailOption
from swagger_client.models.create_fork_option import CreateForkOption
from swagger_client.models.create_gpg_key_option import CreateGPGKeyOption
from swagger_client.models.create_hook_option import CreateHookOption
from swagger_client.models.create_issue_comment_option import CreateIssueCommentOption
from swagger_client.models.create_issue_option import CreateIssueOption
from swagger_client.models.create_key_option import CreateKeyOption
from swagger_client.models.create_label_option import CreateLabelOption
from swagger_client.models.create_milestone_option import CreateMilestoneOption
from swagger_client.models.create_org_option import CreateOrgOption
from swagger_client.models.create_pull_request_option import CreatePullRequestOption
from swagger_client.models.create_release_option import CreateReleaseOption
from swagger_client.models.create_repo_option import CreateRepoOption
from swagger_client.models.create_status_option import CreateStatusOption
from swagger_client.models.create_team_option import CreateTeamOption
from swagger_client.models.create_user_option import CreateUserOption
from swagger_client.models.delete_email_option import DeleteEmailOption
from swagger_client.models.deploy_key import DeployKey
from swagger_client.models.edit_attachment_options import EditAttachmentOptions
from swagger_client.models.edit_deadline_option import EditDeadlineOption
from swagger_client.models.edit_hook_option import EditHookOption
from swagger_client.models.edit_issue_comment_option import EditIssueCommentOption
from swagger_client.models.edit_issue_option import EditIssueOption
from swagger_client.models.edit_label_option import EditLabelOption
from swagger_client.models.edit_milestone_option import EditMilestoneOption
from swagger_client.models.edit_org_option import EditOrgOption
from swagger_client.models.edit_pull_request_option import EditPullRequestOption
from swagger_client.models.edit_release_option import EditReleaseOption
from swagger_client.models.edit_team_option import EditTeamOption
from swagger_client.models.edit_user_option import EditUserOption
from swagger_client.models.email import Email
from swagger_client.models.gpg_key import GPGKey
from swagger_client.models.gpg_key_email import GPGKeyEmail
from swagger_client.models.inline_response_200 import InlineResponse200
from swagger_client.models.issue import Issue
from swagger_client.models.issue_deadline import IssueDeadline
from swagger_client.models.issue_labels_option import IssueLabelsOption
from swagger_client.models.label import Label
from swagger_client.models.markdown_option import MarkdownOption
from swagger_client.models.migrate_repo_form import MigrateRepoForm
from swagger_client.models.milestone import Milestone
from swagger_client.models.organization import Organization
from swagger_client.models.pr_branch_info import PRBranchInfo
from swagger_client.models.payload_commit import PayloadCommit
from swagger_client.models.payload_commit_verification import PayloadCommitVerification
from swagger_client.models.payload_user import PayloadUser
from swagger_client.models.permission import Permission
from swagger_client.models.public_key import PublicKey
from swagger_client.models.pull_request import PullRequest
from swagger_client.models.pull_request_meta import PullRequestMeta
from swagger_client.models.release import Release
from swagger_client.models.repository import Repository
from swagger_client.models.search_results import SearchResults
from swagger_client.models.server_version import ServerVersion
from swagger_client.models.state_type import StateType
from swagger_client.models.status import Status
from swagger_client.models.status_state import StatusState
from swagger_client.models.team import Team
from swagger_client.models.tracked_time import TrackedTime
from swagger_client.models.user import User
from swagger_client.models.watch_info import WatchInfo
