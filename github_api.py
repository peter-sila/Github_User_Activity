import requests



def main():
   print("View User Activities On Github.\n")

   username = input("Enter username: ")
   response = requests.get(f'https://api.github.com/users/{username}/events')
   
   print(response)
   if response.status_code == 200:
      data = response.json()
      for event in data[:5]:
         print(f"\nType: {event['type']}")
         print(f"Repo: {event['repo']['name']}")
         print(f"Time: {event['created_at']}")

   else:
      print("Failed to fetch data.")

if __name__ == ("__main__"):
   main()