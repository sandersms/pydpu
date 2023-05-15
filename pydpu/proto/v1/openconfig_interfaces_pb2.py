# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openconfig_interfaces.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bopenconfig_interfaces.proto\x12\x12opi_api.network.v1\"\xbd\x14\n\tInterface\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x06\x63onfig\x18\x02 \x01(\x0b\x32$.opi_api.network.v1.Interface.Config\x12\x32\n\x05state\x18\x03 \x01(\x0b\x32#.opi_api.network.v1.Interface.State\x12\x38\n\x08holdtime\x18\x04 \x01(\x0b\x32&.opi_api.network.v1.Interface.HoldTime\x12\x42\n\rsubinterfaces\x18\x05 \x01(\x0b\x32+.opi_api.network.v1.Interface.Subinterfaces\x1a\x91\x01\n\x06\x43onfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x04type\x18\x02 \x01(\x0e\x32!.opi_api.network.v1.InterfaceType\x12\x0b\n\x03mtu\x18\x03 \x01(\r\x12\x15\n\rloopback_mode\x18\x04 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x06 \x01(\x08\x1a\xce\x06\n\x05State\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x04type\x18\x02 \x01(\x0e\x32!.opi_api.network.v1.InterfaceType\x12\x0b\n\x03mtu\x18\x03 \x01(\r\x12\x15\n\rloopback_mode\x18\x04 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x06 \x01(\x08\x12\x0f\n\x07ifindex\x18\x07 \x01(\r\x12\x38\n\x0c\x61\x64min_status\x18\x08 \x01(\x0e\x32\".opi_api.network.v1.InterfaceState\x12\x37\n\x0boper_status\x18\t \x01(\x0e\x32\".opi_api.network.v1.InterfaceState\x12\x13\n\x0blast_change\x18\n \x01(\x04\x12\x0f\n\x07logical\x18\x0b \x01(\x08\x12\x12\n\nmanagement\x18\x0c \x01(\x08\x12\x0b\n\x03\x63pu\x18\r \x01(\x08\x12>\n\x08\x63ounters\x18\x0e \x01(\x0b\x32,.opi_api.network.v1.Interface.State.Counters\x1a\xb0\x03\n\x08\x43ounters\x12\x11\n\tin_octets\x18\x01 \x01(\x04\x12\x12\n\nin_packets\x18\x02 \x01(\x04\x12\x17\n\x0fin_unicast_pkts\x18\x03 \x01(\x04\x12\x19\n\x11in_broadcast_pkts\x18\x04 \x01(\x04\x12\x19\n\x11in_multicast_pkts\x18\x05 \x01(\x04\x12\x13\n\x0bin_discards\x18\x06 \x01(\x04\x12\x11\n\tin_errors\x18\x07 \x01(\x04\x12\x19\n\x11in_unknown_protos\x18\x08 \x01(\x04\x12\x15\n\rin_fcs_errors\x18\t \x01(\x04\x12\x12\n\nout_octets\x18\n \x01(\x04\x12\x13\n\x0bout_packets\x18\x0b \x01(\x04\x12\x18\n\x10out_unicast_pkts\x18\x0c \x01(\x04\x12\x1a\n\x12out_broadcast_pkts\x18\r \x01(\x04\x12\x1a\n\x12out_multicast_pkts\x18\x0e \x01(\x04\x12\x14\n\x0cout_discards\x18\x0f \x01(\x04\x12\x12\n\nout_errors\x18\x10 \x01(\x04\x12\x1b\n\x13\x63\x61rrier_transitions\x18\x11 \x01(\x04\x12\x12\n\nlast_clear\x18\x12 \x01(\x04\x1a\xcd\x01\n\x08HoldTime\x12=\n\x06\x63onfig\x18\x01 \x01(\x0b\x32-.opi_api.network.v1.Interface.HoldTime.Config\x12;\n\x05state\x18\x02 \x01(\x0b\x32,.opi_api.network.v1.Interface.HoldTime.State\x1a\"\n\x06\x43onfig\x12\n\n\x02up\x18\x01 \x01(\r\x12\x0c\n\x04\x64own\x18\x02 \x01(\r\x1a!\n\x05State\x12\n\n\x02up\x18\x01 \x01(\r\x12\x0c\n\x04\x64own\x18\x02 \x01(\r\x1a\x84\t\n\rSubinterfaces\x12N\n\x0csubinterface\x18\x02 \x03(\x0b\x32\x38.opi_api.network.v1.Interface.Subinterfaces.Subinterface\x1a\xa2\x08\n\x0cSubinterface\x12\r\n\x05index\x18\x01 \x01(\x04\x12O\n\x06\x63onfig\x18\x02 \x01(\x0b\x32?.opi_api.network.v1.Interface.Subinterfaces.Subinterface.Config\x12M\n\x05state\x18\x03 \x01(\x0b\x32>.opi_api.network.v1.Interface.Subinterfaces.Subinterface.State\x1a=\n\x06\x43onfig\x12\r\n\x05index\x18\x01 \x01(\x04\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x1a\xa3\x06\n\x05State\x12\r\n\x05index\x18\x01 \x01(\r\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07ifindex\x18\x05 \x01(\r\x12\x38\n\x0c\x61\x64min_status\x18\x06 \x01(\x0e\x32\".opi_api.network.v1.InterfaceState\x12\x37\n\x0boper_status\x18\x07 \x01(\x0e\x32\".opi_api.network.v1.InterfaceState\x12\x13\n\x0blast_change\x18\n \x01(\x04\x12\x0f\n\x07logical\x18\x0b \x01(\x08\x12\x12\n\nmanagement\x18\x0c \x01(\x08\x12\x0b\n\x03\x63pu\x18\r \x01(\x08\x12Y\n\x08\x63ounters\x18\x0e \x01(\x0b\x32G.opi_api.network.v1.Interface.Subinterfaces.Subinterface.State.Counters\x1a\xb0\x03\n\x08\x43ounters\x12\x11\n\tin_octets\x18\x01 \x01(\x04\x12\x12\n\nin_packets\x18\x02 \x01(\x04\x12\x17\n\x0fin_unicast_pkts\x18\x03 \x01(\x04\x12\x19\n\x11in_broadcast_pkts\x18\x04 \x01(\x04\x12\x19\n\x11in_multicast_pkts\x18\x05 \x01(\x04\x12\x13\n\x0bin_discards\x18\x06 \x01(\x04\x12\x11\n\tin_errors\x18\x07 \x01(\x04\x12\x19\n\x11in_unknown_protos\x18\x08 \x01(\x04\x12\x15\n\rin_fcs_errors\x18\t \x01(\x04\x12\x12\n\nout_octets\x18\n \x01(\x04\x12\x13\n\x0bout_packets\x18\x0b \x01(\x04\x12\x18\n\x10out_unicast_pkts\x18\x0c \x01(\x04\x12\x1a\n\x12out_broadcast_pkts\x18\r \x01(\x04\x12\x1a\n\x12out_multicast_pkts\x18\x0e \x01(\x04\x12\x14\n\x0cout_discards\x18\x0f \x01(\x04\x12\x12\n\nout_errors\x18\x10 \x01(\x04\x12\x1b\n\x13\x63\x61rrier_transitions\x18\x11 \x01(\x04\x12\x12\n\nlast_clear\x18\x12 \x01(\x04\">\n\nInterfaces\x12\x30\n\tinterface\x18\x01 \x03(\x0b\x32\x1d.opi_api.network.v1.Interface\"&\n\x16NetInterfaceGetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"K\n\x17NetInterfaceGetResponse\x12\x30\n\tinterface\x18\x01 \x01(\x0b\x32\x1d.opi_api.network.v1.Interface\"\x19\n\x17NetInterfaceListRequest\"L\n\x18NetInterfaceListResponse\x12\x30\n\tinterface\x18\x01 \x03(\x0b\x32\x1d.opi_api.network.v1.Interface\"M\n\x19NetInterfaceUpdateRequest\x12\x30\n\tinterface\x18\x01 \x01(\x0b\x32\x1d.opi_api.network.v1.Interface\",\n\x1aNetInterfaceUpdateResponse\x12\x0e\n\x06result\x18\x01 \x01(\r*+\n\rInterfaceType\x12\x0c\n\x08\x45THERNET\x10\x00\x12\x0c\n\x08LOOPBACK\x10\x01*\"\n\x0eInterfaceState\x12\x08\n\x04\x44OWN\x10\x00\x12\x06\n\x02UP\x10\x01\x32\xe4\x02\n\x0cNetInterface\x12l\n\x0fNetInterfaceGet\x12*.opi_api.network.v1.NetInterfaceGetRequest\x1a+.opi_api.network.v1.NetInterfaceGetResponse\"\x00\x12o\n\x10NetInterfaceList\x12+.opi_api.network.v1.NetInterfaceListRequest\x1a,.opi_api.network.v1.NetInterfaceListResponse\"\x00\x12u\n\x12NetInterfaceUpdate\x12-.opi_api.network.v1.NetInterfaceUpdateRequest\x1a..opi_api.network.v1.NetInterfaceUpdateResponse\"\x00\x42\x31Z/github.com/opiproject/opi-api/network/v1/gen/gob\x06proto3')

