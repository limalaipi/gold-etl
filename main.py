import requests

def main():
    print("Hello from gold-etl!")
    api = "https://www.thaigoldtoday.com/api/gold-price"
    response = requests.get(api)
    if response.status_code == 200:
        data = response.json()
        print("Data fetched successfully:", data)
    else:
        print("Failed to fetch data")



if __name__ == "__main__":
    main()
