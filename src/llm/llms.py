import os
import json
from openai import OpenAI
from src.config import BASE_URL, TUNESTUDIO_KEY , MAX_ITERATIONS, MODEL_NAME, SYSTEM




class LLM:
    def __init__(self, tools=None) -> None:
        client = OpenAI(
            base_url=BASE_URL,
            api_key=TUNESTUDIO_KEY,
            
            )
        self.client = client
        #self.init_history()
        self.tools = tools
        
    def init_history(self):
        self.messages = [ {
            "role": "system",
            "content": SYSTEM,
            }]
        
    def get_response(self,messages, tools=None):
        if tools : 
            response =  self.client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=messages,
                    tools=self.tools.tools_meta_data,
                    tool_choice="auto")
        else:
            response =  self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,)
        return response



    def run_instance(self, query):
        messages = self.messages.copy()
        messages.append({
            "role": "user",
            "content": query,
            })
        response =  self.get_response(messages, self.tools)
        return response.choices[0].message.content
    

    
    def chat(self, query, history):
        if not ( history or len(history)==0):
            self.init_history()
        else:
            self.messages = history
        self.messages.append({
            "role": "user",
            "content": query,
            })
        
        for _ in range(MAX_ITERATIONS):
            response = self.get_response(tools=self.tools.tools_meta_data, messages=self.messages)

            #print(f"{response.choices[0].message.content}")

            if response.choices[0].finish_reason == "stop":
                print(f"\nFinal answer:{response.choices[0].message.content}")
                self.messages.append({
                            "role": "system",
                            "content": response.choices[0].message.content,
                            })
                return response.choices[0].message.content
            
            if response.choices[0].finish_reason == 'tool_calls':
                tool_calls = response.choices[0].message.tool_calls
                self.messages.append(response.choices[0].message)

                for tool_call in tool_calls[:1]:
                    function_name = tool_call.function.name

                    print(f"\nTool call : {function_name}\n{response.choices[0].message}")

                    function_to_call = self.tools.tool_to_call[function_name]
                    function_args = json.loads(tool_call.function.arguments)
                    function_response = function_to_call(
                        function_args
                    )

                    print(f"\nFucntion response :{function_response}")

                    """self.messages.append(
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": function_response,
                        }
                    )"""
                    self.messages.append(
                        {
                            "role": "user",
                            "content": f"Function response : {function_response}",
                        })
            else:
                print(f"{response.choices[0].finish_reason}")
                return response

        
if __name__ == "__main__":
    print(LLM().run_instance(query="hi"))

                

