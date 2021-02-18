






response = requests.get('https://api.exchangeratesapi.io/latest')
response_json  = response.json()
rates = response_json[‘rates’]














if __name__ == "__main__":

