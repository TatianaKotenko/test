from smartphone import Smartphone
catalog = [
    Smartphone("IPhone", "16 Pro", "+79493522137"),
    Smartphone("IPhone", "15 Pro", "+79493241534"),
    Smartphone("IPhone", "14", "+79499870567"),
    Smartphone("IPhone", "12 Pro", "+79493780980"),
    Smartphone("IPhone", "11 Pro", "+79494321709")
]
for smartphone in catalog:
    print(f"{smartphone.brand_of_the_phone} - {smartphone.phone_model}.\
           {smartphone.subscriber_number}")
