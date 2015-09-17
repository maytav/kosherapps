def add_color_css():
    color_css = """
    <style type="text/css">
    body {
    color: purple;
    background-color: #eeeeee }
    </style> """
    return color_css


def add_frame_css():
    frame_css = """
    <html lang="en-US">
    <style>
    .name {
    float: left;
    margin: 5px;
    padding: 10px;
    width: 120px;
    height: 250px;
    border: 2px solid black;
    }
    </style>
    """
    return frame_css


def add_information(data):
    body_page = ''
    for k, v in enumerate(data):
        body_page += """
        <div class="name">
        <a href="{}">
        <img src="{}"  style="width:120px;height:100px;border:0">
        </a>
        <div style="background-color:White; color:black; padding:10px;">
        <h3>{}</h3>
        <p>{}</p>
        </div></div>""".format(v[3], v[2], v[0], v[0])
    return body_page


def create_html(data):
    color = add_color_css()
    frame = add_frame_css()
    information = add_information(data)
    head_page = """
    {}\n{}\n<meta charset="utf-8" />
    <center>
    <title>first page</title>
    </head>
    <body>
    <img src="images.png" width="500" height="150">

    <u><h1 style="font-size:300%">Kosher apps</h1></u>
    <hr>
    <form action="">
    Search :
    <input type="text" name="Search">

    <hr>
    """.format(frame, color)

    all_the_page = "<!DOCTYPE html>\n{}\n{}\n</body>\n</center>\n</html>".format(head_page, information)
    return all_the_page


demo = ['Subway Surfers ', 'DASH as fast as you can! <br>DODGE the oncoming trains! ',
        'https://lh3.googleusercontent.com/-gEFw3tNPqLIiR4OUcVhmYtmvolJHxdauraygimLKikNhAtbrEAhRjqGP4wgoz9gZRU=w300',
        'https://play.google.com/store/apps/details?id=com.kiloo.subwaysurf'], \
       ['Waze Traffic ', 'Waze is the world&#39;s largest community-based traffic and navigation app.',
        'https://lh3.ggpht.com/7JPOKRuanUwnX42dJ9H-PscC-sRkK43GQGRoklxusB4FKBPJEOJY3c7ZhQbcsXol-v8=w300',
        'https://play.google.com/store/apps/details?id=com.waze'], \
       ['Facebook ', 'Keeping up with friends is faster than ever.',
        'https://lh3.googleusercontent.com/ZZPdzvlpK9r_Df9C3M7j1rNRi7hhHRvPhlklJ3lfi5jk86Jd1s0Y5wcQ1QgbVaAP5Q=w300',
        'https://play.google.com/store/apps/details?id=com.facebook.katana'], \
       ['eBay ',
        'At eBay we work hard every day to build a world-class online shopping experience for Android.',
        'https://lh3.ggpht.com/IaZ95xVwF-EL7-__IjE1e2M_KUZEh3ZvUwJPn_wYW7INKiKOfZbkJN2XJ1cDo49RcsaH=w300',
        'https://play.google.com/store/apps/details?id=com.ebay.mobile'], \
       ['Google Translate ',
        '* Type to translate 90 languages<br>* Use your camera to translate text instantly in 26 languages ',
        'https://lh5.ggpht.com/_oJcEUNMen3q-CL0zaH3bGMNHIUynnWUbAYOnl12QuwblFFVQhqfa5jEItCpz_5uvG4=w300',
        'https://play.google.com/store/apps/details?id=com.google.android.apps.translate'], \
       ['YouTube ',
        'Get the official YouTube app for Android phones and tablets.',
        'https://lh5.ggpht.com/jZ8XCjpCQWWZ5GLhbjRAufsw3JXePHUJVfEvMH3D055ghq0dyiSP3YxfSc_czPhtCLSO=w300',
        'https://play.google.com/store/apps/details?id=com.google.android.youtube'], \
       ['Tiny Flashlight',
        'Tiny Flashlight + LED is a simple, free flashlight app with LED light and several screen modes.',
        'https://lh3.ggpht.com/aFo5TwJieEcGiqFOAAEznv1V22YPPOLSyeGc2w4_YpUKztu_wBNB1ghw0wCcZQWMlIPJ=w300',
        'https://play.google.com/store/apps/details?id=com.devuni.flashlight'], \
       ['Twitter ',
        'Twitter is a free app that lets you connect with people ',
        'https://lh3.ggpht.com/lSLM0xhCA1RZOwaQcjhlwmsvaIQYaP3c5qbDKCgLALhydrgExnaSKZdGa8S3YtRuVA=w300',
        'https://play.google.com/store/apps/details?id=com.twitter.android'], \
       ['GO Keyboard',
        'Enjoy every tap and personalize your keyboard! Are you bored with plain android keyboard? We offer the personalized keyboard,',
        'https://lh3.ggpht.com/BfMJpHXJ4WKbYMFQCJLaGlEdiCOut0JLob4O5sEZul0v0QPXdSAekSw9VLBUAj6QBDla=w300',
        'https://play.google.com/store/apps/details?id=com.jb.emoji.gokeyboard'], \
       ['Temple Run 2 ',
        'With over a zillion downloads, Temple Run redefined mobile gaming.',
        'https://lh3.googleusercontent.com/7A-m5Eayursob4Gtj-FZ0fpK1ELh1maprfNifQ-l85aSS5Hxq7OG41l0n3qHP61exzBe=w300',
        'https://play.google.com/store/apps/details?id=com.imangi.templerun2'], \
       ['Angry Birds ', 'Use the unique powers of the Angry Birds to destroy the greedy',
        'https://lh6.ggpht.com/M9q_Zs_CRt2rbA41nTMhrPqiBxhUEUN8Z1f_mn9m89_TiHbIbUF8hjnc_zwevvLsRIJy=w300',
        'https://play.google.com/store/apps/details?id=com.rovio.angrybirds']


def open_file():
    file = create_html(demo)
    with open('kosher_apps.html', 'w') as apps:
        apps.write(file)


open_file()
