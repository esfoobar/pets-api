def pet_obj(pet):
    return {
      "id":             pet.external_id,
      "name":           pet.name,
      "species":        pet.species.name,
      "breed":          pet.breed.name,
      "age":            pet.age,
      "store":          pet.store.external_id,
      "price":          str(pet.price),
      "received_date":  pet.received_date,
      "links": [
        { "rel": "self", "href": "/pets/" + pet.external_id }
      ]
    }

def pets_obj(pets):
    pets_obj = []
    for pet in pets.items:
        pets_obj.append(pet_obj(pet))
    return pets_obj
