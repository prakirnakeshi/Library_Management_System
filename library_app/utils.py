# import requests

# from library_app.models import Book


# def get_books(num_books):
#     print("See")
#     url = "https://frappe.io/api/method/frappe-library"
#     response = requests.get(url)
#     data= response.json()["message"] 
#     for title in data[:num_books]:
#         print("API Response:", title)  
#         # if not Book.objects.filter(title=title["title"],authors=title["authors"],isbn=title["isbn"],publisher=title["publisher"]):
#         Book.objects.create(title=title["title"],authors=title["authors"],isbn=title["isbn"],publisher=title["publisher"],)
#             # print("Saved")
#         # else:
#             # print("Data Exists")