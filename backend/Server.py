from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    
    if intent == "check.bmi - context:ongoing-check.bmi":
                height = int(parameters['unit-length']['amount'])
                weight = int(parameters['unit-weight']['amount'])

                # Convert height from centimeters to meters (since BMI formula requires height in meters)
                height_meters = height / 100
            
                # Compute BMI using the formula: weight / (height^2)
                bmi = weight / (height_meters ** 2)
                
            
                if bmi < 18.5:
                        message = "Under Weight"
                elif 18.5 <= bmi < 24.9:
                        message = "Normal Weight"
                elif 25 <= bmi < 29.9:
                        message = "Over Weight"
                else:
                        message = "Obesity"

                return JSONResponse(content={
                    "fulfillmentText": f"Your BMI is {round(bmi,2)} kg/m^2 and you are : {message}"
                })


 
           


           




            


        





 

    

        

       
    



 



    