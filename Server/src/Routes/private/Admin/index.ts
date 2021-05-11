import express, { Request, Response } from "express";
const router = express.Router({ mergeParams: true });
import check from './Check'

router.get("/", (req: Request, res: Response) => {
    return res.status(201).send({message: "Welcome to the admin API."});
})
router.get("/check", check);

export default router;