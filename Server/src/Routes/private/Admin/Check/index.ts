import { Request, Response } from "express";

export default async (req: Request, res: Response) => {
    const tokenData = req.token
    console.log("Welcome to admin");
    
    return res.status(200).send(req.token)
}