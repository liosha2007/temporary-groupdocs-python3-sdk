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

class SystemApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient
        self.__basePath = "https://dev-api.groupdocs.com/v2.0"

    @property
    def basePath(self):
        return self.__basePath
    
    @basePath.setter
    def basePath(self, value):
        self.__basePath = value

    
    def GetUserPlan(self, callerId, **kwargs):
        """Get user plan

        Args:
            callerId, str: User GUID (required)
            
        Returns: GetPlanResponse
        """
        if( callerId == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['callerId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetUserPlan" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/system/{callerId}/plan'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('callerId' in params):
            replacement = str(self.apiClient.toPathValue(params['callerId']))
            resourcePath = resourcePath.replace('{' + 'callerId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetPlanResponse')
        return responseObject
        
        
    def GetUserSubscriptionPlan(self, callerId, **kwargs):
        """Get user plan

        Args:
            callerId, str: User GUID (required)
            
        Returns: GetUserSubscriptionPlanResponse
        """
        if( callerId == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['callerId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetUserSubscriptionPlan" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/system/{callerId}/subscription'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('callerId' in params):
            replacement = str(self.apiClient.toPathValue(params['callerId']))
            resourcePath = resourcePath.replace('{' + 'callerId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetUserSubscriptionPlanResponse')
        return responseObject
        
        
    def GetSubscriptionPlans(self, callerId, family, **kwargs):
        """Get subscription plans

        Args:
            callerId, str: User GUID (required)
            family, str: Product Family Name (required)
            
        Returns: GetSubscriptionPlansResponse
        """
        if( callerId == None or family == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['callerId', 'family']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetSubscriptionPlans" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/system/{callerId}/plans/{family}?invalidate={invalidate}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('callerId' in params):
            replacement = str(self.apiClient.toPathValue(params['callerId']))
            resourcePath = resourcePath.replace('{' + 'callerId' + '}',
                                                replacement)
        if ('family' in params):
            replacement = str(self.apiClient.toPathValue(params['family']))
            resourcePath = resourcePath.replace('{' + 'family' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetSubscriptionPlansResponse')
        return responseObject
        
        
    def SetSubscriptionPlan(self, userId, productId, body, **kwargs):
        """Set subscription plan user plan

        Args:
            userId, str: User GUID (required)
            productId, str: Product ID (required)
            body, SubscriptionPlanInfo: Subscription Plan (required)
            
        Returns: SetUserSubscriptionPlanResponse
        """
        if( userId == None or productId == None or body == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['userId', 'productId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method SetSubscriptionPlan" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/system/{userId}/subscriptions/{productId}'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        if ('productId' in params):
            replacement = str(self.apiClient.toPathValue(params['productId']))
            resourcePath = resourcePath.replace('{' + 'productId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SetUserSubscriptionPlanResponse')
        return responseObject
        
        
    def GetCountries(self, callerId, **kwargs):
        """Get countries

        Args:
            callerId, str: User GUID (required)
            
        Returns: GetCountriesResponse
        """
        if( callerId == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['callerId']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetCountries" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/system/{callerId}/countries'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('callerId' in params):
            replacement = str(self.apiClient.toPathValue(params['callerId']))
            resourcePath = resourcePath.replace('{' + 'callerId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetCountriesResponse')
        return responseObject
        
        
    def GetStates(self, callerId, countryName, **kwargs):
        """Get states

        Args:
            callerId, str: User GUID (required)
            countryName, str: Country Name (required)
            
        Returns: GetStatesResponse
        """
        if( callerId == None or countryName == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['callerId', 'countryName']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method GetStates" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/system/{callerId}/countries/{countryName}/states'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('callerId' in params):
            replacement = str(self.apiClient.toPathValue(params['callerId']))
            resourcePath = resourcePath.replace('{' + 'callerId' + '}',
                                                replacement)
        if ('countryName' in params):
            replacement = str(self.apiClient.toPathValue(params['countryName']))
            resourcePath = resourcePath.replace('{' + 'countryName' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetStatesResponse')
        return responseObject
        
        
    def SetBillingAddress(self, userId, body, **kwargs):
        """Set user billing address

        Args:
            userId, str: User GUID (required)
            body, BillingAddressInfo: Billing Address (required)
            
        Returns: GetBillingAddressResponse
        """
        if( userId == None or body == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['userId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method SetBillingAddress" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/system/{userId}/billingaddress'.replace('*', '')
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            replacement = str(self.apiClient.toPathValue(params['userId']))
            resourcePath = resourcePath.replace('{' + 'userId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GetBillingAddressResponse')
        return responseObject
        
        
    


