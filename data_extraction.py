from sqlalchemy.orm import sessionmaker, scoped_session
import model
import csv

def open_csv(session):
    # opens the wine csv
    with open('winelist.csv', 'ru') as csvfile:
        itemdata = [row for row in csv.reader(csvfile.read().splitlines(), delimiter = ",", dialect=csv.excel_tab)]
        img_path_list=["01_Riesling.png", "02_Pinot_Grigio.png", "04_Sauvignon_Blanc.png", "05_Chardonnay.png", "06_Pinot-Noir.png", "07_Merlot.png", "08_Cabernet_Sauvignon.png", "09_Syrah.png", "10_Zinfindel.png"]

        for i, row in enumerate(itemdata):
            wine_object = model.WineObject(
                wine_type=row[0].decode("latin-1"), 
                varietal=row[1].decode("latin-1"), 
                flavor_profile=row[2].decode("latin-1"), 
                region=row[3].decode("latin-1"), 
                description=row[4].decode("latin-1"), 
                cheese_pairing=row[5].decode("latin-1"), 
                food_pairing=row[6].decode("latin-1"), 
                fruit_pairing=row[7].decode("latin-1"), 
                flavor_pairing=row[8].decode("latin-1"), 
                img_path=img_path_list[i])

            session.add(wine_object)
        session.commit()

def main(session):
    csv = open_csv(session)

if __name__ == "__main__":
    session = model.connect()
    main(session)

