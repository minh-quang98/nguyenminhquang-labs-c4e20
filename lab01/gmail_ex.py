from gmail import GMail, Message
from random import choice

mess = """
    <p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: left;">Em ch&agrave;o thầy em t&ecirc;n bla</p>
<p style="text-align: left;">Xin nghỉ {{sickness}} v&agrave; sẽ học b&ugrave; v&agrave;o 1 ng&agrave;y kh&ocirc;ng xa tới. K&iacute;nh ch&agrave;o thầy&nbsp;</p>
"""

res = [
    "<p>do&nbsp;đau bụng</p>", 
    "<p>do&nbsp;đau&nbsp;đầu</p>", 
    "<p>do&nbsp;đau ch&acirc;n</p>", 
    "<p>do&nbsp;đau tay</p>", 
    "<p>do&nbsp;đau mắt</p>"
]
sickness = choice(res)
html_new = mess.replace("{{sickness}}",sickness)

gmail = GMail('quang<kanameichigo998@gmail.com>','barondark998x')
msg = Message(
    'Gửi cho vui',
    to= '20130075@student.hust.edu.vn',
    html= html_new)
gmail.send(msg)