import requests 
from datetime import datetime
GRAPH_ID="graph1"
USERNAME="george180594"
TOKEN="dsa45d4s5d452234sd"
pixela_endpoint ="https://pixe.la/v1/users"

user_params={
    "token":TOKEN ,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}
# response= requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
# pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# graph_config= {
#     "id":GRAPH_ID,
#     "name":"Cycling Graph",
#     "unit":"Km",
#     "type":"float",
#     "color":"ajisai"
# }
# today= datetime.now()
# today= datetime(year=2024,month=11,day=13)

pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20241113"

pixel_config= {
    "quantity":"10",
}


headers={
    "X-USER-TOKEN":TOKEN
}
response=requests.put(url=pixel_endpoint,json=pixel_config,headers =headers) #delete vs put
print(response.text)




# pixel_config= {
#     "date":today.strftime("%Y%m%d"),
#     "quantity":"9.2",

# }


# headers={
#     "X-USER-TOKEN":TOKEN
# }
# response=requests.post(url=pixel_endpoint,json=pixel_config,headers =headers)
# print(response.text)


