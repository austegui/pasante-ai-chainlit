import chainlit as cl, httpx, os

BASE      = os.getenv("GRADIENT_BASE", "https://qe7ahat47vdp32r2akh6gtrw.agents.do-ai.run")
ENDPOINT  = f"{BASE}/api/v1/chat/completions"
HEADERS   = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('GRADIENT_KEY')}"
}

@cl.on_message
async def main(msg_in: cl.Message):
    reply = cl.Message(""); await reply.send()
    payload = {"messages": [{"role": "user", "content": msg_in.content}]}

    async with httpx.AsyncClient() as client:
        try:
            r = await client.post(ENDPOINT, headers=HEADERS, json=payload, timeout=30)
            reply.content = (
                r.json()["choices"][0]["message"]["content"]
                if r.status_code == 200 else
                f"Error {r.status_code}: {r.text}"
            )
        except Exception as e:
            reply.content = f"Exception: {e}"
        await reply.update()

@cl.on_chat_start
async def hello():
    await cl.Message("Hola Ernesto, ¿cómo puedo ayudarte hoy? 🤖").send()