_INTERFACETYPE = DESCRIPTOR.enum_types_by_name['InterfaceType']
InterfaceType = enum_type_wrapper.EnumTypeWrapper(_INTERFACETYPE)
_INTERFACESTATE = DESCRIPTOR.enum_types_by_name['InterfaceState']
InterfaceState = enum_type_wrapper.EnumTypeWrapper(_INTERFACESTATE)
ETHERNET = 0
LOOPBACK = 1
DOWN = 0
UP = 1


_INTERFACE = DESCRIPTOR.message_types_by_name['Interface']
_INTERFACE_CONFIG = _INTERFACE.nested_types_by_name['Config']
_INTERFACE_STATE = _INTERFACE.nested_types_by_name['State']
_INTERFACE_STATE_COUNTERS = _INTERFACE_STATE.nested_types_by_name['Counters']
_INTERFACE_HOLDTIME = _INTERFACE.nested_types_by_name['HoldTime']
_INTERFACE_HOLDTIME_CONFIG = _INTERFACE_HOLDTIME.nested_types_by_name['Config']
_INTERFACE_HOLDTIME_STATE = _INTERFACE_HOLDTIME.nested_types_by_name['State']
_INTERFACE_SUBINTERFACES = _INTERFACE.nested_types_by_name['Subinterfaces']
_INTERFACE_SUBINTERFACES_SUBINTERFACE = _INTERFACE_SUBINTERFACES.nested_types_by_name['Subinterface']
_INTERFACE_SUBINTERFACES_SUBINTERFACE_CONFIG = _INTERFACE_SUBINTERFACES_SUBINTERFACE.nested_types_by_name['Config']
_INTERFACE_SUBINTERFACES_SUBINTERFACE_STATE = _INTERFACE_SUBINTERFACES_SUBINTERFACE.nested_types_by_name['State']
_INTERFACE_SUBINTERFACES_SUBINTERFACE_STATE_COUNTERS = _INTERFACE_SUBINTERFACES_SUBINTERFACE_STATE.nested_types_by_name['Counters']
_INTERFACES = DESCRIPTOR.message_types_by_name['Interfaces']
_NETINTERFACEGETREQUEST = DESCRIPTOR.message_types_by_name['NetInterfaceGetRequest']
_NETINTERFACEGETRESPONSE = DESCRIPTOR.message_types_by_name['NetInterfaceGetResponse']
_NETINTERFACELISTREQUEST = DESCRIPTOR.message_types_by_name['NetInterfaceListRequest']
_NETINTERFACELISTRESPONSE = DESCRIPTOR.message_types_by_name['NetInterfaceListResponse']
_NETINTERFACEUPDATEREQUEST = DESCRIPTOR.message_types_by_name['NetInterfaceUpdateRequest']
_NETINTERFACEUPDATERESPONSE = DESCRIPTOR.message_types_by_name['NetInterfaceUpdateResponse']
Interface = _reflection.GeneratedProtocolMessageType('Interface', (_message.Message,), {

  'Config' : _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
    'DESCRIPTOR' : _INTERFACE_CONFIG,
    '__module__' : 'openconfig_interfaces_pb2'
    # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interface.Config)
    })
  ,

  'State' : _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {

    'Counters' : _reflection.GeneratedProtocolMessageType('Counters', (_message.Message,), {
      'DESCRIPTOR' : _INTERFACE_STATE_COUNTERS,
      '__module__' : 'openconfig_interfaces_pb2'
      # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interface.State.Counters)
      })
    ,
    'DESCRIPTOR' : _INTERFACE_STATE,
    '__module__' : 'openconfig_interfaces_pb2'
    # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interface.State)
    })
  ,

  'HoldTime' : _reflection.GeneratedProtocolMessageType('HoldTime', (_message.Message,), {

    'Config' : _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
      'DESCRIPTOR' : _INTERFACE_HOLDTIME_CONFIG,
      '__module__' : 'openconfig_interfaces_pb2'
      # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interface.HoldTime.Config)
      })
    ,

    'State' : _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
      'DESCRIPTOR' : _INTERFACE_HOLDTIME_STATE,
      '__module__' : 'openconfig_interfaces_pb2'
      # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interface.HoldTime.State)
      })
    ,
    'DESCRIPTOR' : _INTERFACE_HOLDTIME,
    '__module__' : 'openconfig_interfaces_pb2'
    # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interface.HoldTime)
    })
  ,

  'Subinterfaces' : _reflection.GeneratedProtocolMessageType('Subinterfaces', (_message.Message,), {

    'Subinterface' : _reflection.GeneratedProtocolMessageType('Subinterface', (_message.Message,), {

      'Config' : _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
        'DESCRIPTOR' : _INTERFACE_SUBINTERFACES_SUBINTERFACE_CONFIG,
        '__module__' : 'openconfig_interfaces_pb2'
        # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interface.Subinterfaces.Subinterface.Config)
        })
      ,

      'State' : _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {

        'Counters' : _reflection.GeneratedProtocolMessageType('Counters', (_message.Message,), {
          'DESCRIPTOR' : _INTERFACE_SUBINTERFACES_SUBINTERFACE_STATE_COUNTERS,
          '__module__' : 'openconfig_interfaces_pb2'
          # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interface.Subinterfaces.Subinterface.State.Counters)
          })
        ,
        'DESCRIPTOR' : _INTERFACE_SUBINTERFACES_SUBINTERFACE_STATE,
        '__module__' : 'openconfig_interfaces_pb2'
        # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interface.Subinterfaces.Subinterface.State)
        })
      ,
      'DESCRIPTOR' : _INTERFACE_SUBINTERFACES_SUBINTERFACE,
      '__module__' : 'openconfig_interfaces_pb2'
      # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interface.Subinterfaces.Subinterface)
      })
    ,
    'DESCRIPTOR' : _INTERFACE_SUBINTERFACES,
    '__module__' : 'openconfig_interfaces_pb2'
    # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interface.Subinterfaces)
    })
  ,
  'DESCRIPTOR' : _INTERFACE,
  '__module__' : 'openconfig_interfaces_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interface)
  })
