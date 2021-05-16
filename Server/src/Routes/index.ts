import express, { Request, Response, NextFunction } from "express";
const router = express.Router({ mergeParams: true });
import publicRoutes from './public'
import privateRoutes from './private'
import verifyToken from 'Middlewares/verifyToken'

router.use("/public", publicRoutes);
router.use("/private", verifyToken, privateRoutes);
router.get("*", (req: Request, res: Response)=>{
    return res.status(201).send({message: "You need to choose a path between public or private API."})
})  

export default router;