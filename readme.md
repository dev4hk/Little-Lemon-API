# Restaurant API Documentation

## Overview

This documentation provides an overview of the endpoints available in the Little Lemon Restaurant API, including routes for managing bookings and menu items. It also includes example JSON requests.

## Endpoints

### Booking Endpoints

The booking endpoints allow you to create, retrieve, update, and delete booking information.

- **List all bookings:** `GET /restaurant/booking/tables/`

- **Retrieve a single booking** `GET /restaurant/booking/tables/{id}/`

- **Create a new booking** `POST /restaurant/booking/tables/`

```json
{
  "name": "John Doe",
  "no_of_guests": 4,
  "booking_date": "2024-11-24T18:00:00Z"
}
```

- **Update a booking** `PUT /restaurant/booking/tables/{id}/`

```json
{
  "name": "John Doe",
  "no_of_guests": 5,
  "booking_date": "2024-11-24T19:00:00Z"
}
```

- **Delete a booking** `DELETE /restaurant/booking/tables/{id}/`

## Menu Item Endpoints

The menu item endpoints allow you to create, retrieve, update, and delete menu items.

- **List all menu items** `GET /restaurant/menu-items/`

- **Retrieve a single menu item** `GET /restaurant/menu-items/{id}`

- **Create a new menu item** `POST /restaurant/menu-items/`

```json
{
  "title": "Pasta",
  "price": 7.99,
  "inventory": 15
}
```

- **Update a menu item** `PUT /restaurant/menu-items/{id}/`

```json
{
  "title": "Pasta",
  "price": 8.99,
  "inventory": 10
}
```

- **Delete a menu item** `DELETE /restaurant/menu-items/{id}/`

## Authentication Endpoints

The API uses token-based authentication. ```NOTE: As per the project requirement, in order to create an user, please visit the admin panel and create a user from there```

- **Retrieve a user token** `GET /restaurant/api-token-auth/`

```json
{
  "username": "YOUR_USERNAME",
  "password": "YOUR_PASSWORD"
}
```
