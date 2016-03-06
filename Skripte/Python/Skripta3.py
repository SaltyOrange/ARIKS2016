#!/usr/bin/env python

from os import environ as env
import novaclient.client
from neutronclient.v2_0 import client as neutronclient

nova = novaclient.client.Client("2", auth_url=env['OS_AUTH_URL'],
                                username=env['OS_USERNAME'],
                                api_key=env['OS_PASSWORD'],
                                project_id=env['OS_TENANT_NAME'],
                                region_name=env['OS_REGION_NAME'])

#instanciranje neutron objekta
neutron = neutronclient.Client(auth_url=env['OS_AUTH_URL'],
                               username=env['OS_USERNAME'],
                               password=env['OS_PASSWORD'],
                               tenant_name=env['OS_TENANT_NAME'],
                               region_name=env['OS_REGION_NAME'])

network_name = 'my_net2'

try:
      #pohrana podataka o mre�i koju �elimo stvoriti unutar
      #dvodimenzionalnog asocijativnog polja
      body_net = {'network': {'name': network_name,
                   'admin_state_up': True}}

      #kreacija mre�e te pohrana podataka o toj mre�i
	netw = neutron.create_network(body=body_net)

      #dohvacanje ID kreirane mre�e
	net_dict = netw['network']
	network_id = net_dict['id']

	print('Network %s created' % network_id)

      #pohrana podataka o podmre�i koju �elimo stvoriti unutar
      #dvodimenzionalnog asocijativnog polja
	body_subnet = {'subnets': [{'name':'my_subnet1',
                            'cidr':'10.20.1.0/24',
                            'ip_version': 4,
                            'network_id': network_id}]}

      #kreacija podmre�e te pohrana podataka o toj mre�i
	subnet = neutron.create_subnet(body=body_subnet)
    
	print('\nCreated subnet %s\n' % subnet)

#izvr�ava se nakon �to se try blok izvr�i bez gre�ke
finally:
    print("Execution completed")