_sym_db.RegisterMessage(Interface)
_sym_db.RegisterMessage(Interface.Config)
_sym_db.RegisterMessage(Interface.State)
_sym_db.RegisterMessage(Interface.State.Counters)
_sym_db.RegisterMessage(Interface.HoldTime)
_sym_db.RegisterMessage(Interface.HoldTime.Config)
_sym_db.RegisterMessage(Interface.HoldTime.State)
_sym_db.RegisterMessage(Interface.Subinterfaces)
_sym_db.RegisterMessage(Interface.Subinterfaces.Subinterface)
_sym_db.RegisterMessage(Interface.Subinterfaces.Subinterface.Config)
_sym_db.RegisterMessage(Interface.Subinterfaces.Subinterface.State)
_sym_db.RegisterMessage(Interface.Subinterfaces.Subinterface.State.Counters)

Interfaces = _reflection.GeneratedProtocolMessageType('Interfaces', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACES,
  '__module__' : 'openconfig_interfaces_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.v1.Interfaces)
  })
_sym_db.RegisterMessage(Interfaces)

NetInterfaceGetRequest = _reflection.GeneratedProtocolMessageType('NetInterfaceGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _NETINTERFACEGETREQUEST,
  '__module__' : 'openconfig_interfaces_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.v1.NetInterfaceGetRequest)
  })
