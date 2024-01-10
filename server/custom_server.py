#!/usr/bin/env python3

__author__ = "Jaime Zelada"
__copyright__ = "Copyright 2023, Kinect Consulting"
__license__ = "Commercial"
__email__ = "jzelada@kinect-consulting.com"

import logging
import json
import pprint

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.managementgroups import ManagementGroupsAPI
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.mgmt.loganalytics import LogAnalyticsManagementClient
from azure.mgmt.resource.policy import PolicyClient
from azure.graphrbac import GraphRbacManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from msgraph.core import GraphClient 
from azure.identity import ClientSecretCredential

# import module
import traceback
import os

logger = logging.getLogger("server")
logger.setLevel(logging.INFO)

def pp(d):
    print(pprint.pformat(d))


def get_resource_groups(params):
    # Acquire a credential object using CLI-based authentication.
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    credential = DefaultAzureCredential()
    resource_client = ResourceManagementClient(credential, subscription_id)
    group_list = resource_client.resource_groups.list()
    resource_groups = []
    sorted_entities = sorted(group_list, key=lambda x: x.name.lower(), reverse=False)
    rc_rgs = list(filter(lambda x: x.tags is not None and x.tags.get('profile') is not None and x.tags.get('profile') == params.get('env') ,sorted_entities))
    other_rgs = list(filter((lambda x: x.tags is None) ,sorted_entities))
    additional_rgs = list(filter((lambda x: x.tags is not None and x.tags.get('profile') is None) ,sorted_entities))

    final_list = rc_rgs + other_rgs + additional_rgs
    
    # for item in list(final_list):
    #     print(item.name)

    #sorted_entities = sorted(group_list, key=lambda x: x.name.lower(), reverse=False)
    for group in list(final_list):
        output_dict = {}
        is_rc = ""
        if not group.tags:
            label = f"{group.name} ({group.location})"
        else:
            if group.tags is not None:
                if group.tags.get('profile') is not None:
                    if group.tags.get('profile').lower() == params.get('env').lower():
                        is_rc = "value"
            if is_rc == '':
                label = f"{group.name} ({group.location})"
            else:
                label = f"{group.name} ({group.location}) (Managed by Rapid Cloud)"
        output_dict['value'] = {}
        output_dict['type'] = "Theia::Option"
        output_dict['label'] = label
        output_dict['value']['type'] = "Theia::DataOption"
        output_dict['value']['value'] = group.name
        output_dict['value']['scope'] = group.id
        resource_groups.append(output_dict)
    return resource_groups

def get_management_groups():
    # Acquire a credential object using CLI-based authentication.
    credential = DefaultAzureCredential()

    mgmt_groups_api = ManagementGroupsAPI(credential)
    entities = mgmt_groups_api.entities.list()

    mgmt_groups = []

    for group in list(entities):
        if group.type == "Microsoft.Management/managementGroups":
            output_dict = {}
            label = f"{group.display_name} ({group.name})"
            output_dict['value'] = {}
            output_dict['type'] = "Theia::Option"
            output_dict['label'] = label
            output_dict['value']['type'] = "Theia::DataOption"
            output_dict['value']['value'] = group.name
            output_dict['value']['scope'] = group.id
            mgmt_groups.append(output_dict)
        
        

    return mgmt_groups

def get_subscription_ids():
    # Acquire a credential object using CLI-based authentication.
    credential = DefaultAzureCredential()

    subs_client = SubscriptionClient(credential)
    entities = subs_client.subscriptions.list()

    subscriptions = []

    for group in list(entities):
        output_dict = {}
        label = f"{group.display_name} ({group.subscription_id})"
        output_dict['value'] = {}
        output_dict['type'] = "Theia::Option"
        output_dict['label'] = label
        output_dict['value']['type'] = "Theia::DataOption"
        output_dict['value']['value'] = group.subscription_id
        output_dict['value']['scope'] = group.id
        subscriptions.append(output_dict)
    return subscriptions

def get_key_vaults():
    # Acquire a credential object using CLI-based authentication.
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    credential = DefaultAzureCredential()

    kv_client = KeyVaultManagementClient(credential,subscription_id)
    entities = kv_client.vaults.list()

    vaults = []

    for vault in list(entities):
        output_dict = {}
        label = f"{vault.name}"
        output_dict['value'] = {}
        output_dict['type'] = "Theia::Option"
        output_dict['label'] = label
        output_dict['value']['type'] = "Theia::DataOption"
        output_dict['value']['value'] = vault.name
        vaults.append(output_dict)
    return vaults

def get_log_workspaces():
    # Acquire a credential object using CLI-based authentication.
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    credential = DefaultAzureCredential()

    log_client = LogAnalyticsManagementClient(credential,subscription_id)
    entities = log_client.workspaces.list()

    workspaces = []

    for workspace in list(entities):
        output_dict = {}
        label = f"{workspace.name}"
        output_dict['value'] = {}
        output_dict['type'] = "Theia::Option"
        output_dict['label'] = label
        output_dict['value']['type'] = "Theia::DataOption"
        output_dict['value']['value'] = workspace.name
        workspaces.append(output_dict)
    return workspaces

