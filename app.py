import chainlit as cl
import httpx
import json
import os

# Get endpoint from environment variable
GRADIENT_ENDPOINT = os.getenv("GRADIENT_ENDPOINT", "https://qe7ahat47vdp32r2akh6gtrw.agents.do-ai.run/api/v1/chat/completions")

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()
    
    messages = [{"role": "user", "content": message.content}]
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                GRADIENT_ENDPOINT,
                json={"messages": messages},
                timeout=30.0
            )
            
            if response.status_code == 200:
                data = response.json()
                assistant_message = data['choices'][0]['message']['content']
                msg.content = assistant_message
                await msg.update()
            else:
                msg.content = f"Error: {response.status_code}"
                await msg.update()
                
        except Exception as e:
            msg.content = f"Error: {str(e)}"
            await msg.update()

@cl.on_chat_start
async def start():
    await cl.Message(
        content="Hola Ernesto, como puedo ayudarte hoy? 🤖"
    ).send()
