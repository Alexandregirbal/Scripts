import { Request, Response } from "express";

import authenticate from 'Services/Users/authenticate'
import { UserSignupData } from "Services/Users/interfaces";

export default async (req: Request, res: Response) => {
    const query = {...req.query} as unknown as UserSignupData
    const token = await authenticate(query)
    
    return res.status(200).send({
        token
    })
}