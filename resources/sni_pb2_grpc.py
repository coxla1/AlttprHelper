# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import resources.sni_pb2 as sni__pb2


class DevicesStub(object):
    """////////////////////////////////////////////////////////////////////////////////////////////////
    services
    ////////////////////////////////////////////////////////////////////////////////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListDevices = channel.unary_unary(
                '/Devices/ListDevices',
                request_serializer=sni__pb2.DevicesRequest.SerializeToString,
                response_deserializer=sni__pb2.DevicesResponse.FromString,
                )


class DevicesServicer(object):
    """////////////////////////////////////////////////////////////////////////////////////////////////
    services
    ////////////////////////////////////////////////////////////////////////////////////////////////

    """

    def ListDevices(self, request, context):
        """detect and list devices currently connected to the system:
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DevicesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDevices,
                    request_deserializer=sni__pb2.DevicesRequest.FromString,
                    response_serializer=sni__pb2.DevicesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Devices', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Devices(object):
    """////////////////////////////////////////////////////////////////////////////////////////////////
    services
    ////////////////////////////////////////////////////////////////////////////////////////////////

    """

    @staticmethod
    def ListDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Devices/ListDevices',
            sni__pb2.DevicesRequest.SerializeToString,
            sni__pb2.DevicesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DeviceControlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ResetSystem = channel.unary_unary(
                '/DeviceControl/ResetSystem',
                request_serializer=sni__pb2.ResetSystemRequest.SerializeToString,
                response_deserializer=sni__pb2.ResetSystemResponse.FromString,
                )
        self.ResetToMenu = channel.unary_unary(
                '/DeviceControl/ResetToMenu',
                request_serializer=sni__pb2.ResetToMenuRequest.SerializeToString,
                response_deserializer=sni__pb2.ResetToMenuResponse.FromString,
                )
        self.PauseUnpauseEmulation = channel.unary_unary(
                '/DeviceControl/PauseUnpauseEmulation',
                request_serializer=sni__pb2.PauseEmulationRequest.SerializeToString,
                response_deserializer=sni__pb2.PauseEmulationResponse.FromString,
                )
        self.PauseToggleEmulation = channel.unary_unary(
                '/DeviceControl/PauseToggleEmulation',
                request_serializer=sni__pb2.PauseToggleEmulationRequest.SerializeToString,
                response_deserializer=sni__pb2.PauseToggleEmulationResponse.FromString,
                )


class DeviceControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ResetSystem(self, request, context):
        """only available if DeviceCapability ResetSystem is present
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetToMenu(self, request, context):
        """only available if DeviceCapability ResetToMenu is present
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PauseUnpauseEmulation(self, request, context):
        """only available if DeviceCapability PauseUnpauseEmulation is present
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PauseToggleEmulation(self, request, context):
        """only available if DeviceCapability PauseToggleEmulation is present
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ResetSystem': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetSystem,
                    request_deserializer=sni__pb2.ResetSystemRequest.FromString,
                    response_serializer=sni__pb2.ResetSystemResponse.SerializeToString,
            ),
            'ResetToMenu': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetToMenu,
                    request_deserializer=sni__pb2.ResetToMenuRequest.FromString,
                    response_serializer=sni__pb2.ResetToMenuResponse.SerializeToString,
            ),
            'PauseUnpauseEmulation': grpc.unary_unary_rpc_method_handler(
                    servicer.PauseUnpauseEmulation,
                    request_deserializer=sni__pb2.PauseEmulationRequest.FromString,
                    response_serializer=sni__pb2.PauseEmulationResponse.SerializeToString,
            ),
            'PauseToggleEmulation': grpc.unary_unary_rpc_method_handler(
                    servicer.PauseToggleEmulation,
                    request_deserializer=sni__pb2.PauseToggleEmulationRequest.FromString,
                    response_serializer=sni__pb2.PauseToggleEmulationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DeviceControl', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeviceControl(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ResetSystem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceControl/ResetSystem',
            sni__pb2.ResetSystemRequest.SerializeToString,
            sni__pb2.ResetSystemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetToMenu(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceControl/ResetToMenu',
            sni__pb2.ResetToMenuRequest.SerializeToString,
            sni__pb2.ResetToMenuResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PauseUnpauseEmulation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceControl/PauseUnpauseEmulation',
            sni__pb2.PauseEmulationRequest.SerializeToString,
            sni__pb2.PauseEmulationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PauseToggleEmulation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceControl/PauseToggleEmulation',
            sni__pb2.PauseToggleEmulationRequest.SerializeToString,
            sni__pb2.PauseToggleEmulationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DeviceMemoryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MappingDetect = channel.unary_unary(
                '/DeviceMemory/MappingDetect',
                request_serializer=sni__pb2.DetectMemoryMappingRequest.SerializeToString,
                response_deserializer=sni__pb2.DetectMemoryMappingResponse.FromString,
                )
        self.SingleRead = channel.unary_unary(
                '/DeviceMemory/SingleRead',
                request_serializer=sni__pb2.SingleReadMemoryRequest.SerializeToString,
                response_deserializer=sni__pb2.SingleReadMemoryResponse.FromString,
                )
        self.SingleWrite = channel.unary_unary(
                '/DeviceMemory/SingleWrite',
                request_serializer=sni__pb2.SingleWriteMemoryRequest.SerializeToString,
                response_deserializer=sni__pb2.SingleWriteMemoryResponse.FromString,
                )
        self.MultiRead = channel.unary_unary(
                '/DeviceMemory/MultiRead',
                request_serializer=sni__pb2.MultiReadMemoryRequest.SerializeToString,
                response_deserializer=sni__pb2.MultiReadMemoryResponse.FromString,
                )
        self.MultiWrite = channel.unary_unary(
                '/DeviceMemory/MultiWrite',
                request_serializer=sni__pb2.MultiWriteMemoryRequest.SerializeToString,
                response_deserializer=sni__pb2.MultiWriteMemoryResponse.FromString,
                )
        self.StreamRead = channel.stream_stream(
                '/DeviceMemory/StreamRead',
                request_serializer=sni__pb2.MultiReadMemoryRequest.SerializeToString,
                response_deserializer=sni__pb2.MultiReadMemoryResponse.FromString,
                )
        self.StreamWrite = channel.stream_stream(
                '/DeviceMemory/StreamWrite',
                request_serializer=sni__pb2.MultiWriteMemoryRequest.SerializeToString,
                response_deserializer=sni__pb2.MultiWriteMemoryResponse.FromString,
                )


class DeviceMemoryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MappingDetect(self, request, context):
        """detect the current memory mapping for the given device by reading $00:FFB0 header:
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SingleRead(self, request, context):
        """read a single memory segment with a given size from the given device:
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SingleWrite(self, request, context):
        """write a single memory segment with given data to the given device:
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiRead(self, request, context):
        """read multiple memory segments with given sizes from the given device:
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiWrite(self, request, context):
        """write multiple memory segments with given data to the given device:
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamRead(self, request_iterator, context):
        """stream read multiple memory segments with given sizes from the given device:
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamWrite(self, request_iterator, context):
        """stream write multiple memory segments with given data to the given device:
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceMemoryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MappingDetect': grpc.unary_unary_rpc_method_handler(
                    servicer.MappingDetect,
                    request_deserializer=sni__pb2.DetectMemoryMappingRequest.FromString,
                    response_serializer=sni__pb2.DetectMemoryMappingResponse.SerializeToString,
            ),
            'SingleRead': grpc.unary_unary_rpc_method_handler(
                    servicer.SingleRead,
                    request_deserializer=sni__pb2.SingleReadMemoryRequest.FromString,
                    response_serializer=sni__pb2.SingleReadMemoryResponse.SerializeToString,
            ),
            'SingleWrite': grpc.unary_unary_rpc_method_handler(
                    servicer.SingleWrite,
                    request_deserializer=sni__pb2.SingleWriteMemoryRequest.FromString,
                    response_serializer=sni__pb2.SingleWriteMemoryResponse.SerializeToString,
            ),
            'MultiRead': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiRead,
                    request_deserializer=sni__pb2.MultiReadMemoryRequest.FromString,
                    response_serializer=sni__pb2.MultiReadMemoryResponse.SerializeToString,
            ),
            'MultiWrite': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiWrite,
                    request_deserializer=sni__pb2.MultiWriteMemoryRequest.FromString,
                    response_serializer=sni__pb2.MultiWriteMemoryResponse.SerializeToString,
            ),
            'StreamRead': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamRead,
                    request_deserializer=sni__pb2.MultiReadMemoryRequest.FromString,
                    response_serializer=sni__pb2.MultiReadMemoryResponse.SerializeToString,
            ),
            'StreamWrite': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamWrite,
                    request_deserializer=sni__pb2.MultiWriteMemoryRequest.FromString,
                    response_serializer=sni__pb2.MultiWriteMemoryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DeviceMemory', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeviceMemory(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MappingDetect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceMemory/MappingDetect',
            sni__pb2.DetectMemoryMappingRequest.SerializeToString,
            sni__pb2.DetectMemoryMappingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SingleRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceMemory/SingleRead',
            sni__pb2.SingleReadMemoryRequest.SerializeToString,
            sni__pb2.SingleReadMemoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SingleWrite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceMemory/SingleWrite',
            sni__pb2.SingleWriteMemoryRequest.SerializeToString,
            sni__pb2.SingleWriteMemoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceMemory/MultiRead',
            sni__pb2.MultiReadMemoryRequest.SerializeToString,
            sni__pb2.MultiReadMemoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiWrite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceMemory/MultiWrite',
            sni__pb2.MultiWriteMemoryRequest.SerializeToString,
            sni__pb2.MultiWriteMemoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamRead(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/DeviceMemory/StreamRead',
            sni__pb2.MultiReadMemoryRequest.SerializeToString,
            sni__pb2.MultiReadMemoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamWrite(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/DeviceMemory/StreamWrite',
            sni__pb2.MultiWriteMemoryRequest.SerializeToString,
            sni__pb2.MultiWriteMemoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DeviceFilesystemStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadDirectory = channel.unary_unary(
                '/DeviceFilesystem/ReadDirectory',
                request_serializer=sni__pb2.ReadDirectoryRequest.SerializeToString,
                response_deserializer=sni__pb2.ReadDirectoryResponse.FromString,
                )
        self.MakeDirectory = channel.unary_unary(
                '/DeviceFilesystem/MakeDirectory',
                request_serializer=sni__pb2.MakeDirectoryRequest.SerializeToString,
                response_deserializer=sni__pb2.MakeDirectoryResponse.FromString,
                )
        self.RemoveFile = channel.unary_unary(
                '/DeviceFilesystem/RemoveFile',
                request_serializer=sni__pb2.RemoveFileRequest.SerializeToString,
                response_deserializer=sni__pb2.RemoveFileResponse.FromString,
                )
        self.RenameFile = channel.unary_unary(
                '/DeviceFilesystem/RenameFile',
                request_serializer=sni__pb2.RenameFileRequest.SerializeToString,
                response_deserializer=sni__pb2.RenameFileResponse.FromString,
                )
        self.PutFile = channel.unary_unary(
                '/DeviceFilesystem/PutFile',
                request_serializer=sni__pb2.PutFileRequest.SerializeToString,
                response_deserializer=sni__pb2.PutFileResponse.FromString,
                )
        self.GetFile = channel.unary_unary(
                '/DeviceFilesystem/GetFile',
                request_serializer=sni__pb2.GetFileRequest.SerializeToString,
                response_deserializer=sni__pb2.GetFileResponse.FromString,
                )
        self.BootFile = channel.unary_unary(
                '/DeviceFilesystem/BootFile',
                request_serializer=sni__pb2.BootFileRequest.SerializeToString,
                response_deserializer=sni__pb2.BootFileResponse.FromString,
                )


class DeviceFilesystemServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReadDirectory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MakeDirectory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RenameFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PutFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BootFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceFilesystemServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadDirectory,
                    request_deserializer=sni__pb2.ReadDirectoryRequest.FromString,
                    response_serializer=sni__pb2.ReadDirectoryResponse.SerializeToString,
            ),
            'MakeDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.MakeDirectory,
                    request_deserializer=sni__pb2.MakeDirectoryRequest.FromString,
                    response_serializer=sni__pb2.MakeDirectoryResponse.SerializeToString,
            ),
            'RemoveFile': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveFile,
                    request_deserializer=sni__pb2.RemoveFileRequest.FromString,
                    response_serializer=sni__pb2.RemoveFileResponse.SerializeToString,
            ),
            'RenameFile': grpc.unary_unary_rpc_method_handler(
                    servicer.RenameFile,
                    request_deserializer=sni__pb2.RenameFileRequest.FromString,
                    response_serializer=sni__pb2.RenameFileResponse.SerializeToString,
            ),
            'PutFile': grpc.unary_unary_rpc_method_handler(
                    servicer.PutFile,
                    request_deserializer=sni__pb2.PutFileRequest.FromString,
                    response_serializer=sni__pb2.PutFileResponse.SerializeToString,
            ),
            'GetFile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFile,
                    request_deserializer=sni__pb2.GetFileRequest.FromString,
                    response_serializer=sni__pb2.GetFileResponse.SerializeToString,
            ),
            'BootFile': grpc.unary_unary_rpc_method_handler(
                    servicer.BootFile,
                    request_deserializer=sni__pb2.BootFileRequest.FromString,
                    response_serializer=sni__pb2.BootFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DeviceFilesystem', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeviceFilesystem(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReadDirectory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceFilesystem/ReadDirectory',
            sni__pb2.ReadDirectoryRequest.SerializeToString,
            sni__pb2.ReadDirectoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MakeDirectory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceFilesystem/MakeDirectory',
            sni__pb2.MakeDirectoryRequest.SerializeToString,
            sni__pb2.MakeDirectoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceFilesystem/RemoveFile',
            sni__pb2.RemoveFileRequest.SerializeToString,
            sni__pb2.RemoveFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RenameFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceFilesystem/RenameFile',
            sni__pb2.RenameFileRequest.SerializeToString,
            sni__pb2.RenameFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PutFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceFilesystem/PutFile',
            sni__pb2.PutFileRequest.SerializeToString,
            sni__pb2.PutFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceFilesystem/GetFile',
            sni__pb2.GetFileRequest.SerializeToString,
            sni__pb2.GetFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BootFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceFilesystem/BootFile',
            sni__pb2.BootFileRequest.SerializeToString,
            sni__pb2.BootFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DeviceInfoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FetchFields = channel.unary_unary(
                '/DeviceInfo/FetchFields',
                request_serializer=sni__pb2.FieldsRequest.SerializeToString,
                response_deserializer=sni__pb2.FieldsResponse.FromString,
                )


class DeviceInfoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FetchFields(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceInfoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FetchFields': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchFields,
                    request_deserializer=sni__pb2.FieldsRequest.FromString,
                    response_serializer=sni__pb2.FieldsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DeviceInfo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeviceInfo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FetchFields(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceInfo/FetchFields',
            sni__pb2.FieldsRequest.SerializeToString,
            sni__pb2.FieldsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DeviceNWAStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NWACommand = channel.unary_unary(
                '/DeviceNWA/NWACommand',
                request_serializer=sni__pb2.NWACommandRequest.SerializeToString,
                response_deserializer=sni__pb2.NWACommandResponse.FromString,
                )


class DeviceNWAServicer(object):
    """Missing associated documentation comment in .proto file."""

    def NWACommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceNWAServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NWACommand': grpc.unary_unary_rpc_method_handler(
                    servicer.NWACommand,
                    request_deserializer=sni__pb2.NWACommandRequest.FromString,
                    response_serializer=sni__pb2.NWACommandResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DeviceNWA', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeviceNWA(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def NWACommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceNWA/NWACommand',
            sni__pb2.NWACommandRequest.SerializeToString,
            sni__pb2.NWACommandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
