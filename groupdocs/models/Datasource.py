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
"""
class Datasource:
    """
    
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'id': 'float',
            'questionnaire_id': 'float',
            'descr': 'str',
            'fields': 'list[DatasourceField]',
            'created_on': 'int',
            'modified_on': 'int'

        }


        self.id = None # float
        self.questionnaire_id = None # float
        self.descr = None # str
        self.fields = None # list[DatasourceField]
        self.created_on = None # int
        self.modified_on = None # int
        
