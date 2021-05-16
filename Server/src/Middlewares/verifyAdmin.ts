import { Request, Response, NextFunction } from "express";
import HttpException from "Exceptions/http";

export default async (req: Request, res: Response, next: NextFunction) => {
    if (req.user.admin){
        return next();
    }
    else {
        return next(new HttpException(403, "Admin only have access to this route"));
    }
}