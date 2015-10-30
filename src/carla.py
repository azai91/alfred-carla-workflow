from pushbullet import Pushbullet
from workflow import Workflow, PasswordNotFound, ICON_TRASH, ICON_WARNING, ICON_USER
from config import ACCESS_TOKEN

wf = Workflow()
settings = 'SET DEVICE'

def main():
  user_input = wf.args[0]
  pb = None

  try:
    pb = wf.stored_data('carla_pb')
  except:
    pb = get_pb()

  if not user_input or user_input.lower() in settings.lower():
    wf.add_item(title=settings,
      autocomplete='%s ' % settings,
      valid=False)
  elif ('%s ' % settings).lower() in user_input.lower():
    show_devices(pb.devices)

  wf.send_feedback()

def show_devices(devices):
  for index,device in enumerate(devices):
    wf.add_item(title=device.__dict__['nickname'],
      arg=str(index),
      valid=True)

def get_pb():
  try:
    pb = Pushbullet(ACCESS_TOKEN)
    wf.store_data('carla_pb', pb)
  except:
    show_error('Invalid ACCESS_TOKEN');
    return 0

def show_error(error_name):
  wf.add_item(title=error_name,
    icon=ICON_WARNING)

if __name__ == '__main__':
  main()