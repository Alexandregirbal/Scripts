import express, { Request, Response } from "express";
const router = express.Router({ mergeParams: true });
import user from "./User";

router.get("/", function (req: Request, res: Response) {
    res.status(201).send({message: "Welcome into the private API."});
})
router.get("/user", user);

export default router;