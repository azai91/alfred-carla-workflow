from workflow import Workflow, PasswordNotFound, ICON_TRASH, ICON_WARNING, ICON_USER
from pushbullet import Pushbullet
from config import ACCESS_TOKEN, CARLA_PHONE

wf = Workflow()
pb = Pushbullet(ACCESS_TOKEN)

class Carla():

  @classmethod
  def send_message(cls, message):
    device = wf.stored_data('pb_device')
    pb.push_sms(device, CARLA_PHONE , message)

  @classmethod
  def set_device(cls, index):
    wf.store_data('pb_device', pb.devices[int(index)])


