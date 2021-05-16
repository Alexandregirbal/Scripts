import { Request, Response } from "express";
import { UserDataToken } from "interfaces";
import createAPIKey from "Services/ThirdParties/createAPIKey";
import { APIKey } from "Services/ThirdParties/interfaces";

export default async (req: Request, res: Response) => {
    const apiKey: APIKey | undefined = await createAPIKey((req.decodedToken as UserDataToken).user);
    return res.status(200).send({key: apiKey});
}