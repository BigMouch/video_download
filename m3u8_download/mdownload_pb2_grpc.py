# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import mdownload_pb2 as mdownload__pb2


class mDownloadStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.addUri = channel.unary_unary(
        '/protocol.mDownload/addUri',
        request_serializer=mdownload__pb2.requestData.SerializeToString,
        response_deserializer=mdownload__pb2.responseData.FromString,
        )


class mDownloadServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def addUri(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_mDownloadServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'addUri': grpc.unary_unary_rpc_method_handler(
          servicer.addUri,
          request_deserializer=mdownload__pb2.requestData.FromString,
          response_serializer=mdownload__pb2.responseData.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protocol.mDownload', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))