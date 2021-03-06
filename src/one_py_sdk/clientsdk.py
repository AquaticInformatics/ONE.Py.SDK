import requests
from datetime import time
import json
from one_py_sdk.enterprise.core import CoreApi
from one_py_sdk.historian.data import HistorianApi
from one_py_sdk.operations.spreadsheet import SpreadsheetApi
from one_py_sdk.common.library import LibraryApi
from one_py_sdk.enterprise.twin  import DigitalTwinApi
from one_py_sdk.shared.constants import *
from one_py_sdk.enterprise.authentication import AuthenticationApi
from one_py_sdk.shared.helpers.csvhelper import Exporter



class ClientSdk:
	def __init__(self, env="https://api-us.aquaticinformatics.net/"):
		self.Environment = env
		self.Initialize()
	
	def Initialize(self):
		self.Authentication= AuthenticationApi(self.Environment)
		self.DigitalTwin = DigitalTwinApi(self.Environment, self.Authentication)
		self.Spreadsheet = SpreadsheetApi(self.Environment, self.Authentication)
		self.Library = LibraryApi(self.Environment, self.Authentication)
		self.Core = CoreApi(self.Environment, self.Authentication)
		self.Historian = HistorianApi(self.Environment, self.Authentication)
		self.Exporter = Exporter(self.Environment, self.Authentication)
	
	def LoadCurrentUser(self):
		if not self.Authentication.IsAuthenticated:
			print("Not authenticated. Authenticate and try again")
		if(self.Authentication.User.id != None):
			self.Authentication.GetUserInfo()
			self.Authentication.User.CopyFrom(self.Core.GetUser(self.Authentication.User.id))


  

	
 