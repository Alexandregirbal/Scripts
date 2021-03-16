import { Request, Response, NextFunction } from "express";
const jwt = require('jsonwebtoken');
const SALT = 'qwertyuiopasdfghjklzxcvbnm123456'
export default async (req: Request, res: Response, next: NextFunction) => {
    try {
        const token: string = req.headers.authorization?.split(' ')[1] as string
        try {
            const decoded: any = jwt.verify(token , SALT);
            req.user = decoded;
          } catch(err) {
            // err
            return res.status(400).send({message: 'Wrong token.'})
          }
        return next();
    } catch (error) {
        console.error(error);
        return next();
    }
};
