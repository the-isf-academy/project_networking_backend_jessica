# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
My API  is  a color palette generator.

You can:

Add a new palette - new

Like palettes

Edit existing palettes

Search up palette through keywords

### Model
| Model |     |
|-------|-----|
| id    | int |
| hex1  | str |
| hex2  | str |
| hex3  | str |
| hex4  | str |
| likes | int |

| Method         | Parameter                |
|----------------|--------------------------|
| increase_likes | self                     |
| change_palette | self,hex1,hex2,hex3,hex4 |
| json_responce  | self                     |


### Endpoints
| route name | HTTP method | payload                |
|------------|-------------|------------------------|
| all        | get         | none                   |
| new        | post        | hex1,hex2,hex3,hex4    |
| likes      | post        | id                     |
| edit       | post        | id,hex1,hex2,hex3,hex4 |
| search     | post        | keyword                |

## Setup

### Contentsi

Here's what is included:
- `\app`
    - `models.py` - `Fortune` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/)



