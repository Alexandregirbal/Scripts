import "module-alias/register";
import express from "express";
import { Request, Response, NextFunction } from "express";
import routes from './Routes'

const app = express()
const port = process.env.port || 10000

app.use(function (req: Request, res: Response, next: NextFunction) {
  console.info('Call to API: ', req.url);
  return next()
})
app.get('/', (req: Request, res: Response) => {
  return res.send('Welcome in this API !')
})
app.use("/api", routes);

app.use("*", function (req: Request, res: Response) {
    return res.status(404).send({message: "End point not available."});
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}...`)
})