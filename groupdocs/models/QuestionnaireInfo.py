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
class QuestionnaireInfo:
    """
    
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'resolved_executions': 'int',
            'pages': 'list[QuestionnairePageInfo]',
            'document_ids': 'list[str]',
            'id': 'float',
            'guid': 'str',
            'name': 'str',
            'descr': 'str',
            'status': 'str',
            'assigned_questions': 'int',
            'total_questions': 'int',
            'modified': 'int',
            'expires': 'int',
            'folder': 'str',
            'emails': 'str'

        }


        self.resolved_executions = None # int
        self.pages = None # list[QuestionnairePageInfo]
        self.document_ids = None # list[str]
        self.id = None # float
        self.guid = None # str
        self.name = None # str
        self.descr = None # str
        self.status = None # str
        self.assigned_questions = None # int
        self.total_questions = None # int
        self.modified = None # int
        self.expires = None # int
        self.folder = None # str
        self.emails = None # str
        
