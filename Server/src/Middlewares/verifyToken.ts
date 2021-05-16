import HttpException from "Exceptions/http";
import { Request, Response, NextFunction } from "express";
import decodeToken from 'Services/JsonWebToken/decode'
const memoize = require('fast-memoize')
const sleep = (milliseconds: number) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
  }

const memo_decodeToken = memoize(decodeToken)

export default async (req: Request, res: Response, next: NextFunction) => {
    try {
        const token: string = req.headers.authorization?.split(' ')[1] as string
        try {
            const decoded = await memo_decodeToken(token)
            req.decodedToken = decoded;
            return next();
            
        } catch (error) {
            console.info('Error name: ', error.name);
            let httpError = new HttpException(401,"Authentication token error")
            if (error.name === 'TokenExpiredError'){
                httpError = new HttpException(401,"Token expired")
            }            
            return next(httpError)
        }
    } catch (error) {
        return next(new HttpException());
    }
};
