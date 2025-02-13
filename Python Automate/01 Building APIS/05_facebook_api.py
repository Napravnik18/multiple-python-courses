import requests

#campo me redireciona a meu perfil, pode ser substituido por outro
url = "https://graph.facebook.com/v21.0/me?fields=id%2Cname%2Cemail%2Cposts&access_token=myaccesstoken"

response = requests.get(url)
print(response.text)