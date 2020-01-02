# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest
import time

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, JMESPathCheck, JMESPathCheckExists)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class NotificationHubsScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_notificationhubs')
    def test_notificationhubs(self, resource_group):

        self.kwargs.update({
            'namespace-name': 'my-test-space',
            'notification-hub-name': 'my-test-hub',
            'rg': 'feng-cli-rg',
        })

        self.cmd('az notificationhubs namespace check-availability '
                 '--name {namespace-name}',
                 checks=[])

        self.cmd('az notificationhubs namespace create '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name} '
                 '--location "South Central US" '
                 '--sku-name "Free"',
                 checks=[JMESPathCheck('name', self.kwargs.get('namespace-name',''))])

        if self.is_live:
            time.sleep(60)

        self.cmd('az notificationhubs check-availability '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name} '
                 '--notification-hub-name {notification-hub-name}',
                 checks=[])

        self.cmd('az notificationhubs create '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name} '
                 '--notification-hub-name {notification-hub-name} '
                 '--location "South Central US" '
                 '--sku-name "Free"',
                 checks=[JMESPathCheck('name', self.kwargs.get('notification-hub-name',''))])

        self.cmd('az notificationhubs namespace authorization-rule create '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name} '
                 '--name "my-space-rule" '
                 '--rights "Listen,Send"',
                 checks=[JMESPathCheck('name', 'my-space-rule')])

        self.cmd('az notificationhubs namespace authorization-rule show '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name} '
                 '--name "my-space-rule"',
                 checks=[JMESPathCheck('name', 'my-space-rule')])

        self.cmd('az notificationhubs namespace authorization-rule list '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name}',
                 checks=[JMESPathCheckExists("[0].rights")])

        # self.cmd('az notificationhubs namespace authorization-rule list_keys '
        #          '--resource-group {rg} '
        #          '--namespace-name {namespace-name} '
        #          '--name "my-space-rule"',
        #          checks=[JMESPathCheckExists('primaryConnectionString')])

        self.cmd('az notificationhubs authorization-rule create '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name} '
                 '--notification-hub-name {notification-hub-name} '
                 '--name "my-hub-send-key" '
                 '--rights "Listen"',
                 checks=[JMESPathCheck('name', 'my-hub-send-key')])

        self.cmd('az notificationhubs authorization-rule show '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name} '
                 '--notification-hub-name {notification-hub-name} '
                 '--name "my-hub-send-key"',
                 checks=[JMESPathCheck('name', 'my-hub-send-key')])

        self.cmd('az notificationhubs authorization-rule list '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name} '
                 '--notification-hub-name {notification-hub-name}',
                 checks=[JMESPathCheckExists("[0].rights")])

        # self.cmd('az notificationhubs authorization-rule list_keys '
        #          '--resource-group {rg} '
        #          '--namespace-name {namespace-name} '
        #          '--notification-hub-name {notification-hub-name} '
        #          '--name "my-hub-send-key"',
        #          checks=[JMESPathCheckExists('primaryConnectionString')])

        self.cmd('az notificationhubs credential gcm update '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name} '
                 '--notification-hub-name {notification-hub-name} '
                 '--google-api-key "AAAANgU-LAk:APA91bFs_MDVVfouFbeIHNx8p-y8ZHk3jLgxXr4CDZLbiCLKyRd9pnGSGI4BY9OeiZZXY3thSPN0Mh0_irhnymnhyWvauSgeCplUF1aDvDCB8lDiQngOgx6tOAbSohy1oZRLUXedgkWp"',
                 checks=[])

        self.cmd('az notificationhubs credential list '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name} '
                 '--notification-hub-name {notification-hub-name}',
                 checks=[JMESPathCheckExists('gcmCredential.googleApiKey')])

        # self.cmd('az notificationhubs test-send '
        #     '--resource-group {rg} '
        #     '--namespace-name {namespace-name} '
        #     '--notification-hub-name {notification-hub-name} '
        #     '--notification-format gcm '
        #     r'--payload "{\"data\":{\"message\":\"test notification\"}}"',
        #     checks=[])

        self.cmd('az notificationhubs show '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name} '
                 '--notification-hub-name {notification-hub-name}',
                 checks=[JMESPathCheck('name', self.kwargs.get('notification-hub-name',''))])

        self.cmd('az notificationhubs list '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name}',
                 checks=[])

        self.cmd('az notificationhubs namespace show '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name}',
                 checks=[JMESPathCheck('name', self.kwargs.get('namespace-name',''))])

        self.cmd('az notificationhubs namespace list '
                 '--resource-group {rg}',
                 checks=[])

        # if self.is_live:
        #     time.sleep(60)
        # self.cmd('az notificationhubs authorization-rule regenerate_keys '
        #          '--resource-group {rg} '
        #          '--namespace-name {namespace-name} '
        #          '--notification-hub-name {notification-hub-name} '
        #          '--name "my-hub-send-key" '
        #          '--policy-key "Secondary Key"',
        #          checks=[])

        # self.cmd('az notificationhubs namespace authorization-rule regenerate_keys '
        #          '--resource-group {rg} '
        #          '--namespace-name {namespace-name} '
        #          '--name "my-space-rule" '
        #          '--policy-key "Secondary Key"',
        #          checks=[])

        self.cmd('az notificationhubs delete '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name} '
                 '--notification-hub-name {notification-hub-name}',
                 checks=[])

        self.cmd('az notificationhubs namespace delete '
                 '--resource-group {rg} '
                 '--namespace-name {namespace-name}',
                 checks=[])
