#!/usr/bin/env python
"""
Copyright 2012 GroupDocs.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from .models import *
from groupdocs.FileStream import FileStream
from groupdocs.ApiClient import ApiException

class ComparisonApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient
        self.__basePath = "https://api.groupdocs.com/v2.0"

    @property
    def basePath(self):
        return self.__basePath
    
    @basePath.setter
    def basePath(self, value):
        self.__basePath = value

    
    def DownloadResult(self, userId, resultFileId, **kwargs):
        """Download comparison result file

        Args:
            userId, str: User GUID (required)
            resultFileId, str: Comparison result file GUID (required)
            format, str: Comparison result file format (optional)
            
        Returns: stream
        """
        if( userId == None or resultFileId == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['userId', 'resultFileId', 'format']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method DownloadResult" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/comparison/{userId}/comparison/download?resultFileId={resultFileId}&format={format}'.replace('*', '')
        pos = resourcePath.find("?")
        if pos != -1:
            resourcePath = resourcePath[0:pos]
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('resultFileId' in params):
            queryParams['resultFileId'] = self.apiClient.toPathValue(params['resultFileId'])
        if ('format' in params):
            queryParams['format'] = self.apiClient.toPathValue(params['format'])
        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        return self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams, FileStream)
        
    def Compare(self, userId, sourceFileId, targetFileId, callbackUrl, **kwargs):
        """Compare

        Args:
            userId, str: User GUID (required)
            sourceFileId, str: Source File GUID (required)
            targetFileId, str: Target File GUID (required)
            callbackUrl, str: Callback Url (required)
            
        Returns: CompareResponse
        """
        if( userId == None or sourceFileId == None or targetFileId == None or callbackUrl == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['userId', 'sourceFileId', 'targetFileId', 'callbackUrl']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method Compare" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/comparison/{userId}/comparison/compare?source={sourceFileId}&target={targetFileId}&callback={callbackUrl}'.replace('*', '')
        pos = resourcePath.find("?")
        if pos != -1:
            resourcePath = resourcePath[0:pos]
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('sourceFileId' in params):
            queryParams['source'] = self.apiClient.toPathValue(params['sourceFileId'])
        if ('targetFileId' in params):
            queryParams['target'] = self.apiClient.toPathValue(params['targetFileId'])
        if ('callbackUrl' in params):
            queryParams['callback'] = self.apiClient.toPathValue(params['callbackUrl'])
        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CompareResponse')
        return responseObject
        
        
    def GetChanges(self, userId, resultFileId, **kwargs):
        """Get changes

        Args:
            userId, str: User GUID (required)
            resultFileId, str: Comparison result file GUID (required)
            
        Returns: ChangesResponse
        """
        if( userId == None or resultFileId == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['userId', 'resultFileId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetChanges" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/comparison/{userId}/comparison/changes?resultFileId={resultFileId}'.replace('*', '')
        pos = resourcePath.find("?")
        if pos != -1:
            resourcePath = resourcePath[0:pos]
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('resultFileId' in params):
            queryParams['resultFileId'] = self.apiClient.toPathValue(params['resultFileId'])
        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ChangesResponse')
        return responseObject
        
        
    def UpdateChanges(self, userId, resultFileId, body, **kwargs):
        """Update changes

        Args:
            userId, str: User GUID (required)
            resultFileId, str: Comparison result file GUID (required)
            body, List[ChangeInfo]: Comparison changes to update (accept or reject) (required)
            
        Returns: ChangesResponse
        """
        if( userId == None or resultFileId == None or body == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['userId', 'resultFileId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method UpdateChanges" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/comparison/{userId}/comparison/changes?resultFileId={resultFileId}'.replace('*', '')
        pos = resourcePath.find("?")
        if pos != -1:
            resourcePath = resourcePath[0:pos]
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('resultFileId' in params):
            queryParams['resultFileId'] = self.apiClient.toPathValue(params['resultFileId'])
        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ChangesResponse')
        return responseObject
        
        
    def GetDocumentDetails(self, userId, guid, **kwargs):
        """Get document details

        Args:
            userId, str: User GUID (required)
            guid, str: Document GUID (required)
            
        Returns: DocumentDetailsResponse
        """
        if( userId == None or guid == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['userId', 'guid']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetDocumentDetails" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/comparison/{userId}/comparison/document?guid={guid}'.replace('*', '')
        pos = resourcePath.find("?")
        if pos != -1:
            resourcePath = resourcePath[0:pos]
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('guid' in params):
            queryParams['guid'] = self.apiClient.toPathValue(params['guid'])
        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DocumentDetailsResponse')
        return responseObject
        
        
    


