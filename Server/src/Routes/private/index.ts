import HttpException from "Exceptions/http.exceptions";
import express, { NextFunction, Request, Response } from "express";
const router = express.Router({ mergeParams: true });
import user from "./User";

router.get("/", (req: Request, res: Response) => {
    return res.status(201).send({message: "Welcome into the private API."});
})
router.get("/user", user);

export default router;