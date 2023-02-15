# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import backend_nvme_tcp_pb2 as backend__nvme__tcp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class NVMfRemoteControllerServiceStub(object):
    """Back End (network-facing) APIs. NVMe/TCP and NVMe/RoCEv2 protocols are covered by this service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateNVMfRemoteController = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/CreateNVMfRemoteController',
                request_serializer=backend__nvme__tcp__pb2.CreateNVMfRemoteControllerRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NVMfRemoteController.FromString,
                )
        self.DeleteNVMfRemoteController = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/DeleteNVMfRemoteController',
                request_serializer=backend__nvme__tcp__pb2.DeleteNVMfRemoteControllerRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdateNVMfRemoteController = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/UpdateNVMfRemoteController',
                request_serializer=backend__nvme__tcp__pb2.UpdateNVMfRemoteControllerRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NVMfRemoteController.FromString,
                )
        self.ListNVMfRemoteControllers = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/ListNVMfRemoteControllers',
                request_serializer=backend__nvme__tcp__pb2.ListNVMfRemoteControllersRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.ListNVMfRemoteControllersResponse.FromString,
                )
        self.GetNVMfRemoteController = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/GetNVMfRemoteController',
                request_serializer=backend__nvme__tcp__pb2.GetNVMfRemoteControllerRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NVMfRemoteController.FromString,
                )
        self.NVMfRemoteControllerReset = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerReset',
                request_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerResetRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.NVMfRemoteControllerStats = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerStats',
                request_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerStatsRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerStatsResponse.FromString,
                )


class NVMfRemoteControllerServiceServicer(object):
    """Back End (network-facing) APIs. NVMe/TCP and NVMe/RoCEv2 protocols are covered by this service.
    """

    def CreateNVMfRemoteController(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNVMfRemoteController(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNVMfRemoteController(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNVMfRemoteControllers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNVMfRemoteController(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NVMfRemoteControllerReset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NVMfRemoteControllerStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NVMfRemoteControllerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateNVMfRemoteController': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNVMfRemoteController,
                    request_deserializer=backend__nvme__tcp__pb2.CreateNVMfRemoteControllerRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NVMfRemoteController.SerializeToString,
            ),
            'DeleteNVMfRemoteController': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNVMfRemoteController,
                    request_deserializer=backend__nvme__tcp__pb2.DeleteNVMfRemoteControllerRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateNVMfRemoteController': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNVMfRemoteController,
                    request_deserializer=backend__nvme__tcp__pb2.UpdateNVMfRemoteControllerRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NVMfRemoteController.SerializeToString,
            ),
            'ListNVMfRemoteControllers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNVMfRemoteControllers,
                    request_deserializer=backend__nvme__tcp__pb2.ListNVMfRemoteControllersRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.ListNVMfRemoteControllersResponse.SerializeToString,
            ),
            'GetNVMfRemoteController': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNVMfRemoteController,
                    request_deserializer=backend__nvme__tcp__pb2.GetNVMfRemoteControllerRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NVMfRemoteController.SerializeToString,
            ),
            'NVMfRemoteControllerReset': grpc.unary_unary_rpc_method_handler(
                    servicer.NVMfRemoteControllerReset,
                    request_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerResetRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'NVMfRemoteControllerStats': grpc.unary_unary_rpc_method_handler(
                    servicer.NVMfRemoteControllerStats,
                    request_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerStatsRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerStatsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'opi_api.storage.v1.NVMfRemoteControllerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NVMfRemoteControllerService(object):
    """Back End (network-facing) APIs. NVMe/TCP and NVMe/RoCEv2 protocols are covered by this service.
    """

    @staticmethod
    def CreateNVMfRemoteController(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/CreateNVMfRemoteController',
            backend__nvme__tcp__pb2.CreateNVMfRemoteControllerRequest.SerializeToString,
            backend__nvme__tcp__pb2.NVMfRemoteController.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteNVMfRemoteController(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/DeleteNVMfRemoteController',
            backend__nvme__tcp__pb2.DeleteNVMfRemoteControllerRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateNVMfRemoteController(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/UpdateNVMfRemoteController',
            backend__nvme__tcp__pb2.UpdateNVMfRemoteControllerRequest.SerializeToString,
            backend__nvme__tcp__pb2.NVMfRemoteController.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNVMfRemoteControllers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/ListNVMfRemoteControllers',
            backend__nvme__tcp__pb2.ListNVMfRemoteControllersRequest.SerializeToString,
            backend__nvme__tcp__pb2.ListNVMfRemoteControllersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNVMfRemoteController(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/GetNVMfRemoteController',
            backend__nvme__tcp__pb2.GetNVMfRemoteControllerRequest.SerializeToString,
            backend__nvme__tcp__pb2.NVMfRemoteController.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NVMfRemoteControllerReset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerReset',
            backend__nvme__tcp__pb2.NVMfRemoteControllerResetRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NVMfRemoteControllerStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerStats',
            backend__nvme__tcp__pb2.NVMfRemoteControllerStatsRequest.SerializeToString,
            backend__nvme__tcp__pb2.NVMfRemoteControllerStatsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)