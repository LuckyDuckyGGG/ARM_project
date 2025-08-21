authorization = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "timestamp": {
      "type": "string"
    },
    "success": {
      "type": "string"
    },
    "token": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "middleName": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "timezoneOffset": {
          "type": "integer"
        },
        "active": {
          "type": "boolean"
        },
        "approvedByOrganization": {
          "type": "boolean"
        },
        "roles": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                }
              },
              "required": [
                "name"
              ]
            }
          ]
        },
        "email": {
          "type": "string"
        },
        "organizationName": {
          "type": "string"
        },
        "organizationId": {
          "type": "integer"
        },
        "employment": {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name"
          ]
        },
        "headRole": {
          "type": "string"
        },
        "lastActivity": {
          "type": "string"
        },
        "projectsInfos": {
          "type": "array",
          "items": {}
        },
        "enable": {
          "type": "boolean"
        },
        "links": {
          "type": "array",
          "items": {}
        },
        "last_name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name",
        "middleName",
        "timezone",
        "timezoneOffset",
        "active",
        "approvedByOrganization",
        "roles",
        "email",
        "organizationName",
        "organizationId",
        "employment",
        "headRole",
        "lastActivity",
        "projectsInfos",
        "enable",
        "links",
        "last_name"
      ]
    }
  },
  "required": [
    "timestamp",
    "success",
    "token",
    "data"
  ]
}

account_info = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "timestamp": {
      "type": "string"
    },
    "success": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "middleName": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "timezoneOffset": {
          "type": "integer"
        },
        "active": {
          "type": "boolean"
        },
        "approvedByOrganization": {
          "type": "boolean"
        },
        "roles": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                }
              },
              "required": [
                "name"
              ]
            }
          ]
        },
        "email": {
          "type": "string"
        },
        "organizationName": {
          "type": "string"
        },
        "organizationId": {
          "type": "integer"
        },
        "employment": {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name"
          ]
        },
        "headRole": {
          "type": "string"
        },
        "lastActivity": {
          "type": "string"
        },
        "projectsInfos": {
          "type": "array",
          "items": {}
        },
        "enable": {
          "type": "boolean"
        },
        "links": {
          "type": "array",
          "items": {}
        },
        "last_name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name",
        "middleName",
        "timezone",
        "timezoneOffset",
        "active",
        "approvedByOrganization",
        "roles",
        "email",
        "organizationName",
        "organizationId",
        "employment",
        "headRole",
        "lastActivity",
        "projectsInfos",
        "enable",
        "links",
        "last_name"
      ]
    }
  },
  "required": [
    "timestamp",
    "success",
    "data"
  ]
}

account_edit = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "timestamp": {
      "type": "string"
    },
    "success": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "middleName": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "timezoneOffset": {
          "type": "integer"
        },
        "active": {
          "type": "boolean"
        },
        "approvedByOrganization": {
          "type": "boolean"
        },
        "roles": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                }
              },
              "required": [
                "name"
              ]
            }
          ]
        },
        "email": {
          "type": "string"
        },
        "organizationName": {
          "type": "string"
        },
        "organizationId": {
          "type": "integer"
        },
        "employment": {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name"
          ]
        },
        "headRole": {
          "type": "string"
        },
        "lastActivity": {
          "type": "string"
        },
        "projectsInfos": {
          "type": "array",
          "items": {}
        },
        "enable": {
          "type": "boolean"
        },
        "links": {
          "type": "array",
          "items": {}
        },
        "last_name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name",
        "middleName",
        "timezone",
        "timezoneOffset",
        "active",
        "approvedByOrganization",
        "roles",
        "email",
        "organizationName",
        "organizationId",
        "employment",
        "headRole",
        "lastActivity",
        "projectsInfos",
        "enable",
        "links",
        "last_name"
      ]
    }
  },
  "required": [
    "timestamp",
    "success",
    "data"
  ]
}