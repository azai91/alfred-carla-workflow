from pushbullet import Pushbullet
from workflow import Workflow, PasswordNotFound, ICON_TRASH, ICON_WARNING, ICON_USER
from config import api_key

wf = Workflow()
pb = Pushbullet(api_key)

def main(_):
  user_input = wf.args[0]
  options = True if wf.args[0][0] == '>' else False

  if options:
    show_devices()
  elif wf.stored_data('pb_device'):
    wf.add_item(title=user_input,
      arg='text %s' % user_input,
      valid=True)
    wf.send_feedback()
    return 0

  return 0

def show_devices():
  for index,device in enumerate(pb.devices):
    wf.add_item(title=device.__dict__['nickname'],
      arg="set %d" % index,
      valid=True)

  wf.send_feedback()


if __name__ == '__main__':
  wf.run(main)