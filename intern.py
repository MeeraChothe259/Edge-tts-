import asyncio
import edge_tts

async def main() :
    tts = edge_tts.Communicate("Hello I am Meera","en-IN-NeerjaNeural")
    await tts.save("test.mp3")
asyncio.run(main())