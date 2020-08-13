# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from .. import try_manual
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg):
    test.kwargs.update({'eventhub_namespace': "codegenlivetest", 'eventhub_name': 'livetest'})
    try:
        test.cmd('az eventhubs namespace create --name {eventhub_namespace} -g {rg}')
        test.cmd('az eventhubs eventhub create --name {eventhub_name} --namespace-name {eventhub_namespace} -g {rg}')
    except:
        pass


# EXAMPLE: kustoclusterscreateorupdate
@try_manual
def step_kustoclusterscreateorupdate2(test, rg):
    test.cmd('az kusto cluster create '
             '--cluster-name "{Clusters_2}" '
             '--identity-type "SystemAssigned" '
             '--location "southcentralus" '
             '--enable-purge true '
             '--enable-streaming-ingest true '
             '--key-vault-properties key-name="" key-vault-uri="" key-version="" '
             '--sku name="Standard_D11_v2" capacity=2 tier="Standard" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoclusterscreateorupdate
@try_manual
def step_kustoclusterscreateorupdate(test, rg):
    test.cmd('az kusto cluster create '
             '--cluster-name "{Clusters_3}" '
             '--identity-type "SystemAssigned" '
             '--location "southcentralus" '
             '--enable-purge true '
             '--enable-streaming-ingest true '
             '--key-vault-properties key-name="" key-vault-uri="" key-version="" '
             '--sku name="Standard_D11_v2" capacity=2 tier="Standard" '
             '--resource-group "{rg}"',
             checks=[])
    test.cmd('az kusto cluster wait --created '
             '--cluster-name "{Clusters_3}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoclusterschecknameavailability
@try_manual
def step_kustoclusterschecknameavailability(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: kustoclustersget
@try_manual
def step_kustoclustersget(test, rg):
    test.cmd('az kusto cluster show '
             '--cluster-name "{Clusters_3}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoclusterslist
@try_manual
def step_kustoclusterslist(test, rg):
    test.cmd('az kusto cluster list',
             checks=[])


# EXAMPLE: kustoclusterslistbyresourcegroup
@try_manual
def step_kustoclusterslistbyresourcegroup(test, rg):
    test.cmd('az kusto cluster list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoclustersstop
@try_manual
def step_kustoclustersstop(test, rg):
    test.cmd('az kusto cluster stop '
             '--cluster-name "{Clusters_3}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoclustersstart
@try_manual
def step_kustoclustersstart(test, rg):
    test.cmd('az kusto cluster start '
             '--cluster-name "{Clusters_3}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoclusterslistresourceskus
@try_manual
def step_kustoclusterslistresourceskus(test, rg):
    test.cmd('az kusto cluster list-sku '
             '--cluster-name "{Clusters_3}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoclusterslistskus
@try_manual
def step_kustoclusterslistskus(test, rg):
    test.cmd('az kusto cluster list-sku',
             checks=[])


# EXAMPLE: kustodatabasescreateorupdate
@try_manual
def step_kustodatabasescreateorupdate(test, rg):
    test.cmd('az kusto database create '
             '--cluster-name "{Clusters_3}" '
             '--database-name "KustoDatabase8" '
             '--read-write-database location="southcentralus" soft-delete-period="P1D" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustodatabasechecknameavailability
@try_manual
def step_kustodatabasechecknameavailability(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: kustodatabaseslistbycluster
@try_manual
def step_kustodatabaseslistbycluster(test, rg):
    test.cmd('az kusto database list '
             '--cluster-name "{Clusters_3}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustodatabasesget
@try_manual
def step_kustodatabasesget(test, rg):
    test.cmd('az kusto database show '
             '--database-name "KustoDatabase8" '
             '--cluster-name "{Clusters_3}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustodatabasesupdate
@try_manual
def step_kustodatabasesupdate(test, rg):
    test.cmd('az kusto database update '
             '--cluster-name "{Clusters_3}" '
             '--database-name "KustoDatabase8" '
             '--read-write-database soft-delete-period="P1D" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustodatabaseprincipalassignmentscreateorupdate
@try_manual
def step_kustodatabaseprincipalassignmentscreateorupdate(test, rg):
    test.cmd('az kusto database-principal-assignment create '
             '--cluster-name "{Clusters_3}" '
             '--database-name "Kustodatabase8" '
             '--principal-id "d9a1f322-1293-4595-91e3-f54f8bb34725" '
             '--principal-type "App" '
             '--role "Admin" '
             '--tenant-id "33e01921-4d64-4f8c-a055-5bdaffd5e33d" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}"',
             checks=[])
    test.cmd('az kusto database-principal-assignment wait --created '
             '--cluster-name "{Clusters_3}" '
             '--database-name "Kustodatabase8" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustodatabaselistprincipals
@try_manual
def step_kustodatabaselistprincipals(test, rg):
    test.cmd('az kusto database list-principal '
             '--cluster-name "{Clusters_3}" '
             '--database-name "Kustodatabase8" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustodatabaseprincipalassignmentsget
@try_manual
def step_kustodatabaseprincipalassignmentsget(test, rg):
    test.cmd('az kusto database-principal-assignment show '
             '--cluster-name "{Clusters_3}" '
             '--database-name "Kustodatabase8" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustodatabaseprincipalassignmentsdelete
@try_manual
def step_kustodatabaseprincipalassignmentsdelete(test, rg):
    test.cmd('az kusto database-principal-assignment delete '
             '--cluster-name "{Clusters_3}" '
             '--database-name "Kustodatabase8" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoclusterprincipalassignmentscreateorupdate
@try_manual
def step_kustoclusterprincipalassignmentscreateorupdate(test, rg):
    test.cmd('az kusto cluster-principal-assignment create '
             '--cluster-name "{Clusters_3}" '
             '--principal-id "d9a1f322-1293-4595-91e3-f54f8bb34725" '
             '--principal-type "App" '
             '--role "AllDatabasesViewer" '
             '--tenant-id "33e01921-4d64-4f8c-a055-5bdaffd5e33d" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}"',
             checks=[])
    test.cmd('az kusto cluster-principal-assignment wait --created '
             '--principal-assignment-name "kustoprincipal1" '
             '--cluster-name "{Clusters_3}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoclusterprincipalassignmentsget
@try_manual
def step_kustoclusterprincipalassignmentsget(test, rg):
    test.cmd('az kusto cluster-principal-assignment show '
             '--cluster-name "{Clusters_3}" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: attacheddatabaseconfigurationscreateorupdate
@try_manual
def step_attacheddatabaseconfigurationscreateorupdate(test, rg):
    test.cmd('az kusto attached-database-configuration create '
             '--attached-database-configuration-name "{attachedDatabaseConfigurations_1}" '
             '--cluster-name "{Clusters_2}" '
             '--location "southcentralus" '
             '--cluster-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Kusto/Clu'
             'sters/{Clusters_3}" '
             '--database-name "Kustodatabase8" '
             '--default-principals-modification-kind "Union" '
             '--resource-group "{rg}"',
             checks=[])
    test.cmd('az kusto attached-database-configuration wait --created '
             '--cluster-name "{Clusters_2}" '
             '--attached-database-configuration-name "{attachedDatabaseConfigurations_1}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: attacheddatabaseconfigurationsget
@try_manual
def step_attacheddatabaseconfigurationsget(test, rg):
    test.cmd('az kusto attached-database-configuration show '
             '--attached-database-configuration-name "{attachedDatabaseConfigurations_1}" '
             '--cluster-name "{Clusters_2}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoattacheddatabaseconfigurationslistbycluster
@try_manual
def step_kustoattacheddatabaseconfigurationslistbycluster(test, rg):
    test.cmd('az kusto attached-database-configuration list '
             '--cluster-name "{Clusters_3}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoclusterlistfollowerdatabases
@try_manual
def step_kustoclusterlistfollowerdatabases(test, rg):
    test.cmd('az kusto cluster list-follower-database '
             '--cluster-name "{Clusters_3}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoclusterdetachfollowerdatabases
@try_manual
def step_kustoclusterdetachfollowerdatabases(test, rg):
    test.cmd('az kusto cluster detach-follower-database '
             '--cluster-name "{Clusters_3}" '
             '--attached-database-configuration-name "{attachedDatabaseConfigurations_1}" '
             '--cluster-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Kusto/clu'
             'sters/{Clusters_2}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustooperationslist
@try_manual
def step_kustooperationslist(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: kustodatabasesdelete
@try_manual
def step_kustodatabasesdelete(test, rg):
    test.cmd('az kusto database delete '
             '--cluster-name "{Clusters_3}" '
             '--database-name "KustoDatabase8" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: kustoclustersdelete
@try_manual
def step_kustoclustersdelete(test, rg):
    test.cmd('az kusto cluster delete '
             '--cluster-name "{Clusters_3}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDataConnectionValidation
@try_manual
def step_kustodataconnectionvalidation(test, rg):
    test.cmd('az kusto data-connection event-hub data-connection-validation '
             '--cluster-name "{Clusters_3}" '
             '--database-name "KustoDatabase8" '
             '--data-connection-name "{DataConnections8}" '
             '--consumer-group "$Default" '
             '--event-hub-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.EventHub/namespaces/{eventhub_namespace}/eventhubs/{eventhub_name}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDataConnectionsCreateOrUpdate
@try_manual
def step_kustodataconnectionscreateorupdate(test, rg):
    test.cmd('az kusto data-connection event-hub create '
             '--cluster-name "{Clusters_3}" '
             '--data-connection-name "{DataConnections8}" '
             '--database-name "KustoDatabase8" '
             '--location "southcentralus" '
             '--consumer-group "$Default" '
             '--event-hub-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.EventHub/namespaces/{eventhub_namespace}/eventhubs/{eventhub_name}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDataConnectionsGet
@try_manual
def step_kustodataconnectionsget(test, rg):
    test.cmd('az kusto data-connection show '
             '--cluster-name "{Clusters_3}" '
             '--data-connection-name "{DataConnections8}" '
             '--database-name "KustoDatabase8" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDataConnectionsUpdate
@try_manual
def step_kustodataconnectionsupdate(test, rg):
    test.cmd('az kusto data-connection event-hub update '
             '--cluster-name "{Clusters_3}" '
             '--data-connection-name "{DataConnections8}" '
             '--database-name "KustoDatabase8" '
             '--location "southcentralus" '
             '--consumer-group "$Default" '
             '--event-hub-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.EventHub/namespaces/{eventhub_namespace}/eventhubs/{eventhub_name}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDataConnectionsDelete
@try_manual
def step_kustodataconnectionsdelete(test, rg):
    test.cmd('az kusto data-connection delete '
             '--cluster-name "{Clusters_3}" '
             '--data-connection-name "{DataConnections8}" '
             '--database-name "KustoDatabase8" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def cleanup(test, rg):
    try:
        test.cmd('az eventhubs eventhub delete --name {eventhub_name} --namespace-name {eventhub_namespace} -g {rg}')
        test.cmd('az eventhubs namespace delete --name {eventhub_namespace} -g {rg}')
    except:
        pass


@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step_kustoclusterscreateorupdate2(test, rg)
    step_kustoclusterscreateorupdate(test, rg)
    step_kustodatabasescreateorupdate(test, rg)
    step_kustoclusterschecknameavailability(test, rg)
    step_kustoclustersget(test, rg)
    step_kustoclusterslist(test, rg)
    step_kustoclusterslistbyresourcegroup(test, rg)
    step_kustoclusterslistresourceskus(test, rg)
    step_kustoclusterslistskus(test, rg)
    step_kustodatabasescreateorupdate(test, rg)
    step_kustodatabasechecknameavailability(test, rg)
    step_kustodatabaseslistbycluster(test, rg)
    step_kustodatabasesget(test, rg)
    step_kustodatabasesupdate(test, rg)
    step_kustodatabaseprincipalassignmentscreateorupdate(test, rg)
    step_kustodatabaselistprincipals(test, rg)
    step_kustodatabaseprincipalassignmentsget(test, rg)
    step_kustodatabaseprincipalassignmentsdelete(test, rg)
    step_kustoclusterprincipalassignmentscreateorupdate(test, rg)
    step_kustoclusterprincipalassignmentsget(test, rg)
    step_attacheddatabaseconfigurationscreateorupdate(test, rg)
    step_attacheddatabaseconfigurationsget(test, rg)
    step_kustoattacheddatabaseconfigurationslistbycluster(test, rg)
    step_kustoclusterlistfollowerdatabases(test, rg)
    step_kustoclusterdetachfollowerdatabases(test, rg)
    step_kustodataconnectionvalidation(test, rg)
    step_kustodataconnectionscreateorupdate(test, rg)
    step_kustodataconnectionsget(test, rg)
    step_kustodataconnectionsupdate(test, rg)
    step_kustodataconnectionsdelete(test, rg)
    step_kustooperationslist(test, rg)
    step_kustodatabasesdelete(test, rg)
    step_kustoclustersdelete(test, rg)
    cleanup(test, rg)


@try_manual
class KustoManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestkusto_kustorptest'[:7], key='rg', parameter_name='rg')
    def test_kusto(self, rg):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'Clusters_2': 'followercluster100',
            'Clusters_3': 'leadercluster100',
            'attachedDatabaseConfigurations_1': 'attachedDatabaseConfigurations2',
            'DataConnections8': 'DataConnections8',
        })

        call_scenario(self, rg)
