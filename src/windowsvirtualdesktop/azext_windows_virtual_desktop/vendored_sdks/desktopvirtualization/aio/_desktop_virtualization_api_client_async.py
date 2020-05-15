# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import DesktopVirtualizationAPIClientConfiguration
from .operations_async import OperationOperations
from .operations_async import WorkspaceOperations
from .operations_async import ApplicationGroupAssignmentOperations
from .operations_async import ApplicationGroupOperations
from .operations_async import StartMenuItemOperations
from .operations_async import ApplicationOperations
from .operations_async import DesktopOperations
from .operations_async import HostPoolOperations
from .operations_async import UserSessionOperations
from .operations_async import SessionHostOperations
from .operations_async import ActiveApplicationOperations
from .. import models


class DesktopVirtualizationAPIClient(object):
    """DesktopVirtualizationAPIClient.

    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.DesktopVirtualization.aio.operations_async.OperationOperations
    :ivar workspace: WorkspaceOperations operations
    :vartype workspace: azure.mgmt.DesktopVirtualization.aio.operations_async.WorkspaceOperations
    :ivar application_group_assignment: ApplicationGroupAssignmentOperations operations
    :vartype application_group_assignment: azure.mgmt.DesktopVirtualization.aio.operations_async.ApplicationGroupAssignmentOperations
    :ivar application_group: ApplicationGroupOperations operations
    :vartype application_group: azure.mgmt.DesktopVirtualization.aio.operations_async.ApplicationGroupOperations
    :ivar start_menu_item: StartMenuItemOperations operations
    :vartype start_menu_item: azure.mgmt.DesktopVirtualization.aio.operations_async.StartMenuItemOperations
    :ivar application: ApplicationOperations operations
    :vartype application: azure.mgmt.DesktopVirtualization.aio.operations_async.ApplicationOperations
    :ivar desktop: DesktopOperations operations
    :vartype desktop: azure.mgmt.DesktopVirtualization.aio.operations_async.DesktopOperations
    :ivar host_pool: HostPoolOperations operations
    :vartype host_pool: azure.mgmt.DesktopVirtualization.aio.operations_async.HostPoolOperations
    :ivar user_session: UserSessionOperations operations
    :vartype user_session: azure.mgmt.DesktopVirtualization.aio.operations_async.UserSessionOperations
    :ivar session_host: SessionHostOperations operations
    :vartype session_host: azure.mgmt.DesktopVirtualization.aio.operations_async.SessionHostOperations
    :ivar active_application: ActiveApplicationOperations operations
    :vartype active_application: azure.mgmt.DesktopVirtualization.aio.operations_async.ActiveApplicationOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DesktopVirtualizationAPIClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

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

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DesktopVirtualizationAPIClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
