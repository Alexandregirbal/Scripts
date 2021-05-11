import express, { Request, Response } from "express";
const router = express.Router({ mergeParams: true });
import user from "./User";
import adminRoutes from "./Admin";
import verifyAdmin from "Middlewares/verifyAdmin";

router.get("/", (req: Request, res: Response) => {
    return res.status(201).send({message: "Welcome into the private API."});
})
router.get("/user", user);
router.use("/admin",verifyAdmin, adminRoutes);

export default router;