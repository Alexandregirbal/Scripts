import { Request, Response, NextFunction } from "express";
import HttpException from "Exceptions/http";
import { isAPIKey } from "Services/ThirdParties/interfaces";
import { APIKeyToken } from "interfaces";

export default async (req: Request, res: Response, next: NextFunction) => {
    if (isAPIKey((req.decodedToken as APIKeyToken).key)) {
        return next();
    }
    else {
        return next(new HttpException(403, "Only authorized third parties have access to this API."));
    }
}