# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from keystoneclient import exceptions as keystone_exceptions

from wildcard.test.test_data import utils


def create_stubbed_exception(cls, status_code=500):
    msg = "Expected failure."

    def fake_init_exception(self, code, message, **kwargs):
        self.code = code
        self.message = message

    def fake_str(self):
        return str(self.message)

    def fake_unicode(self):
        return unicode(self.message)

    cls.__init__ = fake_init_exception
    cls.__str__ = fake_str
    cls.__unicode__ = fake_unicode
    cls.silence_logging = True
    return cls(status_code, msg)


def data(TEST):
    TEST.exceptions = utils.TestDataContainer()

    unauth = keystone_exceptions.Unauthorized
    TEST.exceptions.keystone_unauthorized = create_stubbed_exception(unauth)

    keystone_exception = keystone_exceptions.ClientException
    TEST.exceptions.keystone = create_stubbed_exception(keystone_exception)
