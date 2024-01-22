from utils.ElgatoApi import ElgatoApi

ELGATO_API_ADDRESS = "192.168.1.47"

def run(args, response):
  lights = ElgatoApi(ELGATO_API_ADDRESS)
  if args[0] == "on":
    lights.turn_on()
    return 'Light started'
  elif args[0] == "off":
    lights.turn_off()
    return 'Light started'