import pyrebase
def pushcode():
  config = {
    "apiKey": "AIzaSyDCqXgsWsa6SAnAOWek_K4lDA0nV5yNC1Y",
    "authDomain": "SarinCinema.firebaseapp.com",
    "databaseURL": "https://sarincinema.firebaseio.com",
    "storageBucket": "sarincinema.appspot.com"
  }

  firebase = pyrebase.initialize_app(config)

  storage = firebase.storage()

  # storage.child("qrcodes/example.jpg").put("site.png")

  local_file_path = "site.png"
  storage_file_path = "images/qrcode"
  fbupload = storage.child(storage_file_path).put(local_file_path)

  # storage.child("/home/utkarsh/Desktop/Projects/TicketDatabase/site.png").put("site.png")
  # print(storage.child("images").child("qrcode").get_url("a27bedbc-0358-4ea8-92ef-e5e5ce18c0bd"))
  # storage.child("site.png").get_url()