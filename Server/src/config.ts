require('dotenv').config()

export const PORT = process.env.PORT;

export const TOKEN = {secret: process.env.TOKEN_SECRET};