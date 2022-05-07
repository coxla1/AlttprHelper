import grpc
import socket
import logging as lg

import utils
import resources.sni_pb2 as sni
import resources.sni_pb2_grpc as sni_grpc


# Detect FXPak function
def detect(variables, log):
    # Start SNI and wait for it
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    flag = sock.connect_ex(('localhost', 8191))
    if flag:
        t_sni = utils.Thread(variables['usb-interface'].get())
        t_sni.start()

    cnt = 0
    max_cnt = 3
    while flag and cnt < max_cnt:
        flag = sock.connect_ex(('localhost', 8191))
        cnt += 1
        lg.info(f'Attempt {cnt} to connect to SNI')
    sock.close()

    if cnt > max_cnt:
        lg.error('Could not reach port 8191')
        log.config(text='Could not reach port 8191, make sure SNI is running and QUSB2SNES is not')
        return -1

    # Look for FXPak
    with grpc.insecure_channel('localhost:8191') as channel:
        stub = sni_grpc.DevicesStub(channel)
        response = stub.ListDevices(sni.DevicesRequest())
        channel.close()

    uri = None
    for x in response.devices:
        if x.kind == 'fxpakpro':
            uri = x.uri
            name = x.displayName
            lg.info(f'FXPak capabilities {x.capabilities}')
            break

    if uri:
        lg.info(f'FXPak URI : {name}')
        log.config(text=f'FXPak found on {name}')
    else:
        lg.warning(f'No FXPak found')
        log.config(text='No FXPak found')
        return -1

    variables['uri'].set(uri)


# List folder content function
def dir_content(uri, path, t):
    content = []

    with grpc.insecure_channel('localhost:8191') as channel:
        stub = sni_grpc.DeviceFilesystemStub(channel)
        response = stub.ReadDirectory(sni.ReadDirectoryRequest(uri=uri, path=path))
        channel.close()

    # Types : 0 = directory, 1 = files
    for x in response.entries:
        if x.type == t and x.name not in ['.', '..']:
            content.append(f'{x.name}')

    return content


# Send file function (data must be a byte feed)
def send_file(uri, path, data):
    with grpc.insecure_channel('localhost:8191') as channel:
        stub = sni_grpc.DeviceFilesystemStub(channel)
        stub.PutFile(sni.PutFileRequest(uri=uri, path=path, data=data))
        channel.close()

# Boot ROM function
def boot_rom(uri, path):
    with grpc.insecure_channel('localhost:8191') as channel:
        stub = sni_grpc.DeviceFilesystemStub(channel)
        try:
            stub.BootFile(sni.BootFileRequest(uri=uri, path=path))
        except grpc._channel._InactiveRpcError as e:
            # TODO : this is where shit happens
            lg.warning(f'SNI raises an error, but I suspect it to be good: {e}')
        channel.close()
