import express, { Request, Response } from "express";
const router = express.Router({ mergeParams: true });
import generateApiKey from '../User/GenerateAPIKey'

router.get("/", (req: Request, res: Response) => {
    return res.status(201).send({message: "Welcome to the user API."});
})
router.get("/generateApiKey", generateApiKey);

export default router;