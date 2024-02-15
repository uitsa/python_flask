def make_body(title, body):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title> {title}Title of the document</title>
    </head>

    <body>
    The content of the document......
    </body>
    {body}

    </html>
    """

def form():
    return """
    <form action="/action_page.php">
    <label for="fname">First name:</label>
    <input type="text" id="fname" name="fname"><br><br>
    <input type="submit" value="Submit">
    </form>
    """