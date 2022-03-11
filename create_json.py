
import json

def write_json():

    data = {
                    "target": "bmv2",
                    "p4info": "build/basic.p4.p4info.txt",
                    "bmv2_json": "build/basic.json",
                    "table_entries":[]
    }
    #create a list
    data_holder = data["table_entries"]

    data_holder.append({'table': 'MyIngress.ipv4_lpm',
                        'default_action': True,
                        'action_name': 'MyIngress.drop',
                         'action_params': { }},)
    data_holder.append({ 'table': 'MyIngress.ipv4_lpm',
                         'match': {'hdr.ipv4.dstAddr': ['10.0.1.1', 32]},
                         'action_name': 'MyIngress.ipv4_forward',
                         'action_params': {
                            'dstAddr': "08:00:00:00:01:11",
                            'port': 1
                         }},)
    data_holder.append({'table': 'MyIngress.ipv4_lpm',
                        'match': {'hdr.ipv4.dstAddr': ['10.0.2.2', 32]},
                        'action_name': 'MyIngress.ipv4_forward',
                        'action_params': {
                            'dstAddr': "08:00:00:00:02:22",
                            'port': 2
                        }}, )
    data_holder.append({'table': 'MyIngress.ipv4_lpm',
                        'match': {'hdr.ipv4.dstAddr': ['10.0.3.3', 32]},
                        'action_name': 'MyIngress.ipv4_forward',
                        'action_params': {
                            'dstAddr': "08:00:00:00:03:00",
                            'port': 3
                        }}, )
    data_holder.append({'table': 'MyIngress.ipv4_lpm',
                        'match': {'hdr.ipv4.dstAddr': ['10.0.4.4', 32]},
                        'action_name': 'MyIngress.ipv4_forward',
                        'action_params': {
                            'dstAddr': "08:00:00:00:04:00",
                            'port': 4
                        }})
    file = open('domain_name_3.txt', 'r')
    Lines = file.readlines()

    for line in Lines:
        data_holder.append({'table': 'MyIngress.ipv4_lpm',
          'match': {
            'hdr.ipv4.dstAddr': [line.strip(), 32]
          },
          'action_name': 'MyIngress.drop',
          'action_params': {}
             },)


    #write the file
    file_path='s1-runtime.json'
    with open(file_path, 'w') as outfile:
        print("writing file to: ",file_path)
        json.dump(data, outfile, indent=4)
    outfile.close()
    print("done")

write_json()