_sym_db.RegisterMessage(NetInterfaceGetRequest)

NetInterfaceGetResponse = _reflection.GeneratedProtocolMessageType('NetInterfaceGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _NETINTERFACEGETRESPONSE,
  '__module__' : 'openconfig_interfaces_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.v1.NetInterfaceGetResponse)
  })
_sym_db.RegisterMessage(NetInterfaceGetResponse)

NetInterfaceListRequest = _reflection.GeneratedProtocolMessageType('NetInterfaceListRequest', (_message.Message,), {
  'DESCRIPTOR' : _NETINTERFACELISTREQUEST,
  '__module__' : 'openconfig_interfaces_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.v1.NetInterfaceListRequest)
  })
_sym_db.RegisterMessage(NetInterfaceListRequest)

NetInterfaceListResponse = _reflection.GeneratedProtocolMessageType('NetInterfaceListResponse', (_message.Message,), {
  'DESCRIPTOR' : _NETINTERFACELISTRESPONSE,
  '__module__' : 'openconfig_interfaces_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.v1.NetInterfaceListResponse)
  })
_sym_db.RegisterMessage(NetInterfaceListResponse)

NetInterfaceUpdateRequest = _reflection.GeneratedProtocolMessageType('NetInterfaceUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _NETINTERFACEUPDATEREQUEST,
  '__module__' : 'openconfig_interfaces_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.v1.NetInterfaceUpdateRequest)
  })
