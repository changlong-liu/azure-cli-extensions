# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ApplicationGroupOperations(object):
    """ApplicationGroupOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.DesktopVirtualization.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get(
        self,
        resource_group_name,  # type: str
        application_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ApplicationGroup"
        """Get an application group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param application_group_name: The name of the application group.
        :type application_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationGroup or the result of cls(response)
        :rtype: ~azure.mgmt.DesktopVirtualization.models.ApplicationGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ApplicationGroup"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-10-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'applicationGroupName': self._serialize.url("application_group_name", application_group_name, 'str', max_length=24, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationGroup', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}'}  # type: ignore

    def create_or_update(
        self,
        resource_group_name,  # type: str
        application_group_name,  # type: str
        location,  # type: str
        host_pool_arm_path,  # type: str
        application_group_type,  # type: Union[str, "models.ApplicationGroupType"]
        tags=None,  # type: Optional[Dict[str, str]]
        description=None,  # type: Optional[str]
        friendly_name=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ApplicationGroup"
        """Create or update an applicationGroup.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param application_group_name: The name of the application group.
        :type application_group_name: str
        :param location: The geo-location where the resource lives.
        :type location: str
        :param host_pool_arm_path: HostPool arm path of ApplicationGroup.
        :type host_pool_arm_path: str
        :param application_group_type: Resource Type of ApplicationGroup.
        :type application_group_type: str or ~azure.mgmt.DesktopVirtualization.models.ApplicationGroupType
        :param tags: Resource tags.
        :type tags: dict[str, str]
        :param description: Description of ApplicationGroup.
        :type description: str
        :param friendly_name: Friendly name of ApplicationGroup.
        :type friendly_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationGroup or the result of cls(response)
        :rtype: ~azure.mgmt.DesktopVirtualization.models.ApplicationGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ApplicationGroup"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _application_group = models.ApplicationGroup(tags=tags, location=location, description=description, friendly_name=friendly_name, host_pool_arm_path=host_pool_arm_path, application_group_type=application_group_type)
        api_version = "2019-12-10-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'applicationGroupName': self._serialize.url("application_group_name", application_group_name, 'str', max_length=24, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_application_group, 'ApplicationGroup')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ApplicationGroup', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ApplicationGroup', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}'}  # type: ignore

    def delete(
        self,
        resource_group_name,  # type: str
        application_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Remove an applicationGroup.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param application_group_name: The name of the application group.
        :type application_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-10-preview"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'applicationGroupName': self._serialize.url("application_group_name", application_group_name, 'str', max_length=24, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}'}  # type: ignore

    def update(
        self,
        resource_group_name,  # type: str
        application_group_name,  # type: str
        tags=None,  # type: Optional[object]
        description=None,  # type: Optional[str]
        friendly_name=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ApplicationGroup"
        """Update an applicationGroup.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param application_group_name: The name of the application group.
        :type application_group_name: str
        :param tags: tags to be updated.
        :type tags: object
        :param description: Description of ApplicationGroup.
        :type description: str
        :param friendly_name: Friendly name of ApplicationGroup.
        :type friendly_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationGroup or the result of cls(response)
        :rtype: ~azure.mgmt.DesktopVirtualization.models.ApplicationGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ApplicationGroup"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _application_group = models.ApplicationGroupPatch(tags=tags, description=description, friendly_name=friendly_name)
        api_version = "2019-12-10-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'applicationGroupName': self._serialize.url("application_group_name", application_group_name, 'str', max_length=24, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        if _application_group is not None:
            body_content = self._serialize.body(_application_group, 'ApplicationGroupPatch')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationGroup', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}'}  # type: ignore

    def list_by_resource_group(
        self,
        resource_group_name,  # type: str
        filter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.ApplicationGroupList"]
        """List applicationGroups.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param filter: OData filter expression. Valid properties for filtering are
     applicationGroupType.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of ApplicationGroupList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.DesktopVirtualization.models.ApplicationGroupList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ApplicationGroupList"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-10-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ApplicationGroupList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups'}  # type: ignore

    def list_by_subscription(
        self,
        filter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.ApplicationGroupList"]
        """List applicationGroups in subscription.

        :param filter: OData filter expression. Valid properties for filtering are
     applicationGroupType.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of ApplicationGroupList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.DesktopVirtualization.models.ApplicationGroupList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ApplicationGroupList"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-10-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_subscription.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ApplicationGroupList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DesktopVirtualization/applicationGroups'}  # type: ignore
