from website import create_app

app = create_app()

if __name__ == '__main__':
    """
        Start the webserver
        debug=True means that everytime there are changes in the code, it automatically rerun the webserver
    """
    app.run(debug=True)
