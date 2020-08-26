# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.testsdk.checkers import JMESPathCheck, JMESPathCheckExists


# EXAMPLE: /HostPools/get/HostPool_List
def step__hostpools_get_hostpool_list(test, rg):
    test.cmd('az desktopvirtualization hostpool list '
             '-g ""',
             checks=[
                 JMESPathCheckExists('[?name==\'{}\']'.format(
                     test.kwargs["myHostPool"])),
             ])


# EXAMPLE: /ApplicationGroups/put/ApplicationGroup_Create
def step__applicationgroups_put_applicationgroup_create(test, rg):
    test.cmd('az desktopvirtualization applicationgroup create '
             '--location "centralus" '
             '--description "des1" '
             '--application-group-type "RemoteApp" '
             '--friendly-name "friendly" '
             '--host-pool-arm-path "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.DesktopVir'
             'tualization/hostPools/{myHostPool}" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myApplicationGroup}" '
             '--resource-group "{rg}"',
             checks=[
                 JMESPathCheck('name', test.kwargs["myApplicationGroup"]),
                 JMESPathCheck('tags.tag1', 'value1'),
                 JMESPathCheck('tags.tag2', 'value2'),
             ])


# EXAMPLE: /ApplicationGroups/get/ApplicationGroup_ListByResourceGroup
def step__applicationgroups_get_applicationgroup_listbyresourcegroup(test, rg):
    test.cmd('az desktopvirtualization applicationgroup list '
             '--filter "applicationGroupType eq \'RailApplication\'" '
             '--resource-group "{rg}"',
             checks=[
                 JMESPathCheckExists('[?name==\'{}\']'.format(
                     test.kwargs["myApplicationGroup"])),
             ])


# EXAMPLE: /ApplicationGroups/patch/ApplicationGroups_Update
def step__applicationgroups_patch_applicationgroups_update(test, rg):
    test.cmd('az desktopvirtualization applicationgroup update '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--tags tag1="value3" tag2="value4" '
             '--name "{myApplicationGroup}" '
             '--resource-group "{rg}"',
             checks=[
                 JMESPathCheck('name', test.kwargs["myApplicationGroup"]),
                 JMESPathCheck('tags.tag1', 'value3'),
                 JMESPathCheck('tags.tag2', 'value4'),
             ])


# EXAMPLE: /Workspaces/put/Workspace_Create
def step__workspaces_put_workspace_create(test, rg):
    test.cmd('az desktopvirtualization workspace create '
             '--resource-group "{rg}" '
             '--location "centralus" '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myWorkspace}"',
             checks=[
                 JMESPathCheck('name', test.kwargs["myWorkspace"]),
                 JMESPathCheck('tags.tag1', 'value1'),
                 JMESPathCheck('tags.tag2', 'value2'),
             ])


# EXAMPLE: /Workspaces/get/Workspace_Get
def step__workspaces_get_workspace_get(test, rg):
    test.cmd('az desktopvirtualization workspace show '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}"',
             checks=[
                 JMESPathCheck('name', test.kwargs["myWorkspace"]),
             ])


# EXAMPLE: /Workspaces/patch/Workspace_Update
def step__workspaces_patch_workspace_update(test, rg):
    test.cmd('az desktopvirtualization workspace update '
             '--resource-group "{rg}" '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--tags tag1="value3" tag2="value4" '
             '--name "{myWorkspace}"',
             checks=[
                 JMESPathCheck('name', test.kwargs["myWorkspace"]),
                 JMESPathCheck('tags.tag1', 'value3'),
                 JMESPathCheck('tags.tag2', 'value4'),
             ])

def call_scenario(test, rg):
    from ....tests.latest import test_desktopvirtualization_scenario as g
    g.setup(test, rg)
    g.step__hostpools_put_hostpool_create(test, rg)
    g.step__hostpools_get_hostpool_get(test, rg)
    g.step__hostpools_get_hostpool_list(test, rg)
    g.step__hostpools_get_hostpool_listbyresourcegroup(test, rg)
    g.step__hostpools_patch_hostpool_update(test, rg)
    g.step__workspaces_put_workspace_create(test, rg)
    g.step__workspaces_get_workspace_get(test, rg)
    g.step__workspaces_get_workspace_listbyresourcegroup(test, rg)
    g.step__workspaces_get_workspace_listbysubscription(test, rg)
    g.step__workspaces_patch_workspace_update(test, rg)
    g.step__hostpools_delete_hostpool_delete(test, rg)
    g.step__workspaces_delete_workspace_delete(test, rg)
    g.cleanup(test, rg)