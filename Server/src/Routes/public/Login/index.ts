import { Request, Response } from "express";

import authenticate from 'Services/Users/authenticate'
import { UserCredentials } from "Services/Users/interfaces";

export default async (req: Request, res: Response) => {
    const query = {...req.query} as UserCredentials
    const token = await authenticate(query)
    
    return res.status(200).send({
        token
    })
}