_sym_db.RegisterMessage(NetInterfaceUpdateRequest)

NetInterfaceUpdateResponse = _reflection.GeneratedProtocolMessageType('NetInterfaceUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _NETINTERFACEUPDATERESPONSE,
  '__module__' : 'openconfig_interfaces_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.v1.NetInterfaceUpdateResponse)
  })
_sym_db.RegisterMessage(NetInterfaceUpdateResponse)

_NETINTERFACE = DESCRIPTOR.services_by_name['NetInterface']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/opiproject/opi-api/network/v1/gen/go'
  _INTERFACETYPE._serialized_start=3086
  _INTERFACETYPE._serialized_end=3129
  _INTERFACESTATE._serialized_start=3131
  _INTERFACESTATE._serialized_end=3165
  _INTERFACE._serialized_start=52
  _INTERFACE._serialized_end=2673
  _INTERFACE_CONFIG._serialized_start=312
  _INTERFACE_CONFIG._serialized_end=457
  _INTERFACE_STATE._serialized_start=460
  _INTERFACE_STATE._serialized_end=1306
  _INTERFACE_STATE_COUNTERS._serialized_start=874
  _INTERFACE_STATE_COUNTERS._serialized_end=1306
  _INTERFACE_HOLDTIME._serialized_start=1309
  _INTERFACE_HOLDTIME._serialized_end=1514
  _INTERFACE_HOLDTIME_CONFIG._serialized_start=1445
  _INTERFACE_HOLDTIME_CONFIG._serialized_end=1479
  _INTERFACE_HOLDTIME_STATE._serialized_start=1481
  _INTERFACE_HOLDTIME_STATE._serialized_end=1514
  _INTERFACE_SUBINTERFACES._serialized_start=1517
  _INTERFACE_SUBINTERFACES._serialized_end=2673
  _INTERFACE_SUBINTERFACES_SUBINTERFACE._serialized_start=1615
  _INTERFACE_SUBINTERFACES_SUBINTERFACE._serialized_end=2673
  _INTERFACE_SUBINTERFACES_SUBINTERFACE_CONFIG._serialized_start=1806
  _INTERFACE_SUBINTERFACES_SUBINTERFACE_CONFIG._serialized_end=1867
  _INTERFACE_SUBINTERFACES_SUBINTERFACE_STATE._serialized_start=1870
  _INTERFACE_SUBINTERFACES_SUBINTERFACE_STATE._serialized_end=2673
  _INTERFACE_SUBINTERFACES_SUBINTERFACE_STATE_COUNTERS._serialized_start=874
  _INTERFACE_SUBINTERFACES_SUBINTERFACE_STATE_COUNTERS._serialized_end=1306
  _INTERFACES._serialized_start=2675
  _INTERFACES._serialized_end=2737
  _NETINTERFACEGETREQUEST._serialized_start=2739
  _NETINTERFACEGETREQUEST._serialized_end=2777
  _NETINTERFACEGETRESPONSE._serialized_start=2779
  _NETINTERFACEGETRESPONSE._serialized_end=2854
  _NETINTERFACELISTREQUEST._serialized_start=2856
  _NETINTERFACELISTREQUEST._serialized_end=2881
  _NETINTERFACELISTRESPONSE._serialized_start=2883
  _NETINTERFACELISTRESPONSE._serialized_end=2959
  _NETINTERFACEUPDATEREQUEST._serialized_start=2961
  _NETINTERFACEUPDATEREQUEST._serialized_end=3038
  _NETINTERFACEUPDATERESPONSE._serialized_start=3040
  _NETINTERFACEUPDATERESPONSE._serialized_end=3084
  _NETINTERFACE._serialized_start=3168
  _NETINTERFACE._serialized_end=3524
# @@protoc_insertion_point(module_scope)
