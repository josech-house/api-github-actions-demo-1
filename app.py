from apiflaskdemo import create_app

print "Hola"

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
