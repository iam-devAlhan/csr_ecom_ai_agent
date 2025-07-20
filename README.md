# csr_ecom_ai_agent
This is a hackathon project of vertical_ai_agent an AI agent that acts as a Customer Service Representative and can place order for your products on e-commerce store

Details to start development, First clone the repo and make sure python is installed
Create Python virtual environment using command
# For Windows: 
```bash
python -m venv myenv # For example
cd myenv/Scripts
activate.bat
```
# For Linux / Mac: 
```bash
python3 -m venv myenv # For example
source myenv/bin/activate
```
Then next you have to install dependencies required to run the FastAPI backend
```bash
pip3 install -r requirements.txt
# For Windows just keep pip instead of pip3
```

This will install all dependencies:

Run FastAPI Server:
```bash
uvicorn server:app --reload
```
This will start FastAPI Server and you can access the docs, maintain the API and the bot.py file and push changes to main branch

You also need to setup Twilio WhatsApp API via its Sandbox and can test the bot
Replace the Shopify Store name and its Admin API Key with yours and fetch all products from your Shopify Store
