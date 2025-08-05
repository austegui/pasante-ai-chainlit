import chainlit as cl, httpx, os

ENDPOINT = os.getenv("GRADIENT_ENDPOINT")
HEADERS  = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('GRADIENT_KEY')}"
}

@cl.on_message
async def main(msg_in: cl.Message):
    reply = cl.Message(content=""); await reply.send()
    payload = {"messages": [{"role": "user", "content": msg_in.content}]}

    async with httpx.AsyncClient() as client:
        try:
            r = await client.post(ENDPOINT, headers=HEADERS, json=payload, timeout=30)
            reply.content = (
                r.json()["choices"][0]["message"]["content"]
                if r.status_code == 200
                else f"Error {r.status_code}: {r.text}"
            )
        except Exception as e:
            reply.content = f"Exception: {e}"
        await reply.update()

@cl.on_chat_start
async def start():
    await cl.Message("Hola Ernesto, ¿cómo puedo ayudarte hoy? 🤖").send()
