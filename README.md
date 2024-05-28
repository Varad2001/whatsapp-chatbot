# Connecting LLMs to Whatsapp

In this project, I have tried to connect chatbots to whatsapp using TWILIO API. The chatbots have access to the user defined tools. <br>
THIS PROJECT IS CURRENTLY IN PROGRESS AND NOT COMPLETE. 

# DEMO
## Video
[[Watch the video]](https://drive.google.com/file/d/1E08VkCfCCUaUzEODFTfpndND2CcXzYqr/view?usp=drive_link)
## Images

<p float="left">
  <img src="assets/image_1.jpeg" width="200" />
  <img src="assets/image_2.jpeg" width="200" /> 
  <img src="assets/image_3.jpeg" width="200" />
</p>
<p float="left">
  <img src="assets/image_4.jpeg" width="200" />
  <img src="assets/image_5.jpeg" width="200" />
  <img src="assets/image_6.jpeg" width="200" />
</p>
<p float="left">
  <img src="assets/image_7.jpeg" width="200" />
  <img src="assets/image_8.jpeg" width="200" />
</p>



## Working
- Once the user connects whatsapp number to Twilio service using a code, s/he is set to send the messages.
- The messages are routed to the above mentioned API endpoint and then LLM API is called to get the response (currently GPT-4). 
- Then the response is sent back to the user as a whatsapp message. 
- A simple database, just a dictionary, is used to store the messages corresponding to the unique phone numbers.
## API DETAILS
A flask api endpoint "/messages" is created and deployed on the Render and the corresponding API url is connected to the Twilio api(Currently in sandbox environment). 

## LLM Details
- Currently OPENAI GPT is used.

## USER DEFINED TOOLS
- Weather tool
- Send email tool
    - Email is sent via my email.
- MUTLIPLY TWO NUMBERS TOOL

