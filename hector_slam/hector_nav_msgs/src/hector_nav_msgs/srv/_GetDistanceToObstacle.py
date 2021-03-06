"""autogenerated by genmsg_py from GetDistanceToObstacleRequest.msg. Do not edit."""
import roslib.message
import struct

import geometry_msgs.msg
import std_msgs.msg

class GetDistanceToObstacleRequest(roslib.message.Message):
  _md5sum = "47dfdbd810b48d0a47b7ad67e4191bcc"
  _type = "hector_nav_msgs/GetDistanceToObstacleRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """




geometry_msgs/PointStamped point

================================================================================
MSG: geometry_msgs/PointStamped
# This represents a Point with reference coordinate frame and timestamp
Header header
Point point

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

"""
  __slots__ = ['point']
  _slot_types = ['geometry_msgs/PointStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       point
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(GetDistanceToObstacleRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.point is None:
        self.point = geometry_msgs.msg.PointStamped()
    else:
      self.point = geometry_msgs.msg.PointStamped()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.point.header.seq, _x.point.header.stamp.secs, _x.point.header.stamp.nsecs))
      _x = self.point.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      _x = self
      buff.write(_struct_3d.pack(_x.point.point.x, _x.point.point.y, _x.point.point.z))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.point is None:
        self.point = geometry_msgs.msg.PointStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.point.header.seq, _x.point.header.stamp.secs, _x.point.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.point.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.point.point.x, _x.point.point.y, _x.point.point.z,) = _struct_3d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.point.header.seq, _x.point.header.stamp.secs, _x.point.header.stamp.nsecs))
      _x = self.point.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x.encode()))
      _x = self
      buff.write(_struct_3d.pack(_x.point.point.x, _x.point.point.y, _x.point.point.z))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      if self.point is None:
        self.point = geometry_msgs.msg.PointStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.point.header.seq, _x.point.header.stamp.secs, _x.point.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.point.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.point.point.x, _x.point.point.y, _x.point.point.z,) = _struct_3d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_3I = struct.Struct("<3I")
_struct_3d = struct.Struct("<3d")
"""autogenerated by genmsg_py from GetDistanceToObstacleResponse.msg. Do not edit."""
import roslib.message
import struct


class GetDistanceToObstacleResponse(roslib.message.Message):
  _md5sum = "6e77fb10f0c8b4833ec273aa9ac74459"
  _type = "hector_nav_msgs/GetDistanceToObstacleResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 distance



"""
  __slots__ = ['distance']
  _slot_types = ['float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       distance
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(GetDistanceToObstacleResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.distance is None:
        self.distance = 0.
    else:
      self.distance = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      buff.write(_struct_f.pack(self.distance))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      start = end
      end += 4
      (self.distance,) = _struct_f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      buff.write(_struct_f.pack(self.distance))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      start = end
      end += 4
      (self.distance,) = _struct_f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_f = struct.Struct("<f")
class GetDistanceToObstacle(roslib.message.ServiceDefinition):
  _type          = 'hector_nav_msgs/GetDistanceToObstacle'
  _md5sum = '39487a7f4ae86519c9734900c4327589'
  _request_class  = GetDistanceToObstacleRequest
  _response_class = GetDistanceToObstacleResponse
