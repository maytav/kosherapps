
import requests

url_apps_url_downland = [

    'https://play.google.com/store/apps/details?id=org.wikipedia',

    "https://play.google.com/store/apps/details?id=com.kiloo.subwaysurf",

    "https://play.google.com/store/apps/details?id=com.waze",

    'https://play.google.com/store/apps/details?id=com.wolfram.android.alpha',

    'https://play.google.com/store/apps/details?id=com.wolfram.android.statistics',

    'https://play.google.com/store/apps/details?id=com.flyersoft.moonreaderp',

    "https://play.google.com/store/apps/details?id=com.facebook.katana",

    "https://play.google.com/store/apps/details?id=com.ebay.mobile",

    'https://play.google.com/store/apps/details?id=com.morriscooke.explaineverything',

    'https://play.google.com/store/apps/details?id=com.splashtop.remote.WHITEBOARD',

    "https://play.google.com/store/apps/details?id=com.google.android.apps.translate",

    "https://play.google.com/store/apps/details?id=com.google.android.youtube",

    "https://play.google.com/store/apps/details?id=com.devuni.flashlight",

    "https://play.google.com/store/apps/details?id=com.twitter.android",

    "https://play.google.com/store/apps/details?id=com.jb.emoji.gokeyboard",

    "https://play.google.com/store/apps/details?id=com.imangi.templerun2",

    "https://play.google.com/store/apps/details?id=com.rovio.angrybirds",

    "https://play.google.com/store/apps/details?id=com.instagram.android",

    "https://play.google.com/store/apps/details?id=com.skype.raider",

    "https://play.google.com/store/apps/details?id=com.khl.kiosk",

    "https://play.google.com/store/apps/details?id=tfilon.tfilon",

    "https://play.google.com/store/apps/details?id=hatanah.application",

    "https://play.google.com/store/apps/details?id=com.google.android.apps.docs",

    "https://play.google.com/store/apps/details?id=com.mobilityware.solitaire",

    'https://play.google.com/store/apps/details?id=com.wewanttoknow.DragonBoxPlus',

    'https://play.google.com/store/apps/details?id=com.wewanttoknow.DragonBox2',

    'https://play.google.com/store/apps/details?id=com.volsoft.policesncradi',

    'https://play.google.com/store/apps/details?id=kr.sira.measure',

    'https://play.google.com/store/apps/details?id=com.bit2be.coinzTfilinLachyal',

    'https://play.google.com/store/apps/details?id=heb.apps.itehilim'
]


def all_param_from_app(name, discraption, pegi, image1, image2, image3, image4, url_video):
    apps_list = []
    apps_list.append(name)
    apps_list.append(discraption)
    apps_list.append(pegi)
    apps_list.append(image1)
    apps_list.append(image2)
    apps_list.append(image3)
    apps_list.append(image4)
    apps_list.append(url_video)
    # apps_list.append(pay)
    # apps_list.append(url_app_downland)
    # print(apps_list)
    return apps_list


