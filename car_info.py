def car_details(make, model, year):
    details = {
        "make": make,
        "model": model,
        "year": year
    }
    return f"The car is a {details['year']} {details['make']} {details['model']}."

if __name__ == "__main__":
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = input("Enter car year: ")
    
    print(car_details(make, model, year))
