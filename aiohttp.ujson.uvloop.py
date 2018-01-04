from aiohttp import web
import ujson
import uvloop
import asyncio


async def hello_world(request):
    return web.Response(
        body=ujson.dumps({'hello': 'world'}).encode('utf-8'),
        content_type='application/json')

app = web.Application()
app.router.add_get('/', hello_world)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

web.run_app(app)
