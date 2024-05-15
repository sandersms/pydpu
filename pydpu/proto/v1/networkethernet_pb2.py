# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: networkethernet.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import networkvlan_pb2 as networkvlan__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15networkethernet.proto\x12%opi_api.network.opinetcommon.v1alpha1\x1a\x11networkvlan.proto\x1a\x1fgoogle/api/field_behavior.proto\"\xe5\x03\n\x0e\x45thernetConfig\x12%\n\x0bmac_address\x18\x01 \x01(\tB\x04\xe2\x41\x01\x01R\nmacAddress\x12+\n\x0e\x61uto_negotiate\x18\x02 \x01(\x08\x42\x04\xe2\x41\x01\x01R\rautoNegotiate\x12>\n\x18standalone_link_training\x18\x03 \x01(\x08\x42\x04\xe2\x41\x01\x01R\x16standaloneLinkTraining\x12[\n\x0b\x64uplex_mode\x18\x04 \x01(\x0e\x32\x34.opi_api.network.opinetcommon.v1alpha1.EthDuplexModeB\x04\xe2\x41\x01\x01R\nduplexMode\x12X\n\nport_speed\x18\x05 \x01(\x0e\x32\x33.opi_api.network.opinetcommon.v1alpha1.EthPortSpeedB\x04\xe2\x41\x01\x01R\tportSpeed\x12\x34\n\x13\x65nable_flow_control\x18\x06 \x01(\x08\x42\x04\xe2\x41\x01\x01R\x11\x65nableFlowControl\x12R\n\x08\x66\x65\x63_mode\x18\x07 \x01(\x0e\x32\x31.opi_api.network.opinetcommon.v1alpha1.EthFecModeB\x04\xe2\x41\x01\x01R\x07\x66\x65\x63Mode\"\xf1\x02\n\x16\x45thernetInDistribution\x12,\n\x12rx_frames_octets64\x18\x01 \x01(\x04R\x10rxFramesOctets64\x12\x37\n\x18rx_frames_octets65_to127\x18\x02 \x01(\x04R\x15rxFramesOctets65To127\x12\x39\n\x19rx_frames_octets128_to255\x18\x03 \x01(\x04R\x16rxFramesOctets128To255\x12\x39\n\x19rx_frames_octets256_to511\x18\x04 \x01(\x04R\x16rxFramesOctets256To511\x12;\n\x1arx_frames_octets512_to1023\x18\x05 \x01(\x04R\x17rxFramesOctets512To1023\x12=\n\x1brx_frames_octets1024_to1518\x18\x06 \x01(\x04R\x18rxFramesOctets1024To1518\"\x8d\x08\n\x10\x45thernetCounters\x12\x31\n\x15rx_mac_control_frames\x18\x01 \x01(\x04R\x12rxMacControlFrames\x12-\n\x13rx_mac_pause_frames\x18\x02 \x01(\x04R\x10rxMacPauseFrames\x12,\n\x12rx_oversize_frames\x18\x03 \x01(\x04R\x10rxOversizeFrames\x12.\n\x13rx_undersize_frames\x18\x04 \x01(\x04R\x11rxUndersizeFrames\x12(\n\x10rx_jabber_frames\x18\x05 \x01(\x04R\x0erxJabberFrames\x12,\n\x12rx_fragment_frames\x18\x06 \x01(\x04R\x10rxFragmentFrames\x12.\n\x13rx_ieee8021q_frames\x18\x07 \x01(\x04R\x11rxIeee8021qFrames\x12\"\n\rrx_crc_errors\x18\x08 \x01(\x04R\x0brxCrcErrors\x12&\n\x0frx_block_errors\x18\t \x01(\x04R\rrxBlockErrors\x12*\n\x11rx_carrier_errors\x18\n \x01(\x04R\x0frxCarrierErrors\x12*\n\x11rx_interrupted_tx\x18\x0b \x01(\x04R\x0frxInterruptedTx\x12*\n\x11rx_late_collision\x18\x0c \x01(\x04R\x0frxLateCollision\x12\'\n\x10rx_mac_errors_rx\x18\r \x01(\x04R\rrxMacErrorsRx\x12.\n\x13rx_single_collision\x18\x0e \x01(\x04R\x11rxSingleCollision\x12&\n\x0frx_symbol_error\x18\x0f \x01(\x04R\rrxSymbolError\x12.\n\x13rx_maxsize_exceeded\x18\x10 \x01(\x04R\x11rxMaxsizeExceeded\x12\x33\n\x16out_mac_control_frames\x18\x11 \x01(\x04R\x13outMacControlFrames\x12/\n\x14out_mac_pause_frames\x18\x12 \x01(\x04R\x11outMacPauseFrames\x12\x30\n\x14out_ieee8021q_frames\x18\x13 \x01(\x04R\x12outIeee8021qFrames\x12)\n\x11out_mac_errors_tx\x18\x14 \x01(\x04R\x0eoutMacErrorsTx\x12m\n\x13\x65th_rx_distribution\x18\x15 \x01(\x0b\x32=.opi_api.network.opinetcommon.v1alpha1.EthernetInDistributionR\x11\x65thRxDistribution\"\x8a\x06\n\rEthernetState\x12\x1f\n\x0bmac_address\x18\x01 \x01(\tR\nmacAddress\x12%\n\x0e\x61uto_negotiate\x18\x02 \x01(\x08R\rautoNegotiate\x12\x38\n\x18standalone_link_training\x18\x03 \x01(\x08R\x16standaloneLinkTraining\x12U\n\x0b\x64uplex_mode\x18\x04 \x01(\x0e\x32\x34.opi_api.network.opinetcommon.v1alpha1.EthDuplexModeR\nduplexMode\x12R\n\nport_speed\x18\x05 \x01(\x0e\x32\x33.opi_api.network.opinetcommon.v1alpha1.EthPortSpeedR\tportSpeed\x12.\n\x13\x65nable_flow_control\x18\x06 \x01(\x08R\x11\x65nableFlowControl\x12L\n\x08\x66\x65\x63_mode\x18\x07 \x01(\x0e\x32\x31.opi_api.network.opinetcommon.v1alpha1.EthFecModeR\x07\x66\x65\x63Mode\x12$\n\x0ehw_mac_address\x18\x08 \x01(\tR\x0chwMacAddress\x12j\n\x16negotiated_duplex_mode\x18\t \x01(\x0e\x32\x34.opi_api.network.opinetcommon.v1alpha1.EthDuplexModeR\x14negotiatedDuplexMode\x12g\n\x15negotiated_port_speed\x18\n \x01(\x0e\x32\x33.opi_api.network.opinetcommon.v1alpha1.EthPortSpeedR\x13negotiatedPortSpeed\x12S\n\x08\x63ounters\x18\x0b \x01(\x0b\x32\x37.opi_api.network.opinetcommon.v1alpha1.EthernetCountersR\x08\x63ounters\"\x83\x02\n\nEthernetIf\x12M\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x35.opi_api.network.opinetcommon.v1alpha1.EthernetConfigR\x06\x63onfig\x12J\n\x05state\x18\x02 \x01(\x0b\x32\x34.opi_api.network.opinetcommon.v1alpha1.EthernetStateR\x05state\x12Z\n\rswitched_vlan\x18\x03 \x01(\x0b\x32\x35.opi_api.network.opinetcommon.v1alpha1.VlanSwitchedIfR\x0cswitchedVlan*d\n\rEthDuplexMode\x12\x1f\n\x1b\x45TH_DUPLEX_MODE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x45TH_DUPLEX_MODE_FULL\x10\x01\x12\x18\n\x14\x45TH_DUPLEX_MODE_HALF\x10\x02*\xa0\x03\n\x0c\x45thPortSpeed\x12\x1e\n\x1a\x45TH_PORT_SPEED_UNSPECIFIED\x10\x00\x12\x16\n\x12\x45TH_PORT_SPEED_10M\x10\x01\x12\x17\n\x13\x45TH_PORT_SPEED_100M\x10\x02\x12\x15\n\x11\x45TH_PORT_SPEED_1G\x10\x03\x12\x18\n\x14\x45TH_PORT_SPEED_2500M\x10\x04\x12\x15\n\x11\x45TH_PORT_SPEED_5G\x10\x05\x12\x16\n\x12\x45TH_PORT_SPEED_10G\x10\x06\x12\x16\n\x12\x45TH_PORT_SPEED_25G\x10\x07\x12\x16\n\x12\x45TH_PORT_SPEED_40G\x10\x08\x12\x16\n\x12\x45TH_PORT_SPEED_50G\x10\t\x12\x17\n\x13\x45TH_PORT_SPEED_100G\x10\n\x12\x17\n\x13\x45TH_PORT_SPEED_200G\x10\x0b\x12\x17\n\x13\x45TH_PORT_SPEED_400G\x10\x0c\x12\x17\n\x13\x45TH_PORT_SPEED_600G\x10\r\x12\x17\n\x13\x45TH_PORT_SPEED_800G\x10\x0e\x12\x1a\n\x16\x45TH_PORT_SPEED_UNKNOWN\x10\x0f*\xb0\x01\n\nEthFecMode\x12\x1c\n\x18\x45TH_FEC_MODE_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x45TH_FEC_MODE_FC\x10\x01\x12\x16\n\x12\x45TH_FEC_MODE_RS528\x10\x02\x12\x16\n\x12\x45TH_FEC_MODE_RS544\x10\x03\x12$\n ETH_FEC_MODE_RS544_2X_INTERLEAVE\x10\x04\x12\x19\n\x15\x45TH_FEC_MODE_DISABLED\x10\x05\x42\x83\x01\n%opi_api.network.opinetcommon.v1alpha1B\x14NetworkEthernetProtoP\x01ZBgithub.com/opiproject/opi-api/network/opinetcommon/v1alpha1/gen/gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'networkethernet_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%opi_api.network.opinetcommon.v1alpha1B\024NetworkEthernetProtoP\001ZBgithub.com/opiproject/opi-api/network/opinetcommon/v1alpha1/gen/go'
  _globals['_ETHERNETCONFIG'].fields_by_name['mac_address']._options = None
  _globals['_ETHERNETCONFIG'].fields_by_name['mac_address']._serialized_options = b'\342A\001\001'
  _globals['_ETHERNETCONFIG'].fields_by_name['auto_negotiate']._options = None
  _globals['_ETHERNETCONFIG'].fields_by_name['auto_negotiate']._serialized_options = b'\342A\001\001'
  _globals['_ETHERNETCONFIG'].fields_by_name['standalone_link_training']._options = None
  _globals['_ETHERNETCONFIG'].fields_by_name['standalone_link_training']._serialized_options = b'\342A\001\001'
  _globals['_ETHERNETCONFIG'].fields_by_name['duplex_mode']._options = None
  _globals['_ETHERNETCONFIG'].fields_by_name['duplex_mode']._serialized_options = b'\342A\001\001'
  _globals['_ETHERNETCONFIG'].fields_by_name['port_speed']._options = None
  _globals['_ETHERNETCONFIG'].fields_by_name['port_speed']._serialized_options = b'\342A\001\001'
  _globals['_ETHERNETCONFIG'].fields_by_name['enable_flow_control']._options = None
  _globals['_ETHERNETCONFIG'].fields_by_name['enable_flow_control']._serialized_options = b'\342A\001\001'
  _globals['_ETHERNETCONFIG'].fields_by_name['fec_mode']._options = None
  _globals['_ETHERNETCONFIG'].fields_by_name['fec_mode']._serialized_options = b'\342A\001\001'
  _globals['_ETHDUPLEXMODE']._serialized_start=3059
  _globals['_ETHDUPLEXMODE']._serialized_end=3159
  _globals['_ETHPORTSPEED']._serialized_start=3162
  _globals['_ETHPORTSPEED']._serialized_end=3578
  _globals['_ETHFECMODE']._serialized_start=3581
  _globals['_ETHFECMODE']._serialized_end=3757
  _globals['_ETHERNETCONFIG']._serialized_start=117
  _globals['_ETHERNETCONFIG']._serialized_end=602
  _globals['_ETHERNETINDISTRIBUTION']._serialized_start=605
  _globals['_ETHERNETINDISTRIBUTION']._serialized_end=974
  _globals['_ETHERNETCOUNTERS']._serialized_start=977
  _globals['_ETHERNETCOUNTERS']._serialized_end=2014
  _globals['_ETHERNETSTATE']._serialized_start=2017
  _globals['_ETHERNETSTATE']._serialized_end=2795
  _globals['_ETHERNETIF']._serialized_start=2798
  _globals['_ETHERNETIF']._serialized_end=3057
# @@protoc_insertion_point(module_scope)