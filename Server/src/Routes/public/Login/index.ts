import { Request, Response } from "express";

import authenticate, {Credentials} from 'Services/Users/authenticate'

export default async (req: Request, res: Response) => {
    const query = {...req.query} as Credentials
    const token = await authenticate(query)
    
    return res.status(200).send({
        token
    })
}