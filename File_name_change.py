import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


file_path = 'C:/Users/lenovo/Desktop/ML_PRATICE/speed_limit/valid/100'
file_names = os.listdir(file_path)
file_names

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i)+'(v_3)' + '.png'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1

#git Test