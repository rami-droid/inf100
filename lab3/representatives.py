import requests


def main():
    data = download_data()
    representatives = data["dagensrepresentanter_liste"]

    people_of_interest = []
    for person in representatives:
        if person["fylke"]["navn"] == "Hordaland":
            people_of_interest.append(person)

    people_of_interest.sort(key=get_first_name_lowercase)
    for person in people_of_interest:
        full_name = (
            f"{person['fornavn']} {person['etternavn']} ({person['parti']['id']})"
        )
        print(full_name)


def download_data():
    url = "https://data.stortinget.no/eksport/dagensrepresentanter?format=json"
    response = requests.get(url, headers={"User-Agent": "no.uib.ii.inf100"})
    data = response.json()
    return data


def get_first_name_lowercase(person):
    return person["fornavn"].lower()


if __name__ == "__main__":
    main()