def pharser_app(url_app):
    page = requests.get(url_app)
    a = page.text


    # free_or_pay = a.find(' Free Game')
    # free_or_pay2 = a.find('free ')
    # free_or_pay4 = a.find(' Buy</span>')
    #
    # if free_or_pay > -1 or free_or_pay2 > -1 and free_or_pay4 < 0:
    #     pay = 'free'
    # else:
    #     pay = a[free_or_pay4-7:free_or_pay4].replace('</div','free').replace('>','')\
    #         .replace('n>','').replace('n','').strip()

    # print(pay)

    # f_main_category = a.find(' Apps. <div class')
    # print(f_main_category)
    # print(a[main_category:f_main_category])
    # # app_name = app__name.strip()

    main_name = a.find('title">')
    f_main_name = a.find('- Android')
    app__name = a[main_name + 7:f_main_name]
    app_name = app__name.replace('&amp;', 'and').strip()
    # print(app__name)


    discraption2 = a.find('desc">')
    dis = a.find('<p>')
    dis1 = a.find('<br> <br>')
    dis3 = a.find('.</div>  <div ')
    if dis > 0:
        discraption_ = a[discraption2 + 6:dis].replace('<br>', ' ').replace('<b>', ' ').replace('*', ' ') \
            .replace('#', ' '.strip()).replace('">', '').replace('&','\'').replace('39;','').\
            replace('quot;','\''.strip()).strip()
        discraption = discraption_
        print(discraption)
    else:
        if dis1 > 0:
            disr = a[discraption2 + 6:dis1].replace('<br>', ' ').replace('<b>', ' ').replace('*', ' ') \
            .replace('#', ' '.strip()).replace('">', '').replace('&','\'').replace('39;','').\
            replace('quot;','\''.strip()).strip()
            discraption = disr.strip()
            print(discraption)
        else:
            if dis3 > 0:
                distr = a[discraption2 + 6:dis3 + 1].replace('<br>', ' ').replace('<b>', ' ').replace('*', ' ') \
            .replace('#', ' '.strip()).replace('">', '').replace('&','\'').replace('39;','').\
            replace('quot;','\''.strip()).strip()
                discraption = distr.strip()
                print(discraption)
            else:
                disc = a[discraption2:discraption2 + 150].replace('<br>', ' ').replace('<b>', ' ').replace('*', ' ') \
            .replace('#', ' '.strip()).replace('">', '').replace('&','\'').replace('39;','').\
            replace('quot;','\''.strip()).strip()
                discraption = disc.strip()
                print(discraption)

        # discraption = a[discraption2:discraption2 + 250].replace('<br>', ' ').replace('<b>', ' ') \
        #     .replace('*', ' ').replace('#', ' ').replace('">', '').strip()
        # print(discraption)

    rating = a.find('> <img alt=')
    rat = a.find(' class="document-subtitle c')
    pegi_3 = a[rating + 12:rat - 1]
    pegi3 = pegi_3.strip()

    main_image1 = a.find('image" src="')
    m_imag1 = a.find(' screenshot thumbnail   " title="  ')
    _main_image1 = a[main_image1 + 12:m_imag1]
    image_1 = _main_image1.split('alt=')[0]
    image1 = image_1[:-2]
    # print(image1[:-2])

    more_image2 = a.find('full-screenshot-0" src="')
    m_image2 = a.find('"full-screenshot-1" ')
    g = a[more_image2 + 24:m_image2 - 140]
    image__2 = g.split('alt=')[0]
    image2 = image__2[:-2]

    more_image3 = a.find('full-screenshot-1" src="')
    if more_image3 > -1:
        m_image3 = a.find('"full-screenshot-2" ')
        image_3 = a[more_image3 + 24:m_image3 - 140]
        image__3 = image_3.split('alt=')[0]
        image3 = image__3[:-2]
    else:
        image3 = None

    more_image4 = a.find('full-screenshot-2" src="')
    if more_image4 > -1:
        m_image4 = a.find('"full-screenshot-3" ')
        image_4 = a[more_image4 + 24:m_image4 - 140]
        image__4 = image_4.split('alt=')[0]
        image4 = image__4[:-2]
    else:
        image4 = None

    video_url = a.find('-url="')
    if video_url > -1:
        v_url = a.find('> <span class="play-action-containe')
        url_main_video = a[video_url + 6:v_url]
        url_video = url_main_video[:-1]
    else:
        url_video = None

    return all_param_from_app(app_name, discraption, pegi3, image1, image2, image3, image4, url_video)



def all_url(url_apps):
    for url in url_apps:
        pharser_app(url)



if __name__ == '__main__':

    all_url(url_apps_url_downland)


    # print(pharser_app("https://play.google.com/store/apps/details?id=com.kiloo.subwaysurf"))




    # set_apps("https://play.google.com/store/apps/details?id=com.kiloo.subwaysurf")
    # # down = link.find('?id="')
    # # finish_link = link.find('tabindex="1" autocapitalize')
    # # link[down:finish_link]
    #
    # print(link)
    # # print(link[down:finish_link])
    # # s = '{}{}{}'.format(link[down+6],aa [1],link[finish_link])
    # # print(s)
    #
    # # lint[down:finish_link]=aa[1]
    # # print(aa[1])
