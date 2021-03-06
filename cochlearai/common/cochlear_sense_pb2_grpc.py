# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import cochlear_sense_pb2 as cochlear__sense__pb2


class cochlear_senseStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.event_detection = channel.unary_unary(
        '/cochlear.ai.cochlear_sense/event_detection',
        request_serializer=cochlear__sense__pb2.input.SerializeToString,
        response_deserializer=cochlear__sense__pb2.output.FromString,
        )
    self.gender_detection = channel.unary_unary(
        '/cochlear.ai.cochlear_sense/gender_detection',
        request_serializer=cochlear__sense__pb2.input.SerializeToString,
        response_deserializer=cochlear__sense__pb2.output.FromString,
        )
    self.key_detection = channel.unary_unary(
        '/cochlear.ai.cochlear_sense/key_detection',
        request_serializer=cochlear__sense__pb2.input.SerializeToString,
        response_deserializer=cochlear__sense__pb2.output.FromString,
        )
    self.tempo_detection = channel.unary_unary(
        '/cochlear.ai.cochlear_sense/tempo_detection',
        request_serializer=cochlear__sense__pb2.input.SerializeToString,
        response_deserializer=cochlear__sense__pb2.output.FromString,
        )
    self.genre_detection = channel.unary_unary(
        '/cochlear.ai.cochlear_sense/genre_detection',
        request_serializer=cochlear__sense__pb2.input.SerializeToString,
        response_deserializer=cochlear__sense__pb2.output.FromString,
        )
    self.mood_detection = channel.unary_unary(
        '/cochlear.ai.cochlear_sense/mood_detection',
        request_serializer=cochlear__sense__pb2.input.SerializeToString,
        response_deserializer=cochlear__sense__pb2.output.FromString,
        )
    self.music_speech_others_detection = channel.unary_unary(
        '/cochlear.ai.cochlear_sense/music_speech_others_detection',
        request_serializer=cochlear__sense__pb2.input.SerializeToString,
        response_deserializer=cochlear__sense__pb2.output.FromString,
        )
    self.cochlear_sense = channel.unary_unary(
        '/cochlear.ai.cochlear_sense/cochlear_sense',
        request_serializer=cochlear__sense__pb2.input_sense.SerializeToString,
        response_deserializer=cochlear__sense__pb2.output_sense.FromString,
        )


class cochlear_senseServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def event_detection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def gender_detection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def key_detection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def tempo_detection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def genre_detection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def mood_detection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def music_speech_others_detection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def cochlear_sense(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_cochlear_senseServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'event_detection': grpc.unary_unary_rpc_method_handler(
          servicer.event_detection,
          request_deserializer=cochlear__sense__pb2.input.FromString,
          response_serializer=cochlear__sense__pb2.output.SerializeToString,
      ),
      'gender_detection': grpc.unary_unary_rpc_method_handler(
          servicer.gender_detection,
          request_deserializer=cochlear__sense__pb2.input.FromString,
          response_serializer=cochlear__sense__pb2.output.SerializeToString,
      ),
      'key_detection': grpc.unary_unary_rpc_method_handler(
          servicer.key_detection,
          request_deserializer=cochlear__sense__pb2.input.FromString,
          response_serializer=cochlear__sense__pb2.output.SerializeToString,
      ),
      'tempo_detection': grpc.unary_unary_rpc_method_handler(
          servicer.tempo_detection,
          request_deserializer=cochlear__sense__pb2.input.FromString,
          response_serializer=cochlear__sense__pb2.output.SerializeToString,
      ),
      'genre_detection': grpc.unary_unary_rpc_method_handler(
          servicer.genre_detection,
          request_deserializer=cochlear__sense__pb2.input.FromString,
          response_serializer=cochlear__sense__pb2.output.SerializeToString,
      ),
      'mood_detection': grpc.unary_unary_rpc_method_handler(
          servicer.mood_detection,
          request_deserializer=cochlear__sense__pb2.input.FromString,
          response_serializer=cochlear__sense__pb2.output.SerializeToString,
      ),
      'music_speech_others_detection': grpc.unary_unary_rpc_method_handler(
          servicer.music_speech_others_detection,
          request_deserializer=cochlear__sense__pb2.input.FromString,
          response_serializer=cochlear__sense__pb2.output.SerializeToString,
      ),
      'cochlear_sense': grpc.unary_unary_rpc_method_handler(
          servicer.cochlear_sense,
          request_deserializer=cochlear__sense__pb2.input_sense.FromString,
          response_serializer=cochlear__sense__pb2.output_sense.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cochlear.ai.cochlear_sense', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
