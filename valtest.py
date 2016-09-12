from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "price": {"type": "number"},
        "name": {"type": "string"},
    },
    "required": ["price", "name"]
}
validate({"name": "Eggs"}, schema)
