from gmail import GMail, Message
import datetime

now = datetime.datetime.now()

gmail = GMail("kanameichigo998@gmail.com","barondark998x")
msg = Message(
    "Gửi do yêu cầu bài tập",
    to= "barondark998@gmail.com",
    text= "Do yêu cầu bài tập thôi ạ đừng để ý để mail này :>"
)
if now.hour > 7 or (now.hour == 7 and now.second >0):
    gmail.send(msg)