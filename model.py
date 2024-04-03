import pickle
import numpy as np
from catboost import CatBoostRegressor

with open("model.pkl", "rb") as model:
    pred_model = pickle.load(model)

gpu_brand_enc = {'amd': 0, 'intel': 1, 'nvidia': 2}
os_enc = {'mac': 0, 'others': 1, 'windows': 2}
cpu_brand_enc = {'amd processor': 0, 'intel core i3': 1, 'intel core i5': 2, 'intel core i7': 3, 'other intel processor': 4}
typename_enc = {'2 in 1 convertible': 0, 'gaming': 1, 'netbook': 2, 'notebook': 3, 'ultrabook': 4, 'workstation': 5}
company_enc = {'acer': 0, 'apple': 1, 'asus': 2, 'chuwi': 3, 'dell': 4, 
               'fujitsu': 5, 'google': 6,'hp': 7, 'huawei': 8,'lg': 9, 
               'lenovo': 10,'msi': 11,'mediacom': 12,'microsoft': 13,
               'razer': 14,'samsung': 15,'toshiba': 16, 'vero': 17,'xiaomi': 18}
ips_enc = {"yes":1, "no":0}
touchscreen_enc = {"yes":1, "no": 0}


def Get_Prediction(company, typename, ram, weight , touchscreen, ips, ppi, cpu_brand, hdd, ssd, gpu_brand, os):
    data = np.array([company_enc[company], 
                     typename_enc[typename],
                     ram,
                     weight, 
                     touchscreen_enc[touchscreen],
                     ips_enc[ips],
                     ppi, 
                     cpu_brand_enc[cpu_brand], 
                     hdd, 
                     ssd,
                     gpu_brand_enc[gpu_brand],
                     os_enc[os]])
    
    return pred_model.predict(data)

