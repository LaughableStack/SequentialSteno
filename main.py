from encode import encode
from decode import decode
encode("im.jpeg","This is a test").save("im.png")
print(decode("im.png"))