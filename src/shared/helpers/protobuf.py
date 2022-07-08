from one_interfaces import apierror_pb2 as apiError
from one_interfaces import apiresponse_pb2 as apiResponse
import google

def DeserializeResponse(response):                
      try:
            pbResponse = apiResponse.ApiResponse()             
            print(pbResponse.ParseFromString(response.content))                             
            return pbResponse
      except(google.protobuf.message.DecodeError):
            pass
     
     
            
    
      
    