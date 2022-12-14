from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Hao")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)
    
## If you want to run in development over TCP/IP
def init_func(argv):
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])
    return app