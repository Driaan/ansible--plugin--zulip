# Ansible Plugin: [Zulip](https://zulip.com/)

## Installation

To install this plugin locally, clone this repo and copy the file ```zulip.py``` to an ansible module location.
Eg. ```~/.ansible/plugins/modules/zulip.py```.

## Usage

    author: Driaan de Beste
    name: zulip
    type: notification
    requirements:
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

## Development

To run/test this plugin, clone this repo and run ```run_dev.sh```.

