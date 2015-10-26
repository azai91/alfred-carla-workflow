from pushbullet import Pushbullet
from workflow import Workflow, PasswordNotFound, ICON_TRASH, ICON_WARNING, ICON_USER
from config import api_key

pb = Pushbullet(api_key)

def main(_):
  user_input = ""
  options = True if wf.args[0][0] == '>' else False
  show_devices();
  # try:
  #   user_input = wf.args[0][1::].strip() if options else wf.args[0]
  # except:
  #   user_input = wf.args[0]

  # return 0

def show_devices():
  for device in pb.devices
    wf.add_item(title=device['nickname'])

  wf.send_feedback()


if __name__ == '__main__':
  wf.run(main)