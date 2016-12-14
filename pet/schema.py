schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "species": {"type": "string"},
        "breed": {"type": "string"},
        "age": {"type": "number"},
        "store": {"type": "string"},
        "price": {"type": "string"},
        "received_date": {"type": "string"},
    },
    "required": ["name", "species", "breed", "age", "store", "price", "received_date"]
}
