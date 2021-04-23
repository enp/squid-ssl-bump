#!/usr/bin/env python3

import asyncio, socket

async def handle_request(reader, writer):
    response = ''
    request = (await reader.read(1000000)).decode('utf8')
    print(request, flush=True)
    if (request.startswith('OPTIONS')):
        response += 'ICAP/1.0 200 OK\r\n'    
    elif (request.startswith('REQMOD')):
        response += 'ICAP/1.0 204 No content\r\n'
    else:
        response += 'ICAP/1.0 400 Bad request\r\n'
    response += '\r\n'
    writer.write(response.encode('utf8'))
    await writer.drain()
    writer.close()

async def run_server():
    print('Starting ICAP filtering daemon', flush=True)
    server = await asyncio.start_server(handle_request, '0.0.0.0', 1344)
    async with server:
        await server.serve_forever()

asyncio.run(run_server())
