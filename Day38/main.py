import requests

GENDER = "male"
WEIGHT = 60
HEIGHT = 128
AGE    = 17

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

apiKey = "310931cb64993d9be7b1172845e88eb3"
app_id = "f9f214de"

exercise_text = input("Tell me what you do? ")


headers = {
	"x-app-id":app_id,
	"x-app-key":apiKey
}

parameters = {
	'query': exercise_text,
	'gender':GENDER,
	'weight_kg':WEIGHT,
	'height_cm':HEIGHT,
	"age" : AGE

}

response = requests.post(exercise_endpoint,json=parameters,headers=headers)
result = response.json()
print(result)