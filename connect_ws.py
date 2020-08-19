import asyncio
import websockets
import ssl
import json

G = '{"_event":"bulk-subscribe","tzID":8,"message":"pid-1057391:%%pid-1061443:%%pid-1057392:%%pid-1061453:%%pid-1061794:%%pid-169:%%pid-166:%%pid-172:%%pid-24441:%%pid-178:%%pid-171:%%pid-14958:%%pid-8830:%%pid-8849:%%pid-1:%%pid-13994:%%pid-23705:%%pid-2:%%pid-3:%%pid-4:%%pid-5:%%pid-7:%%pid-20:%%pid-27:%%pid-179:%%pid-8873:%%pid-8839:%%pid-44336:%%pid-8827:%%event-412518:%%event-412521:%%event-412472:%%event-411533:%%event-411537:%%event-411534:%%event-411535:%%isOpenExch-1:%%isOpenExch-2:%%isOpenPair-8873:%%isOpenPair-8839:%%isOpenPair-44336:%%isOpenPair-8827:%%domain-1:"}'
G1 = "{\"_event\":\"UID\",\"UID\":0}"

async def hello():
    async with websockets.connect('wss://stream80.forexpros.com/echo/814/a18gcy1l/websocket',ssl=ssl.SSLContext(protocol=ssl.PROTOCOL_TLS), ping_interval=None) as websocket:
        response = await websocket.recv()
        print("< {}".format(response))
        await websocket.send(json.dumps(G))
        await websocket.send(json.dumps(G1))
        while True:
           response = await websocket.recv()
           print(response)
        
asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()
