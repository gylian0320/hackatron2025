from website import create_app

app = create_app()

if __name__ == "__main__":
    # from website.auth import User
    # with app.app_context():
    #     print(User.query.all())
    app.run(debug=True)
