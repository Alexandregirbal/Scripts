import { Request, Response } from "express";
const jwt = require('jsonwebtoken');
const SALT = 'qwertyuiopasdfghjklzxcvbnm123456'

export default async (req: Request, res: Response) => {
    console.log(req.query);
    const data = {firstname: req.query.firstname, lastname: req.query.lastname, company: req.query.company}
    const token = jwt.sign({
        user: data
      }, SALT, { expiresIn: '1h' });
    
    return res.status(200).send({
        token
    })
}