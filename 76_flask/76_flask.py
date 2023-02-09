# Day 76 on Replit: "Flask!"

# Fix my code section

# from flask import Flask
# import datetime  # import the datetime library

# app = Flask(__name__, static_url_path="/static")


# @app.route('/')
# def index():
#     page = f"""<html><body>
#   <p><a href = "/home">Go home</a></p>
#   </body>
#   </html>"""
#     return page


# @app.route('/home')
# def home():
#     page = """

#   <html>

#   <head>
#     <title>David's World Of Baldies</title>
#   </head>


#   <body>
#   <h1>Dave's World of Baldies</h1>
#   <h2>Welcome to our website!</h2>

#   <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

#   <h2>Gallery of Baldies</h2>
#   <p>Here are some of the legends of the bald world.</p>

#   <img src="static/images/picard.jpg" width = 30%>
#   <p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>

#   <ul>
#     <li>Beautiful bald man</li>
#     <li>Calm and cool under pressure</li>
#     <li>All the Picard memes</li>
#   </ul>

#   <p><a href = "page2.html">Go to page 2</a></p>

# </body>

# </html>

#   """

#     return page


# app.run(host="0.0.0.0", port=81)


# Challenge section

from flask import Flask

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def home():
    page = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="static/styles/linkedTree.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <div class = "container">  
    <img src="static/images/FlGAgqaWYAAUm6F.png" alt="mrc profile photo">
    <div calss = "container-text">
      <h1>MRC</h1>
    <p class = "subtitle">Python student</p>
    <h3>Socials</h3>
    <a href="https://twitter.com/mrcdevv"><p>Twitter (@mrcdevv)</p></a>
    <a href="https://www.youtube.com/@mrcdev"><p>Youtube (@mrcdev)</p></a>
    <a href="https://www.tiktok.com/@mrcdevv"><p>TikTok (@mrcdevv)</p></a>
    <a href="/portfolio"><p>Portfolio</p></a>
    </div>
  </div>
</body>

</html>"""
    return page


@app.route('/portfolio')
def portfolio():
    page = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>MRC's Portfolio</title>
  <link href="static/styles/portfolio.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <h1>MRC's Protfolio</h1>

  <h2>Day 28 Solution</h2>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris in libero a eros lobortis scelerisque. Nullam vel
    mi nec odio tincidunt venenatis id molestie dolor. Mauris fermentum eu turpis id egestas. Suspendisse at nulla a
    risus rhoncus molestie. Curabitur volutpat erat libero, et fringilla leo finibus sit amet. Sed hendrerit eros sit
    amet elit elementum ornare. Integer mi risus, vestibulum at mi in, consequat sagittis metus.</p>
  <a href="https://replit.com/@marcodeArg/day-28-Battle-Game-simulator#main.py"><img src="static/images/battle.png"
      alt="battle image"></a>
</body>

</html>"""

    return page


app.run(host='0.0.0.0', port=81)
