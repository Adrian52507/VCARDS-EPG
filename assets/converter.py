import base64

with open("assets/img/perfil.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

print(encoded_string)