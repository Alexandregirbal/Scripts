import { Request, Response } from "express";
const jwt = require('jsonwebtoken');
import {TOKEN} from '../../../config'

export default async (req: Request, res: Response) => {
    const data = {firstname: req.query.firstname, lastname: req.query.lastname, company: req.query.company}
    const token = jwt.sign({
        user: data
      }, TOKEN.secret, { expiresIn: '1h' });
    
    return res.status(200).send({
        token
    })
}