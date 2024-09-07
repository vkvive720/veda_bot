from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class FulfillmentRequest(BaseModel):
    session: str
    queryResult: dict
    originalDetectIntentRequest: dict




# fil=

# # class FulfillmentRequest(BaseModel):
# #     session: str
# #     queryResult: dict
# #     originalDetectIntentRequest: dict

@app.post("/")
async def webhook(request: Request):
    data = await request.json()
    fulfillment_request = FulfillmentRequest(**data)
    
    indent= fulfillment_request.queryResult["intent"]["displayName"]
    
    if indent == "final":
          
      oc_context= fulfillment_request.queryResult["outputContexts"]
      
      s={"a":1,}
      # [2]['parameters']
      
      context={"a":1,}
      
        
      
      def key_in_dict(key, dictionary:dict):
          # Check if the key is in the dictionary
          return key in dictionary
        
      for k in oc_context:
            print(k['parameters'])
            para:dict=k['parameters']
            
            if key_in_dict('op1', para):
                  context=para
                  break
                  
                  
            
    
      # # result_of_query=data["queryResult"]
      # # =data
      
      # options=[context["op1"], context["options2"], context["option3"], context["option4"],context["option5"]]
      
      # options=[context["op1"],context["op2"],context["op3"],context["op4"],context["op5"],context["op6"],context["op7"],context["op8"],context["op9"],context["op10"]]
      
      
      options=[context['op1'],context['op2'],context['op3'],context['op4'],context['op5'],context['op6'],
              context['op7'],context['op8'],context['op9'],context['op10'],context['op11'],context['op12'],
              context['op13'],context['op14'],context['op15'],context['op16'],context['op17'],context['op18'],
              context['op19'],context['op20'],context['op21'],context['op22'],context['op23'],context['op24'],
              context['op25'],context['op26'],context['op27']]
      print(context)
      
      print(options)
      a=0
      b=0
      c=0
      
      for i in range(27):
          
          if(options[i]=="A"):
              a+=1
          if(options[i]=="B"):
              b+=1
          if(options[i]=="C"):
              c+=1
              
      ap=a*100/(a+b+c)
      bp=b*100/(a+b+c)
      cp=c*100/(a+b+c)
      
      ap=round(ap,1)
      bp=round(bp,1)
      cp=round(cp,1)
      
      event="name"
      
      if(ap>55):
            event="returnvata"
      elif(bp>55):
            event="returnpita"
      elif(cp>55):
            event="returnkapha"
            
      elif(abs(ap - bp)<=5 and abs(bp - cp)<=5 and abs(ap - cp)<=5):
            event="balanceall"
      elif(a<b and a<c):
            event="pitakapha"
      elif(b<c and b<a):
            event="kaphavata"
      else:
            event="pitavata"
            
      
      
      
              
              
      text_response=f"you have vata {ap} % \npitta {bp} %  \n and kapha {cp} % "
      # text_response=str(fulfillment_request)
      
      # text_response=str(context)
      
      
      # text_response="server conneccted to vivek sucessfully"
      
          
      
    
      
      text_res="connected to server"
      
      return JSONResponse(content={
  "followupEventInput": {
    "name": event,
    "languageCode": "en-US",
    "parameters": {
      "vta": ap,
      "pta": bp,
      "kpa": cp,
    }
  }
}
  )
        
    
