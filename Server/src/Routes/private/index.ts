import express, { Request, Response } from "express";
const router = express.Router({ mergeParams: true });
import userRoutes from "./User";
import adminRoutes from "./Admin";
import thirdPartyRoutes from "./ThirdParty";
import verifyAdmin from "Middlewares/verifyAdmin";
import verifyThirdParty from "Middlewares/verifyThirdParty";

router.get("/", (req: Request, res: Response) => {
    return res.status(201).send({message: "Welcome into the private API."});
})
router.use("/user", userRoutes);
router.use("/admin",verifyAdmin, adminRoutes);
router.use("/thirdParty",verifyThirdParty, thirdPartyRoutes);

export default router;