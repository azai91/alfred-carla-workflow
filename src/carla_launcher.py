from workflow import Workflow, PasswordNotFound, ICON_TRASH, ICON_WARNING, ICON_USER
from pushbullet import Pushbullet
from config import api_key

wf = Workflow()
pb = Pushbullet(api_key)

def main(_):
  wf.store_data('pb_device', pb.devices[0])
  pb.push_sms(pb.devices[0], '3108533732', 'Test1')



if __name__ == '__main__':
  wf.run(main)
