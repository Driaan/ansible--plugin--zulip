#!/bin/bash

mkdir -p ~/.ansible/plugins/modules/
cp zulip.py ~/.ansible/plugins/modules/zulip.py
ansible-playbook plugin_test.yml