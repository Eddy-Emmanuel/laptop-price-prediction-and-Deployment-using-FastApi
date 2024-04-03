import uvicorn
from enum import Enum
from model import Get_Prediction
from fastapi import FastAPI, Query
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()

class Company(str, Enum):
    acer = 'acer'
    apple= 'apple'
    asus = 'asus' 
    chuwi = 'chuwi'
    dell = 'dell' 
    fujitsu = 'fujitsu' 
    google = 'google'
    hp = 'hp'
    huawei = 'huawei'
    lg = 'lg'
    lenovo = 'lenovo'
    msi = 'msi'
    mediacom = 'mediacom'
    microsoft = 'microsoft'
    razer = 'razer'
    samsung = 'samsung'
    toshiba = 'toshiba'
    vero = 'vero'
    xiaomi = 'xiaomi'

class TypeName(str, Enum):
    convertible = '2 in 1 convertible'
    gaming ='gaming'
    netbook = 'netbook'
    notebook = 'notebook'
    ultrabook = 'ultrabook' 
    workstation = 'workstation'

class Ram(int, Enum):
    two = 2
    four = 4  
    six = 6
    eight = 8
    twelve = 12
    sixteen = 16
    twentyfour = 24
    thirtytwo = 32
    sixtyfour = 64

class CpuBrand(str, Enum):
    amd_processor = 'amd processor'
    intel_core_i3 = 'intel core i3',
    intel_core_i5 = 'intel core i5',
    intel_core_i7 = 'intel core i7',
    other_intel_processor = 'other intel processor'

class TouchScreen(str, Enum):
    yes = "yes"
    no = "no"

class IPS(str, Enum):
    yes = "yes"
    no = "no"

class HDD(int, Enum):
      zero = 0
      thirtytwo = 32  
      hundredand28 = 128
      fiveuhundred = 500
      onethousand = 1000
      twothousand = 2000

class SSD(int, Enum):
      zero = 0
      eight = 8 
      sixteen = 16
      thirtytwo = 32
      sixtyfour = 64
      hundredand28 = 128
      hundredand80 = 180
      two40 = 240
      two56 = 256
      five12 = 512
      seven68 = 768
      onethousand = 1000
      onethousand24 = 1024

class GpuBrand(str, Enum):
    amd = 'amd'
    intel = 'intel'
    nvidia = 'nvidia'

class OS(str, Enum):
    mac = 'mac'
    others = 'others'
    windows ='windows'


@app.get("/", include_in_schema=False)
async def HomePage(): # This function ensures that the app loads the swagger ui each time
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Laptop Price Prediction")

