# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LivySessionStateInformation(Model):
    """LivySessionStateInformation.

    :param not_started_at:
    :type not_started_at: datetime
    :param starting_at:
    :type starting_at: datetime
    :param idle_at:
    :type idle_at: datetime
    :param dead_at:
    :type dead_at: datetime
    :param shutting_down_at:
    :type shutting_down_at: datetime
    :param killed_at:
    :type killed_at: datetime
    :param recovering_at:
    :type recovering_at: datetime
    :param busy_at:
    :type busy_at: datetime
    :param error_at:
    :type error_at: datetime
    :param current_state:
    :type current_state: str
    :param job_creation_request:
    :type job_creation_request: ~azure.synapse.models.LivyRequestBase
    """

    _attribute_map = {
        'not_started_at': {'key': 'notStartedAt', 'type': 'iso-8601'},
        'starting_at': {'key': 'startingAt', 'type': 'iso-8601'},
        'idle_at': {'key': 'idleAt', 'type': 'iso-8601'},
        'dead_at': {'key': 'deadAt', 'type': 'iso-8601'},
        'shutting_down_at': {'key': 'shuttingDownAt', 'type': 'iso-8601'},
        'killed_at': {'key': 'killedAt', 'type': 'iso-8601'},
        'recovering_at': {'key': 'recoveringAt', 'type': 'iso-8601'},
        'busy_at': {'key': 'busyAt', 'type': 'iso-8601'},
        'error_at': {'key': 'errorAt', 'type': 'iso-8601'},
        'current_state': {'key': 'currentState', 'type': 'str'},
        'job_creation_request': {'key': 'jobCreationRequest', 'type': 'LivyRequestBase'},
    }

    def __init__(self, **kwargs):
        super(LivySessionStateInformation, self).__init__(**kwargs)
        self.not_started_at = kwargs.get('not_started_at', None)
        self.starting_at = kwargs.get('starting_at', None)
        self.idle_at = kwargs.get('idle_at', None)
        self.dead_at = kwargs.get('dead_at', None)
        self.shutting_down_at = kwargs.get('shutting_down_at', None)
        self.killed_at = kwargs.get('killed_at', None)
        self.recovering_at = kwargs.get('recovering_at', None)
        self.busy_at = kwargs.get('busy_at', None)
        self.error_at = kwargs.get('error_at', None)
        self.current_state = kwargs.get('current_state', None)
        self.job_creation_request = kwargs.get('job_creation_request', None)