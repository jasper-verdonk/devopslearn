import re
from ncclient import manager

with manager.connect(
        host="10.1.1.25",
        port=830,
        username="cisco",
        password="cisco123",
        hostkey_verify=False) as m:

    filter = """
    <filter>
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
            <intf-items>
                <phys-items>
                    <PhysIf-list>
                        <id/>
                        <adminSt/>
                    </PhysIf-list>
                </phys-items>
            </intf-items>
        </System>
    </filter>
    """

    config = m.get_config(source="running", filter=filter).data_xml

    interfaces = config.split("<PhysIf-list>")
    interface_data = []

    for interface in interfaces[1:]:
        try:
            name = interface.split("<id>")[1].split("</id>")[0].strip()
            admin_status = interface.split("<adminSt>")[1].split("</adminSt>")[0].strip()
            interface_data.append((name, admin_status))
        except IndexError:
            continue

    interface_data.sort(key=lambda x: [int(part) if part.isdigit() else part.lower() for part in re.split(r'(\d+)', x[0])])

    for name, admin_status in interface_data[:10]:
        print(f"Interface: {name}, Admin Status: {admin_status}")