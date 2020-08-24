# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_three_state_flag,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_desktopvirtualization.action import (
    AddDesktopvirtualizationHostpoolCreateRegistrationInfo,
    AddDesktopvirtualizationHostpoolUpdateRegistrationInfo
)


def load_arguments(self, _):

    with self.argument_context('desktopvirtualization hostpool create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('host_pool_name', options_list=['--name', '-n', '--host-pool-name'], type=str, help='The name of '
                   'the host pool within the specified resource group. Swagger name=hostPoolName')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('friendly_name', type=str, help='Friendly name of HostPool. Swagger name=friendlyName')
        c.argument('description', type=str, help='Description of HostPool. Swagger name=description')
        c.argument('host_pool_type', arg_type=get_enum_type(['Personal', 'Pooled']), help='HostPool type for desktop. '
                   'Swagger name=hostPoolType')
        c.argument('personal_desktop_assignment_type', arg_type=get_enum_type(['Automatic', 'Direct']), help=''
                   'PersonalDesktopAssignment type for HostPool. Swagger name=personalDesktopAssignmentType')
        c.argument('custom_rdp_property', type=str, help='Custom rdp property of HostPool. Swagger '
                   'name=customRdpProperty')
        c.argument('max_session_limit', type=int, help='The max session limit of HostPool. Swagger '
                   'name=maxSessionLimit')
        c.argument('load_balancer_type', arg_type=get_enum_type(['BreadthFirst', 'DepthFirst', 'Persistent']), help=''
                   'The type of the load balancer. Swagger name=loadBalancerType')
        c.argument('ring', type=int, help='The ring number of HostPool. Swagger name=ring')
        c.argument('validation_environment', arg_type=get_three_state_flag(), help='Is validation environment. Swagger '
                   'name=validationEnvironment')
        c.argument('registration_info', action=AddDesktopvirtualizationHostpoolCreateRegistrationInfo, nargs='*',
                   help='The registration info of HostPool. Swagger name=registrationInfo')
        c.argument('vm_template', type=str, help='VM template for sessionhosts configuration within hostpool. Swagger '
                   'name=vmTemplate')
        c.argument('sso_context', type=str, help='Path to keyvault containing ssoContext secret. Swagger '
                   'name=ssoContext')
        c.argument('preferred_app_group_type', options_list=['--pagt', '--preferred-app-group-type'],
                   arg_type=get_enum_type(['None', 'Desktop', 'RailApplications']), help=''
                   'The type of preferred application group type, default to Desktop Application Group. Swagger '
                   'name=preferredAppGroupType')

    with self.argument_context('desktopvirtualization hostpool update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('host_pool_name', options_list=['--name', '-n', '--host-pool-name'], type=str, help='The name of '
                   'the host pool within the specified resource group. Swagger name=hostPoolName', id_part='name')
        c.argument('tags', tags_type)
        c.argument('friendly_name', type=str, help='Friendly name of HostPool. Swagger name=friendlyName')
        c.argument('description', type=str, help='Description of HostPool. Swagger name=description')
        c.argument('custom_rdp_property', type=str, help='Custom rdp property of HostPool. Swagger '
                   'name=customRdpProperty')
        c.argument('max_session_limit', type=int, help='The max session limit of HostPool. Swagger '
                   'name=maxSessionLimit')
        c.argument('personal_desktop_assignment_type', arg_type=get_enum_type(['Automatic', 'Direct']), help=''
                   'PersonalDesktopAssignment type for HostPool. Swagger name=personalDesktopAssignmentType')
        c.argument('load_balancer_type', arg_type=get_enum_type(['BreadthFirst', 'DepthFirst', 'Persistent']), help=''
                   'The type of the load balancer. Swagger name=loadBalancerType')
        c.argument('ring', type=int, help='The ring number of HostPool. Swagger name=ring')
        c.argument('validation_environment', arg_type=get_three_state_flag(), help='Is validation environment. Swagger '
                   'name=validationEnvironment')
        c.argument('registration_info', action=AddDesktopvirtualizationHostpoolUpdateRegistrationInfo, nargs='*',
                   help='The registration info of HostPool. Swagger name=registrationInfo')
        c.argument('sso_context', type=str, help='Path to keyvault containing ssoContext secret. Swagger '
                   'name=ssoContext')
        c.argument('preferred_app_group_type', options_list=['--pagt', '--preferred-app-group-type'],
                   arg_type=get_enum_type(['None', 'Desktop', 'RailApplications']), help=''
                   'The type of preferred application group type, default to Desktop Application Group. Swagger '
                   'name=preferredAppGroupType')
