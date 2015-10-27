from pushbullet import Pushbullet
from workflow import Workflow, PasswordNotFound, ICON_TRASH, ICON_WARNING, ICON_USER
from config import ACCESS_TOKEN

wf = Workflow()

def main(_):
  user_input = wf.args[0]
  options = True if wf.args[0][0] == '>' else False

  try:
    pb = Pushbullet(ACCESS_TOKEN)
  except:
    show_error('Invalid ACCESS_TOKEN');
    return 0

  if options:
    show_devices(pb.devices)
  elif wf.stored_data('pb_device'):
    wf.add_item(title="Sending Carla",
      subtitle=user_input,
      arg='text %s' % user_input,
      valid=True)
    wf.send_feedback()

  return 0

def show_devices(devices):
  for index,device in enumerate(devices):
    wf.add_item(title=device.__dict__['nickname'],
      arg="set %d" % index,
      valid=True)
  wf.send_feedback()

def show_error(error_name):
  wf.add_item(title=error_name,
    icon=ICON_WARNING)
  wf.send_feedback()

if __name__ == '__main__':
  wf.run(main)