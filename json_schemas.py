AUTH = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "user": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                }
            },
            "additionalProperties": False,
            "required": [
                "email",
                "name"
            ]
        },
        "accessToken": {
            "type": "string"
        },
        "refreshToken": {
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": [
        "success",
        "user",
        "accessToken",
        "refreshToken"
    ]
}
MAKE_ORDERS = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "name": {
            "type": "string"
        },
        "order": {
            "type": "object",
            "properties": {
                "ingredients": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "_id": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            },
                            "type": {
                                "type": "string"
                            },
                            "proteins": {
                                "type": "integer"
                            },
                            "fat": {
                                "type": "integer"
                            },
                            "carbohydrates": {
                                "type": "integer"
                            },
                            "calories": {
                                "type": "integer"
                            },
                            "price": {
                                "type": "integer"
                            },
                            "image": {
                                "type": "string"
                            },
                            "image_mobile": {
                                "type": "string"
                            },
                            "image_large": {
                                "type": "string"
                            },
                            "__v": {
                                "type": "integer"
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "_id",
                            "name",
                            "type",
                            "proteins",
                            "fat",
                            "carbohydrates",
                            "calories",
                            "price",
                            "image",
                            "image_mobile",
                            "image_large",
                            "__v"
                        ]
                    }
                },
                "_id": {
                    "type": "string"
                },
                "owner": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string"
                        },
                        "createdAt": {
                            "type": "string"
                        },
                        "updatedAt": {
                            "type": "string"
                        }
                    },
                    "additionalProperties": False,
                    "required": [
                        "name",
                        "email",
                        "createdAt",
                        "updatedAt"
                    ]
                },
                "status": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "createdAt": {
                    "type": "string"
                },
                "updatedAt": {
                    "type": "string"
                },
                "number": {
                    "type": "integer"
                },
                "price": {
                    "type": "integer"
                }
            },
            "additionalProperties": False,
            "required": [
                "ingredients",
                "_id",
                "owner",
                "status",
                "name",
                "createdAt",
                "updatedAt",
                "number",
                "price"
            ]
        }
    },
    "additionalProperties": False,
    "required": [
        "success",
        "name",
        "order"
    ]
}
GET_ORDERS = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "orders": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "_id": {
                        "type": "string"
                    },
                    "ingredients": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "status": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "createdAt": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string"
                    },
                    "number": {
                        "type": "integer"
                    }
                },
                "additionalProperties": False,
                "required": [
                    "_id",
                    "ingredients",
                    "status",
                    "name",
                    "createdAt",
                    "updatedAt",
                    "number"
                ]
            }
        },
        "total": {
            "type": "integer"
        },
        "totalToday": {
            "type": "integer"
        }
    },
    "additionalProperties": False,
    "required": [
        "success",
        "orders",
        "total",
        "totalToday"
    ]
}
