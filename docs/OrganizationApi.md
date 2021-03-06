# swagger_client.OrganizationApi

All URIs are relative to *http://localhost{{AppSubUrl}}/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_org_repo**](OrganizationApi.md#create_org_repo) | **POST** /org/{org}/repos | Create a repository in an organization
[**org_add_team_member**](OrganizationApi.md#org_add_team_member) | **PUT** /teams/{id}/members/{username} | Add a team member
[**org_add_team_repository**](OrganizationApi.md#org_add_team_repository) | **PUT** /teams/{id}/repos/{org}/{repo} | Add a repository to a team
[**org_conceal_member**](OrganizationApi.md#org_conceal_member) | **DELETE** /orgs/{org}/public_members/{username} | Conceal a user&#39;s membership
[**org_create_hook**](OrganizationApi.md#org_create_hook) | **POST** /orgs/{org}/hooks/ | Create a hook
[**org_create_team**](OrganizationApi.md#org_create_team) | **POST** /orgs/{org}/teams | Create a team
[**org_delete_hook**](OrganizationApi.md#org_delete_hook) | **DELETE** /orgs/{org}/hooks/{id} | Delete a hook
[**org_delete_member**](OrganizationApi.md#org_delete_member) | **DELETE** /orgs/{org}/members/{username} | Remove a member from an organization
[**org_delete_team**](OrganizationApi.md#org_delete_team) | **DELETE** /teams/{id} | Delete a team
[**org_edit**](OrganizationApi.md#org_edit) | **PATCH** /orgs/{org} | Edit an organization
[**org_edit_hook**](OrganizationApi.md#org_edit_hook) | **PATCH** /orgs/{org}/hooks/{id} | Update a hook
[**org_edit_team**](OrganizationApi.md#org_edit_team) | **PATCH** /teams/{id} | Edit a team
[**org_get**](OrganizationApi.md#org_get) | **GET** /orgs/{org} | Get an organization
[**org_get_hook**](OrganizationApi.md#org_get_hook) | **GET** /orgs/{org}/hooks/{id} | Get a hook
[**org_get_team**](OrganizationApi.md#org_get_team) | **GET** /teams/{id} | Get a team
[**org_is_member**](OrganizationApi.md#org_is_member) | **GET** /orgs/{org}/members/{username} | Check if a user is a member of an organization
[**org_is_public_member**](OrganizationApi.md#org_is_public_member) | **GET** /orgs/{org}/public_members/{username} | Check if a user is a public member of an organization
[**org_list_current_user_orgs**](OrganizationApi.md#org_list_current_user_orgs) | **GET** /user/orgs | List the current user&#39;s organizations
[**org_list_hooks**](OrganizationApi.md#org_list_hooks) | **GET** /orgs/{org}/hooks | List an organization&#39;s webhooks
[**org_list_members**](OrganizationApi.md#org_list_members) | **GET** /orgs/{org}/members | List an organization&#39;s members
[**org_list_public_members**](OrganizationApi.md#org_list_public_members) | **GET** /orgs/{org}/public_members | List an organization&#39;s public members
[**org_list_repos**](OrganizationApi.md#org_list_repos) | **GET** /orgs/{org}/repos | List an organization&#39;s repos
[**org_list_team_members**](OrganizationApi.md#org_list_team_members) | **GET** /teams/{id}/members | List a team&#39;s members
[**org_list_team_repos**](OrganizationApi.md#org_list_team_repos) | **GET** /teams/{id}/repos | List a team&#39;s repos
[**org_list_teams**](OrganizationApi.md#org_list_teams) | **GET** /orgs/{org}/teams | List an organization&#39;s teams
[**org_list_user_orgs**](OrganizationApi.md#org_list_user_orgs) | **GET** /user/{username}/orgs | List a user&#39;s organizations
[**org_publicize_member**](OrganizationApi.md#org_publicize_member) | **PUT** /orgs/{org}/public_members/{username} | Publicize a user&#39;s membership
[**org_remove_team_member**](OrganizationApi.md#org_remove_team_member) | **DELETE** /teams/{id}/members/{username} | Remove a team member
[**org_remove_team_repository**](OrganizationApi.md#org_remove_team_repository) | **DELETE** /teams/{id}/repos/{org}/{repo} | Remove a repository from a team


# **create_org_repo**
> Repository create_org_repo(org, body=body)

Create a repository in an organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of organization
body = swagger_client.CreateRepoOption() # CreateRepoOption |  (optional)

try:
    # Create a repository in an organization
    api_response = api_instance.create_org_repo(org, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->create_org_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of organization | 
 **body** | [**CreateRepoOption**](CreateRepoOption.md)|  | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_add_team_member**
> org_add_team_member(id, username)

Add a team member

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
id = 56 # int | id of the team
username = 'username_example' # str | username of the user to add

try:
    # Add a team member
    api_instance.org_add_team_member(id, username)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_add_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **username** | **str**| username of the user to add | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_add_team_repository**
> org_add_team_repository(id, org, repo)

Add a repository to a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
id = 56 # int | id of the team
org = 'org_example' # str | organization that owns the repo to add
repo = 'repo_example' # str | name of the repo to add

try:
    # Add a repository to a team
    api_instance.org_add_team_repository(id, org, repo)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_add_team_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **org** | **str**| organization that owns the repo to add | 
 **repo** | **str**| name of the repo to add | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_conceal_member**
> org_conceal_member(org, username)

Conceal a user's membership

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization
username = 'username_example' # str | username of the user

try:
    # Conceal a user's membership
    api_instance.org_conceal_member(org, username)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_conceal_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| username of the user | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_create_hook**
> list[Branch] org_create_hook(org)

Create a hook

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization

try:
    # Create a hook
    api_response = api_instance.org_create_hook(org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_create_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 

### Return type

[**list[Branch]**](Branch.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_create_team**
> Team org_create_team(org, body=body)

Create a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization
body = swagger_client.CreateTeamOption() # CreateTeamOption |  (optional)

try:
    # Create a team
    api_response = api_instance.org_create_team(org, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **body** | [**CreateTeamOption**](CreateTeamOption.md)|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_delete_hook**
> org_delete_hook(org, id)

Delete a hook

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization
id = 56 # int | id of the hook to delete

try:
    # Delete a hook
    api_instance.org_delete_hook(org, id)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_delete_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **id** | **int**| id of the hook to delete | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_delete_member**
> Responsesempty org_delete_member(org, username)

Remove a member from an organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization
username = 'username_example' # str | username of the user

try:
    # Remove a member from an organization
    api_response = api_instance.org_delete_member(org, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_delete_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| username of the user | 

### Return type

[**Responsesempty**](Responsesempty.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_delete_team**
> Responsesempty org_delete_team(id)

Delete a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
id = 56 # int | id of the team to delete

try:
    # Delete a team
    api_response = api_instance.org_delete_team(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_delete_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team to delete | 

### Return type

[**Responsesempty**](Responsesempty.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_edit**
> Organization org_edit(org, body=body)

Edit an organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization to edit
body = swagger_client.EditOrgOption() # EditOrgOption |  (optional)

try:
    # Edit an organization
    api_response = api_instance.org_edit(org, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization to edit | 
 **body** | [**EditOrgOption**](EditOrgOption.md)|  | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_edit_hook**
> list[Branch] org_edit_hook(org, id)

Update a hook

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization
id = 56 # int | id of the hook to update

try:
    # Update a hook
    api_response = api_instance.org_edit_hook(org, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_edit_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **id** | **int**| id of the hook to update | 

### Return type

[**list[Branch]**](Branch.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_edit_team**
> Team org_edit_team(id, body=body)

Edit a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
id = 56 # int | id of the team to edit
body = swagger_client.EditTeamOption() # EditTeamOption |  (optional)

try:
    # Edit a team
    api_response = api_instance.org_edit_team(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_edit_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team to edit | 
 **body** | [**EditTeamOption**](EditTeamOption.md)|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_get**
> Organization org_get(org)

Get an organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization to get

try:
    # Get an organization
    api_response = api_instance.org_get(org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization to get | 

### Return type

[**Organization**](Organization.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_get_hook**
> list[Branch] org_get_hook(org, id)

Get a hook

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization
id = 56 # int | id of the hook to get

try:
    # Get a hook
    api_response = api_instance.org_get_hook(org, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_get_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **id** | **int**| id of the hook to get | 

### Return type

[**list[Branch]**](Branch.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_get_team**
> Team org_get_team(id)

Get a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
id = 56 # int | id of the team to get

try:
    # Get a team
    api_response = api_instance.org_get_team(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team to get | 

### Return type

[**Team**](Team.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_is_member**
> Responsesempty org_is_member(org, username)

Check if a user is a member of an organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization
username = 'username_example' # str | username of the user

try:
    # Check if a user is a member of an organization
    api_response = api_instance.org_is_member(org, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_is_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| username of the user | 

### Return type

[**Responsesempty**](Responsesempty.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_is_public_member**
> Responsesempty org_is_public_member(org, username)

Check if a user is a public member of an organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization
username = 'username_example' # str | username of the user

try:
    # Check if a user is a public member of an organization
    api_response = api_instance.org_is_public_member(org, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_is_public_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| username of the user | 

### Return type

[**Responsesempty**](Responsesempty.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_current_user_orgs**
> list[Organization] org_list_current_user_orgs()

List the current user's organizations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))

try:
    # List the current user's organizations
    api_response = api_instance.org_list_current_user_orgs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_list_current_user_orgs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Organization]**](Organization.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_hooks**
> list[Branch] org_list_hooks(org)

List an organization's webhooks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization

try:
    # List an organization's webhooks
    api_response = api_instance.org_list_hooks(org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_list_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 

### Return type

[**list[Branch]**](Branch.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_members**
> list[User] org_list_members(org)

List an organization's members

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization

try:
    # List an organization's members
    api_response = api_instance.org_list_members(org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_list_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 

### Return type

[**list[User]**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_public_members**
> list[User] org_list_public_members(org)

List an organization's public members

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization

try:
    # List an organization's public members
    api_response = api_instance.org_list_public_members(org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_list_public_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 

### Return type

[**list[User]**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_repos**
> list[Repository] org_list_repos(org)

List an organization's repos

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization

try:
    # List an organization's repos
    api_response = api_instance.org_list_repos(org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_list_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_team_members**
> list[User] org_list_team_members(id)

List a team's members

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
id = 56 # int | id of the team

try:
    # List a team's members
    api_response = api_instance.org_list_team_members(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_list_team_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 

### Return type

[**list[User]**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_team_repos**
> list[Repository] org_list_team_repos(id)

List a team's repos

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
id = 56 # int | id of the team

try:
    # List a team's repos
    api_response = api_instance.org_list_team_repos(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_list_team_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_teams**
> list[Team] org_list_teams(org)

List an organization's teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization

try:
    # List an organization's teams
    api_response = api_instance.org_list_teams(org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_list_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 

### Return type

[**list[Team]**](Team.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_user_orgs**
> list[Organization] org_list_user_orgs(username)

List a user's organizations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str | username of user

try:
    # List a user's organizations
    api_response = api_instance.org_list_user_orgs(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_list_user_orgs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user | 

### Return type

[**list[Organization]**](Organization.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_publicize_member**
> Responsesempty org_publicize_member(org, username)

Publicize a user's membership

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
org = 'org_example' # str | name of the organization
username = 'username_example' # str | username of the user

try:
    # Publicize a user's membership
    api_response = api_instance.org_publicize_member(org, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_publicize_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| username of the user | 

### Return type

[**Responsesempty**](Responsesempty.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_remove_team_member**
> org_remove_team_member(id, username)

Remove a team member

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
id = 56 # int | id of the team
username = 'username_example' # str | username of the user to remove

try:
    # Remove a team member
    api_instance.org_remove_team_member(id, username)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_remove_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **username** | **str**| username of the user to remove | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_remove_team_repository**
> org_remove_team_repository(id, org, repo)

Remove a repository from a team

This does not delete the repository, it only removes the repository from the team.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = swagger_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = swagger_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationApi(swagger_client.ApiClient(configuration))
id = 56 # int | id of the team
org = 'org_example' # str | organization that owns the repo to remove
repo = 'repo_example' # str | name of the repo to remove

try:
    # Remove a repository from a team
    api_instance.org_remove_team_repository(id, org, repo)
except ApiException as e:
    print("Exception when calling OrganizationApi->org_remove_team_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **org** | **str**| organization that owns the repo to remove | 
 **repo** | **str**| name of the repo to remove | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

