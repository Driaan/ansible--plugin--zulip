#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import zulip
import json

DOCUMENTATION = '''
author: Driaan de Beste
name: zulip
type: notification
requirements:
- zulip bot
- zulip bot zuliprc file
- zulip (python library)
short_description: Sends messages to a zulip server
options:
zuliprc_file_path:
description: path to zuliprc file
default: "./zuliprc"
type: string
notify_users:
description: list of users to notify in zulip
required: false (either notify_users or notify_streams is required)
type: list of strings
notify_streams:
description: list of streams to notify in zulip
required: false (either notify_users or notify_streams is required)
type: list of strings
stream_topic:
description: name of the topic if sending to a stream
required: false
default: "ansible notification"
type: string
content:
description: message content to send to zulip
required: true
type: string
'''


def main():
  module = AnsibleModule(
    argument_spec=dict(
      zuliprc_file_path=dict(default="./zuliprc"),
      notify_users=dict(required=False, type="list"),
      notify_streams=dict(required=False, type="list"),
      stream_topic=dict(default="ansible notification"),
      content=dict(required=True),
      )
    )

  content = module.params.get('content')
  zuliprc_file_path = module.params.get('zuliprc_file_path')
  notify_users = module.params.get('notify_users')
  stream_topic = module.params.get('stream_topic')
  notify_streams = module.params.get('notify_streams')
  zulip_client = zulip.Client(config_file=zuliprc_file_path)
  status = ''

  if notify_streams is not None:
    streams_status = zulip_client.send_message(
                   {'type': 'stream',
                    'content': content,
                    'subject': stream_topic,
                    'to': list(notify_streams)})
    status += json.dumps(streams_status)

  if notify_users is not None:
    users_status = zulip_client.send_message(
                    {'type':
                     'private',
                     'content': content,
                     'to': list(notify_users)})
    status += json.dumps(users_status)

  if notify_streams is not None or notify_users is not None:
    module.exit_json(changed=True, msg=status)
  else:
    module.fail_json(
      msg="Destination not specified. Specify either notify_users or notify_streams")

if __name__ == '__main__':
  main()
