import xml.etree.cElementTree as ET


def xml_parser_read(path='/files_61850/KALINA.CID'):
    tree = ET.parse(path)
    root = tree.getroot()
    pref = '{http://www.iec.ch/61850/2003/SCL}'
    ip = root.findall(
        '{pref}Communication/{pref}SubNetwork/{pref}ConnectedAP/{pref}Address/{pref}P[@type="IP"]'.format(pref=pref))
    mask = root.findall(
        '{pref}Communication/{pref}SubNetwork/{pref}ConnectedAP/{pref}Address/{pref}P[@type="IP-SUBNET"]'.format(pref=pref))
    gate = root.findall(
        '{pref}Communication/{pref}SubNetwork/{pref}ConnectedAP/{pref}Address/{pref}P[@type="IP-GATEWAY"]'.format(pref=pref))
    ied1 = root.findall('{pref}Communication/{pref}SubNetwork/{pref}ConnectedAP'.format(pref=pref))
    ied2 = root.findall('{pref}IED'.format(pref=pref))

    # print(ip[0].text, mask[0].text, gate[0].text)
    # ip[0].text = "192.168.2.13"
    return ip[0].text, mask[0].text, gate[0].text, ied2[0].attrib.get('name')

def xml_parser_write(ip, mask, gate, ied, path='/files_61850/KALINA.CID'):
    tree = ET.parse(path)
    root = tree.getroot()
    pref = '{http://www.iec.ch/61850/2003/SCL}'

    ip_path = root.findall('{pref}Communication/{pref}SubNetwork/{pref}ConnectedAP/{pref}Address/{pref}P[@type="IP"]'.format(pref=pref))
    mask_path = root.findall('{pref}Communication/{pref}SubNetwork/{pref}ConnectedAP/{pref}Address/{pref}P[@type="IP-SUBNET"]'.format(pref=pref))
    gate_path = root.findall('{pref}Communication/{pref}SubNetwork/{pref}ConnectedAP/{pref}Address/{pref}P[@type="IP-GATEWAY"]'.format(pref=pref))
    ied1_path = root.findall('{pref}Communication/{pref}SubNetwork/{pref}ConnectedAP'.format(pref=pref))
    ied2_path = root.findall('{pref}IED'.format(pref=pref))
    ip_path[0].text = ip
    mask_path[0].text = mask
    gate_path[0].text = gate
    ied1_path[0].attrib = {'apName': 'S1', 'iedName': ied}
    ied2_path[0].attrib = {'name': ied}
    tree.write(path)