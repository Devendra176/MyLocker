import requests
import sys

from django.conf import settings

URL = settings.URL_TELEGRAM
TOKEN = ''
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def call_phone_register_api(phone):
    url = URL + 'phone/register/'
    json_data = {'phone': phone,}
    post = requests.post(url, data=json_data, headers=headers)
    return post.json()

def call_phone_verification_api(otp, phone):
    url = URL +'phone/verification/'
    json_data = {'phone': phone, 'otp': otp}
    post = requests.post(url, data=json_data, headers=headers)
    return post.json()

def get_website_data(context):
    if context.get('token'):
        url = URL + 'website/data/'
        headers['Authorization'] = 'token %s'%context.get('token')
        get_data = requests.get(url, headers=headers)
        return get_data.json()