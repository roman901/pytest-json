from aiohttp import web
import uvloop
import asyncio


async def hello_world(request):
    return web.json_response({'hello': 'world'})

app = web.Application()
app.router.add_get('/', hello_world)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
web.run_app(app)
