from workflow import Workflow, PasswordNotFound, ICON_TRASH, ICON_WARNING, ICON_USER
from pushbullet import Pushbullet
from config import ACCESS_TOKEN

wf = Workflow()
pb = Pushbullet(ACCESS_TOKEN)

def main(_):
  message = wf.args[0]

  if message[:3] in 'set':
    index = wf.args[0].split(' ')[1]
    wf.store_data('pb_device', pb.devices[int(index)])
  elif message[:4] in 'text':
    device = wf.stored_data('pb_device')
    pb.push_sms(device, '2134657640', message[5:])

if __name__ == '__main__':
  wf.run(main)