def get_locations():
    # Acquire a credential object using CLI-based authentication.
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    credential = DefaultAzureCredential()

    subs_client = SubscriptionClient(credential)
    entities = subs_client.subscriptions.list_locations(subscription_id)

    locations = []

    for location in list(entities):
        output_dict = {}
        label = f"{location.display_name}"
        output_dict['value'] = {}
        output_dict['type'] = "Theia::Option"
        output_dict['label'] = label
        output_dict['value']['type'] = "Theia::DataOption"
        output_dict['value']['value'] = location.name
        locations.append(output_dict)
    return locations

def get_policies(params):
    # Acquire a credential object using CLI-based authentication.
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    credential = DefaultAzureCredential()
    # print(params.get('policy_type'))
    policy_client = PolicyClient(credential,subscription_id)
    # if params.get('policy_type') == "builtin":
    #     entities = policy_client.policy_definitions.list_built_in()
    # else:
    entities = policy_client.policy_definitions.list()
    sorted_entities = sorted(entities, key=lambda x: x.display_name.lower(), reverse=False)
    policies = []

    for policy in list(sorted_entities):
        output_dict = {}

        label = f"{policy.display_name} (Managed by Rapid Cloud)" if policy.policy_type.lower() == "custom" else f"{policy.display_name}"
        output_dict['value'] = {}
        output_dict['type'] = "Theia::Option"
        output_dict['label'] = label
        output_dict['value']['type'] = "Theia::DataOption"
        output_dict['value']['value'] = policy.id
        policies.append(output_dict)
    return policies

def get_object_ids():
    # Acquire a credential object using CLI-based authentication.
    try:
        credential = ClientSecretCredential(client_id=os.environ["AZURE_CLIENT_ID"],client_secret=os.environ["AZURE_CLIENT_SECRET"],tenant_id=os.environ["AZURE_TENANT_ID"])
        graph_client = GraphClient(credential=credential)
        users = graph_client.get('/users?$select=displayName,id')
        service_principal = graph_client.get('/applications?$select=displayName,id')
        entities_users = json.dumps(users.json())
        ent_users = json.loads(entities_users)
        entities_sps = json.dumps(service_principal.json())
        ent_sps = json.loads(entities_sps)

    except Exception as e:
        traceback.print_exc()
    #For the users 
    users = []
    for user in list(ent_users.get('value')):
        output_dict = {}
        #print(user.get('displayName'))
        label = f"{user.get('displayName')}"
        output_dict['value'] = {}
        output_dict['type'] = "Theia::Option"
        output_dict['label'] = label
        output_dict['value']['type'] = "Theia::DataOption"
        output_dict['value']['value'] = user.get('id')
        users.append(output_dict)
    #For the applications
    for user in list(ent_sps.get('value')):
        output_dict = {}
        #print(user.get('displayName'))
        label = f"{user.get('displayName')}"
        output_dict['value'] = {}
        output_dict['type'] = "Theia::Option"
        output_dict['label'] = label
        output_dict['value']['type'] = "Theia::DataOption"
        output_dict['value']['value'] = user.get('id')
        users.append(output_dict)
    return users

def get_assignable_scopes(params):

    mgmt_groups = switch_value(get_management_groups())
    mgmt_groups = sorted(mgmt_groups, key=lambda x: x.get('label').lower(), reverse=False)
    subscriptions = switch_value(get_subscription_ids())
    subscriptions = sorted(subscriptions, key=lambda x: x.get('label').lower(), reverse=False)
    resource_groups = switch_value(get_resource_groups(params))
    resources = get_resource_group_resources(params)
    resources = sorted(resources, key=lambda x: x.get('label').lower(), reverse=False)
    assignable_scopes = mgmt_groups + subscriptions + resource_groups + resources
    return assignable_scopes


def get_resource_group_resources(params):

    resource_groups = get_resource_groups(params)
    resources = []
    for group in list(resource_groups):
        subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
        credential = DefaultAzureCredential()
        resource_client = ResourceManagementClient(credential, subscription_id)
        resources_list = resource_client.resources.list_by_resource_group(group.get('value').get('value'))

        for resource in list(resources_list):
            output_dict = {}
            label = f"{resource.name} ({resource.type})"
            output_dict['value'] = {}
            output_dict['type'] = "Theia::Option"
            output_dict['label'] = label
            output_dict['value']['type'] = "Theia::DataOption"
            output_dict['value']['value'] = resource.id
            output_dict['value']['scope'] = resource.id
            resources.append(output_dict)

    return resources

def switch_value(input):
    switched = []

    for item in input:
        item['value']['value'] = item['value']['scope']
        switched.append(item)
    return switched


def custom_endpoint(action, params, boto3_session, user_session):
    if action == "resource_groups":
        return get_resource_groups(params)
    elif action == "management_groups":
        return get_management_groups()
    elif action == "subscription_ids":
        return get_subscription_ids()   
    elif action == "key_vaults":
        return get_key_vaults()  
    elif action == "log_workspaces":
        return get_log_workspaces() 
    elif action == "locations":
        return get_locations()
    elif action == "policies":
        return get_policies(params)  
    elif action == "assignable_scopes":
        return get_assignable_scopes(params)  
    elif action == "users":
        return get_object_ids()
    else:
        pp(f"no such endpoint: {action}")
        return ["no such endpoint"]

    return []
