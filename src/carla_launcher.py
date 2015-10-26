from workflow import Workflow, PasswordNotFound, ICON_TRASH, ICON_WARNING, ICON_USER
from pushbullet import Pushbullet
from config import api_key

wf = Workflow()
pb = Pushbullet(api_key)

def main(_):
  message = wf.args[0]

  if message[:3] in 'set':
    index = wf.args[0].split(' ')[1]
    wf.store_data('pb_device', pb.devices[int(index)])
  else:
    device = wf.stored_data('pb_device')
    pb.push_sms(device, '2134657640', message)

if __name__ == '__main__':
  wf.run(main)
