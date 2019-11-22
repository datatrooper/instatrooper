import cv2
import os

nombre_video = "children_ages"
directory = "../outputs/children_ages/images"
path, dirs, files = next(os.walk(directory))
file_count = len(files)



fourcc = cv2.VideoWriter_fourcc('M','J','P','G')

out = cv2.VideoWriter('{}.avi'.format(nombre_video),fourcc, 10.0, (800,600))


for i in range(file_count):
    img_path = os.path.join(directory,f'image({i}).png')
    print(img_path)
    frame = cv2.imread(img_path)
    out.write(frame)

out.release()

# Para enviar por wpp convertir con este link https://webservice.online-convert.com/convert-for-whatsapp
