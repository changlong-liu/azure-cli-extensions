# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

from ._configuration import DesktopVirtualizationAPIClientConfiguration
from .operations import OperationOperations
from .operations import WorkspaceOperations
from .operations import ApplicationGroupAssignmentOperations
from .operations import ApplicationGroupOperations
from .operations import StartMenuItemOperations
from .operations import ApplicationOperations
from .operations import DesktopOperations
from .operations import HostPoolOperations
from .operations import UserSessionOperations
from .operations import SessionHostOperations
from .operations import ActiveApplicationOperations
from . import models


class DesktopVirtualizationAPIClient(object):
    """DesktopVirtualizationAPIClient.

    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.DesktopVirtualization.operations.OperationOperations
    :ivar workspace: WorkspaceOperations operations
    :vartype workspace: azure.mgmt.DesktopVirtualization.operations.WorkspaceOperations
    :ivar application_group_assignment: ApplicationGroupAssignmentOperations operations
    :vartype application_group_assignment: azure.mgmt.DesktopVirtualization.operations.ApplicationGroupAssignmentOperations
    :ivar application_group: ApplicationGroupOperations operations
    :vartype application_group: azure.mgmt.DesktopVirtualization.operations.ApplicationGroupOperations
    :ivar start_menu_item: StartMenuItemOperations operations
    :vartype start_menu_item: azure.mgmt.DesktopVirtualization.operations.StartMenuItemOperations
    :ivar application: ApplicationOperations operations
    :vartype application: azure.mgmt.DesktopVirtualization.operations.ApplicationOperations
    :ivar desktop: DesktopOperations operations
    :vartype desktop: azure.mgmt.DesktopVirtualization.operations.DesktopOperations
    :ivar host_pool: HostPoolOperations operations
    :vartype host_pool: azure.mgmt.DesktopVirtualization.operations.HostPoolOperations
    :ivar user_session: UserSessionOperations operations
    :vartype user_session: azure.mgmt.DesktopVirtualization.operations.UserSessionOperations
    :ivar session_host: SessionHostOperations operations
    :vartype session_host: azure.mgmt.DesktopVirtualization.operations.SessionHostOperations
    :ivar active_application: ActiveApplicationOperations operations
    :vartype active_application: azure.mgmt.DesktopVirtualization.operations.ActiveApplicationOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DesktopVirtualizationAPIClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace = WorkspaceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.application_group_assignment = ApplicationGroupAssignmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.application_group = ApplicationGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.start_menu_item = StartMenuItemOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.application = ApplicationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.desktop = DesktopOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.host_pool = HostPoolOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_session = UserSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.session_host = SessionHostOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.active_application = ActiveApplicationOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DesktopVirtualizationAPIClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
