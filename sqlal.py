from flask.ext.sqlalchemy import _SQLAlchemyState
from sqlalchemy import *
# from list_store.appList import *
from Kosher_apps import url_apps_url_downland,all_url
from sqlalchemy.exc import OperationalError

db = create_engine('sqlite:///kosher_app.sqlite3')

db.echo = False  # Try changing this to True and see what happens

metadata = MetaData(db)

kosherApps = Table('kosher app', metadata,
    Column('app_id',Integer, primary_key=True),
    Column('name', String(100)),
    Column('Description',String(100)),
    Column('PEGI',String(10)),
    Column('Img1',String),
    Column('Img2',String),
    Column('Img3',String),
    Column('Img4',String),
    Column('url_video',String),
    Column('Link_downland',String),
    Column('id_google_play',String)

)
def main():
    try:
        kosherApps.create()
    except OperationalError:
        pass
    url_list=all_url(url_apps_url_downland)
    # print(url_list[0])

    i = kosherApps.insert()

    for row in url_list:
            # print(len(row))
            i.execute({'name': row[0], 'Description': row[1],'PEGI':row[2],
                       'Img1':row[3],'Img2':row[4],'Img3':row[5],
                   'Img4':row[6],'url_video':row[7]})
# print(app_list)

    # print(url_apps_url_downland)
if __name__ == '__main__':
    main()