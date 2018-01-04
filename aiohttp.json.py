from aiohttp import web


async def hello_world(request):
    return web.json_response({'hello': 'world'})

app = web.Application()
app.router.add_get('/', hello_world)

web.run_app(app)
