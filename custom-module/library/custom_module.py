#!/usr/bin/python3

import yaml, os
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = """
---
module: custom_module.py
short_description: Create file and add content to remote service
description:
  - filename to be created on the remote service.
  - Also file content
options:
  filename:
    description:
      - filename to be created on the remote service.
  content:
    description:
      - file content.
"""

def main():
  module = AnsibleModule (
    argument_spec = dict(
      filename = dict(type='str', required=True),
      content  = dict(type='str', required=True),
      state    = dict(type='str', default='present', choices=['absent', 'present'])
    ),
    supports_check_mode = True
  )

  filename = module.params['filename']
  content  = module.params['content']
  state    = module.params['state']

  result = dict(
    changed = False
  )

  got    = {}
  wanted = {}

  wanted['filename'] = filename
  wanted['content']  = content
  wanted['state']    = state

  # Populate both `got` and `wanted`.
  try:
    with open(filename, encoding='utf8') as f:
      got['filename'] = filename
      got['state']    = 'present'
      fc = f.read()
      if fc == content:
        got['content'] = fc
  except Exception as e:
    if wanted['state'] == 'absent':
      code    = 404
      message = str(e)
      module.fail_json(
          msg = f"remote service answered with {code}: {message}",
          **result
      )


  if got != wanted:
    result['changed'] = True
    result['diff'] = dict(
      before = yaml.safe_dump(got),
      after  = yaml.safe_dump(wanted)
    )

  if module.check_mode or not result['changed']:
    module.exit_json(**result)

  # Apply changes.
  try:
    if wanted['state'] == 'absent' and got['state'] == 'present':
      os.remove(filename)
      result["output"] = "your data has deleted successfull!"
      module.exit_json(changed=True, success=result, msg=result)

    file = open(filename, "w")
    file.write(content)
    result["output"] = "your data has stored successfull!"
    module.exit_json(changed=True, success=result, msg=result)
  except Exception as e:
    code    = 404
    message = str(e)
    module.fail_json(
        msg = f"remote service answered with {code}: {message}",
        **result
    )


if __name__ == '__main__':
  main()