@app.post("/get_prediction/")
async def get_data(company : Company, 
                    typename: TypeName,
                    ram: Ram,
                    cpu_brand: CpuBrand,
                    touchscreen : TouchScreen, 
                    ips : IPS, 
                    hdd : HDD, 
                    ssd :  SSD,
                    gpu_brand : GpuBrand, 
                    os: OS,
                    weight: float = Query(..., ge=0.69, le=4.7, description="Weight of the laptop must be between 0.69 and 4.7"),                    
                    ppi : float = Query(..., ge=90.583402, le=352.465147, description="PPI of the laptop must be between 90.583402 and 352.465147")
                    ):
    
    # Get Company's input
    if company == Company.acer:
        company_input = Company.acer
    elif company == Company.apple:
        company_input = Company.apple
    elif company == Company.asus:
        company_input = Company.asus
    elif company == Company.chuwi:
        company_input = Company.chuwi
    elif company == Company.dell:
        company_input = Company.dell
    elif company == Company.fujitsu:
        company_input = Company.fujitsu
    elif company == Company.google:
        company_input = Company.google
    elif company == Company.hp:
        company_input = Company.hp
    elif company == Company.huawei:
        company_input = Company.huawei
    elif company == Company.lg:
        company_input = Company.lg
    elif company == Company.lenovo:
        company_input = Company.lenovo
    elif company == Company.msi:
        company_input = Company.msi
    elif company == Company.mediacom:
        company_input = Company.mediacom
    elif company == Company.microsoft:
        company_input = Company.microsoft
    elif company == Company.razer:
        company_input = Company.razer
    elif company == Company.samsung:
        company_input = Company.samsung
    elif company == Company.toshiba:
        company_input = Company.toshiba
    elif company == Company.vero:
        company_input = Company.vero
    else:
        company_input = Company.xiaomi
    
    # Get TypeName's input
    if typename == TypeName.convertible:
        typename_input = TypeName.convertible
    elif typename == TypeName.gaming:
        typename_input = TypeName.gaming
    elif typename == TypeName.netbook:
        typename_input = TypeName.netbook
    elif typename == TypeName.notebook:
        typename_input = TypeName.notebook
    elif typename == TypeName.ultrabook:
        typename_input = TypeName.ultrabook
    else:
        typename_input =  TypeName.workstation

    # Get Ram input
    if ram == Ram.two:
        ram_input = Ram.two
    elif ram == Ram.four:
        ram_input = Ram.four
    elif ram == Ram.six:
        ram_input = Ram.six
    elif ram == Ram.eight:
        ram_input = Ram.eight
    elif ram == Ram.twelve:
        ram_input = Ram.twelve
    elif ram == Ram.sixteen:
        ram_input = Ram.sixteen
    elif ram == Ram.twentyfour:
        ram_input = Ram.twentyfour
    elif ram == Ram.thirtytwo:
        ram_input = Ram.thirtytwo
    else:
        ram_input = Ram.sixtyfour
    
    # Get cpu brand input
    if cpu_brand == CpuBrand.amd_processor:
        cpu_brand_input = CpuBrand.amd_processor
    elif cpu_brand == CpuBrand.intel_core_i3:
        cpu_brand_input = CpuBrand.intel_core_i3
    elif cpu_brand == CpuBrand.intel_core_i5:
        cpu_brand_input = CpuBrand.intel_core_i5
    elif cpu_brand == CpuBrand.intel_core_i7:
        cpu_brand_input = CpuBrand.intel_core_i7
    else:
        cpu_brand_input = CpuBrand.other_intel_processor

    # Get touchscreen input
    if touchscreen == TouchScreen.yes:
        touchscreen_input = TouchScreen.yes
    else:
        touchscreen_input = TouchScreen.no

    # Get ips input
    if ips == IPS.yes:
        ips_input = IPS.yes
    else:
        ips_input = IPS.no


    # Get HDD input
    if hdd == HDD.zero:
        hdd_input = HDD.zero
    elif hdd == HDD.thirtytwo:
        hdd_input = HDD.thirtytwo
    elif hdd == HDD.hundredand28:
        hdd_input = HDD.hundredand28
    elif hdd == HDD.fiveuhundred:
        hdd_input = HDD.fiveuhundred
    elif hdd == HDD.onethousand:
        hdd_input = HDD.onethousand
    else:
        hdd_input = HDD.twothousand

    # Get SDD input
    if ssd == SSD.zero:
        ssd_input = SSD.zero
    elif ssd == SSD.eight:
        ssd_input = SSD.eight
    elif ssd == SSD.sixteen:
        ssd_input = SSD.sixteen
    elif ssd == SSD.thirtytwo:
        ssd_input = SSD.thirtytwo
    elif ssd == SSD.sixtyfour:
        ssd_input = SSD.sixtyfour
    elif ssd == SSD.hundredand28:
        ssd_input = SSD.hundredand28
    elif ssd == SSD.hundredand80:
        ssd_input = SSD.hundredand80
    elif ssd == SSD.two40:
        ssd_input = SSD.two40
    elif ssd == SSD.two56:
        ssd_input = SSD.two56
    elif ssd == SSD.five12:
        ssd_input = SSD.five12
    elif ssd == SSD.seven68:
        ssd_input = SSD.seven68
    elif ssd == SSD.onethousand:
        ssd_input = SSD.onethousand
    else:
        ssd_input = SSD.onethousand24
    
    # Get gpu_brand input
    if gpu_brand == GpuBrand.amd:
        gpu_brand_input = GpuBrand.amd
    elif gpu_brand == GpuBrand.intel:
        gpu_brand_input = GpuBrand.intel
    else:
        gpu_brand_input = GpuBrand.nvidia
    
    # Get OS input
    if os == OS.mac:
        os_input = OS.mac
    elif os == OS.others:
        os_input = OS.others
    else:
        os_input = OS.windows

    user_input = {"company":company_input,
                  "gpu_brand":gpu_brand_input,
                  "os":os_input, 
                  "ssd":ssd_input,
                  "hdd":hdd_input,
                  "ppi":ppi,
                  "ips":ips_input,
                  "touchscreen":touchscreen_input,
                  "cpu_brand":cpu_brand_input,
                  "ram":ram_input,
                  "typename":typename_input,
                  "weight":weight}
    
    model_pred = Get_Prediction(company=user_input["company"],
                                typename= user_input["typename"], 
                                ram = user_input["ram"],
                                weight = user_input["weight"], 
                                touchscreen = user_input["touchscreen"], 
                                ips = user_input["ips"],
                                ppi = user_input["ppi"], 
                                cpu_brand = user_input["cpu_brand"], 
                                hdd = user_input["hdd"], 
                                ssd = user_input["ssd"], 
                                gpu_brand = user_input["gpu_brand"],
                                os= user_input["os"])
    
    return {"Laptop Price": model_pred}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="127.0.0.1")

