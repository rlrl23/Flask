from .blog.app import db, app
from .blog.models import User

@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")

@app.cli.command("create-users")
def create_users():
    james = User(username="lora")
    nina = User(username="lana", email='lana@mail.ru')
    db.session.add(nina)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", nina, james)

@app.cli.command("create-admin")
def create_admin():
    admin = User(username="admin2", is_staff=True, email='admin2@mail.ru')
    db.session.add(admin)
    db.session.commit()
    print("done! created users:", admin)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True
    )