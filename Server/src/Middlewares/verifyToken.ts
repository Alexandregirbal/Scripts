import HttpException from "Exceptions/http.exceptions";
import { Request, Response, NextFunction } from "express";
require('dotenv').config()
const jwt = require('jsonwebtoken');

export default async (req: Request, res: Response, next: NextFunction) => {  
    try {
        const token: string = req.headers.authorization?.split(' ')[1] as string
        try {
            const decoded = jwt.verify(token , process.env.TOKEN_SECRET)
            req.token = decoded;
            return next();
            
        } catch (error) {
            console.info('Error name: ',error.name);
            let httpError = new HttpException(401,"Authentication token error")
            if (error.name === 'TokenExpiredError'){
                //use var because function scope needed for this case
                httpError = new HttpException(401,"Token expired")
            }            
            return next(httpError)
        }
    } catch (error) {
        return next(new HttpException());
    }
};
