import express, { Request, Response, NextFunction } from "express";
const router = express.Router({ mergeParams: true });
import publicRoutes from './public'
import privateRoutes from './private'
import verifyToken from 'Middlewares/verifyToken'
import HttpException from "Exceptions/http.exceptions";

router.use("/public", publicRoutes);
router.use("/private", verifyToken, privateRoutes);
router.get("*", (req: Request, res: Response)=>{
    return res.status(201).send({message: "You need to choose a path between public or private API."})
})
//'next' parameter is important - don't know why
router.use((error: HttpException, req: Request, res: Response, next: NextFunction) => {
    return res
    .status(error.status)
    .send({ message: error.message });
  });
  

export default router;