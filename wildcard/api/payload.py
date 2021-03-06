# vim: tabstop=4 shiftwidth=4 softtabstop=4
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

from payloadclient.client import get_client

from wildcard.api import base


def client(request):
    return get_client(
        1,
        payload_url=base.url_for(request, 'queue'),
        os_auth_token=request.user.token.id,
    )


def queue_create(request, name=None, description=None, disabled=False):
    return client(request).queues.create(
        name=name,
        description=description,
        disabled=disabled,
    )


def queue_get(request, uuid):
    return client(request).queues.get(uuid)


def queue_delete(request, uuid):
    return client(request).queues.delete(uuid)


def queue_list(request):
    return client(request).queues.list()


def queue_update(request, uuid, **kwargs):
    return client(request).queues.update(
        uuid,
        **kwargs
    )
