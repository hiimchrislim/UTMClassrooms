# UTMClassrooms
JSON representation of classrooms and schedules at UTM stored using MongoDB

## Table of Contents
- [Requirements](#requirements)
- [Usage](#usage)
- [Room Format](#room-format)

## Usage
Run scraper.py and then run filter.py\
Put in your username and password for your Mongo Database\
```mongodb+srv://<USERNAME?:<PASSWORD>@utm-o7d7p.mongodb.net/test?retryWrites=true&w=majority```

## Requirements
- uoftscrapers
- pymongo

## Room Format
```js
{
  "_id": ObjectID
  "room": String,
  "classes": [{
    "course_code": String,
    "name": String,
    "lec_code": String
    "times": [{
      "day": String,
      "start": Integer,
      "end": Integer,
      "duration": Integer
    }]
  }]
}
```
