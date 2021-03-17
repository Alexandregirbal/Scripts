import express, { Request, Response } from "express";
const router = express.Router({ mergeParams: true });
import login from "./Login";

router.get("/", function (req: Request, res: Response) {
    return res.status(201).send({message: "Welcome into the public API."});
})
router.get("/login", login);

export default router;