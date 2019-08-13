import os.path
import saxo

@saxo.setup
def setup(irc):
    path = os.path.join(irc.base, "database.sqlite3")
    with saxo.database(path) as db:
        if "saxo_quote" not in db:
            db["saxo_quote"].create(
                ("unixtime", int),
                ("channel", str),
                ("message", str))

            
