import grpc
import socket
import logging as lg

import utils
import resources.sni_pb2 as sni
import resources.sni_pb2_grpc as sni_grpc


def detect(variables, log):
    # Start SNI and wait for it
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    flag = sock.connect_ex(('localhost', 8191))
    if flag:
        try:
            thread_sni = utils.Thread(variables['usb-interface'].get())
            thread_sni.start()
        except FileNotFoundError as e:
            lg.error(e)
            log.config(text='Error while starting SNI, check your path')
            return -1

    cnt = 0
    max_cnt = 3
    while flag and cnt < max_cnt:
        flag = sock.connect_ex(('localhost', 8191))
        cnt += 1
        lg.info(f'Attempt {cnt} to connect to SNI')
    sock.close()

    if cnt > max_cnt:
        lg.error('Could not reach port 8191, try to close SNI and check your path')
        log.config(text='Could not reach port 8191, try to close SNI and check your path')
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
        log.config(text=f'FXPak found on {name}')
    else:
        log.config(text='No FXPak found')
        return -1

    variables['uri'].set(uri)

    # # List folders
    # with grpc.insecure_channel('localhost:8191') as channel:
    #     stub = sni_grpc.DeviceFilesystemStub(channel)
    #
    #     entries = ['']
    #     i, j = 0, 1
    #     flag = True
    #
    #     while flag:
    #         k = 0
    #         for dir in entries[i:j]:
    #             current_dir = get_subdirectories(stub, uri, dir)
    #             entries.extend(current_dir)
    #             k += len(current_dir)
    #         i = j
    #         j += k
    #
    #         if k == 0:
    #             flag = False
    #
    #     channel.close()

    # entries[0] = '/'
    # entries.sort()
    # for x in entries:
    #     input_fxpakfolders.insert(END, x)
