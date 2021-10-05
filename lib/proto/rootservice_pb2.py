# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/rootservice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as proto_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/rootservice.proto',
  package='bluetooth.facade',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17proto/rootservice.proto\x12\x10\x62luetooth.facade\x1a\x12proto/common.proto\"Q\n\x11StartStackRequest\x12<\n\x11module_under_test\x18\x01 \x01(\x0e\x32!.bluetooth.facade.BluetoothModule\"\x14\n\x12StartStackResponse\"\x12\n\x10StopStackRequest\"\x13\n\x11StopStackResponse*Z\n\x0f\x42luetoothModule\x12\x07\n\x03HAL\x10\x00\x12\x07\n\x03HCI\x10\x01\x12\x12\n\x0eHCI_INTERFACES\x10\x02\x12\t\n\x05L2CAP\x10\x03\x12\x0c\n\x08SECURITY\x10\x04\x12\x08\n\x04SHIM\x10\x05\x32\xbf\x01\n\nRootFacade\x12Y\n\nStartStack\x12#.bluetooth.facade.StartStackRequest\x1a$.bluetooth.facade.StartStackResponse\"\x00\x12V\n\tStopStack\x12\".bluetooth.facade.StopStackRequest\x1a#.bluetooth.facade.StopStackResponse\"\x00\x32\x65\n\x10ReadOnlyProperty\x12Q\n\x10ReadLocalAddress\x12\x17.bluetooth.facade.Empty\x1a\".bluetooth.facade.BluetoothAddress\"\x00\x62\x06proto3'
  ,
  dependencies=[proto_dot_common__pb2.DESCRIPTOR,])

_BLUETOOTHMODULE = _descriptor.EnumDescriptor(
  name='BluetoothModule',
  full_name='bluetooth.facade.BluetoothModule',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HCI', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HCI_INTERFACES', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='L2CAP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SECURITY', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHIM', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=211,
  serialized_end=301,
)
_sym_db.RegisterEnumDescriptor(_BLUETOOTHMODULE)

BluetoothModule = enum_type_wrapper.EnumTypeWrapper(_BLUETOOTHMODULE)
HAL = 0
HCI = 1
HCI_INTERFACES = 2
L2CAP = 3
SECURITY = 4
SHIM = 5



_STARTSTACKREQUEST = _descriptor.Descriptor(
  name='StartStackRequest',
  full_name='bluetooth.facade.StartStackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='module_under_test', full_name='bluetooth.facade.StartStackRequest.module_under_test', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=146,
)


_STARTSTACKRESPONSE = _descriptor.Descriptor(
  name='StartStackResponse',
  full_name='bluetooth.facade.StartStackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=168,
)


_STOPSTACKREQUEST = _descriptor.Descriptor(
  name='StopStackRequest',
  full_name='bluetooth.facade.StopStackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=188,
)


_STOPSTACKRESPONSE = _descriptor.Descriptor(
  name='StopStackResponse',
  full_name='bluetooth.facade.StopStackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=209,
)

_STARTSTACKREQUEST.fields_by_name['module_under_test'].enum_type = _BLUETOOTHMODULE
DESCRIPTOR.message_types_by_name['StartStackRequest'] = _STARTSTACKREQUEST
DESCRIPTOR.message_types_by_name['StartStackResponse'] = _STARTSTACKRESPONSE
DESCRIPTOR.message_types_by_name['StopStackRequest'] = _STOPSTACKREQUEST
DESCRIPTOR.message_types_by_name['StopStackResponse'] = _STOPSTACKRESPONSE
DESCRIPTOR.enum_types_by_name['BluetoothModule'] = _BLUETOOTHMODULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartStackRequest = _reflection.GeneratedProtocolMessageType('StartStackRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTSTACKREQUEST,
  '__module__' : 'proto.rootservice_pb2'
  # @@protoc_insertion_point(class_scope:bluetooth.facade.StartStackRequest)
  })
_sym_db.RegisterMessage(StartStackRequest)

StartStackResponse = _reflection.GeneratedProtocolMessageType('StartStackResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTSTACKRESPONSE,
  '__module__' : 'proto.rootservice_pb2'
  # @@protoc_insertion_point(class_scope:bluetooth.facade.StartStackResponse)
  })
_sym_db.RegisterMessage(StartStackResponse)

StopStackRequest = _reflection.GeneratedProtocolMessageType('StopStackRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPSTACKREQUEST,
  '__module__' : 'proto.rootservice_pb2'
  # @@protoc_insertion_point(class_scope:bluetooth.facade.StopStackRequest)
  })
_sym_db.RegisterMessage(StopStackRequest)

StopStackResponse = _reflection.GeneratedProtocolMessageType('StopStackResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPSTACKRESPONSE,
  '__module__' : 'proto.rootservice_pb2'
  # @@protoc_insertion_point(class_scope:bluetooth.facade.StopStackResponse)
  })
_sym_db.RegisterMessage(StopStackResponse)



_ROOTFACADE = _descriptor.ServiceDescriptor(
  name='RootFacade',
  full_name='bluetooth.facade.RootFacade',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=304,
  serialized_end=495,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartStack',
    full_name='bluetooth.facade.RootFacade.StartStack',
    index=0,
    containing_service=None,
    input_type=_STARTSTACKREQUEST,
    output_type=_STARTSTACKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopStack',
    full_name='bluetooth.facade.RootFacade.StopStack',
    index=1,
    containing_service=None,
    input_type=_STOPSTACKREQUEST,
    output_type=_STOPSTACKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROOTFACADE)

DESCRIPTOR.services_by_name['RootFacade'] = _ROOTFACADE


_READONLYPROPERTY = _descriptor.ServiceDescriptor(
  name='ReadOnlyProperty',
  full_name='bluetooth.facade.ReadOnlyProperty',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=497,
  serialized_end=598,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReadLocalAddress',
    full_name='bluetooth.facade.ReadOnlyProperty.ReadLocalAddress',
    index=0,
    containing_service=None,
    input_type=proto_dot_common__pb2._EMPTY,
    output_type=proto_dot_common__pb2._BLUETOOTHADDRESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_READONLYPROPERTY)

DESCRIPTOR.services_by_name['ReadOnlyProperty'] = _READONLYPROPERTY

# @@protoc_insertion_point(module_scope)
