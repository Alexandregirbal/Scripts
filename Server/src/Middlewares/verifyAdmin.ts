import { Request, Response, NextFunction } from "express";
import HttpException from "Exceptions/http";
const isAdmin  = (object: any) => {
    return object.user?.admin === true
}
export default async (req: Request, res: Response, next: NextFunction) => {
    if (isAdmin(req.decodedToken)){
        return next();
    }
    else {
        return next(new HttpException(403, "Admin only have access to this route"));
    }
}