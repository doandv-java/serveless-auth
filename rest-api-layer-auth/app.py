from chalice import Chalice

app = Chalice(app_name='rest-api-layer-auth')


@app.route('/')
def index():
    return {'hello': 'world'}

