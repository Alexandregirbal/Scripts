require('dotenv').config()
import "module-alias/register";
import express, { Request, Response, NextFunction } from "express";
import routes from './Routes'
import {PORT} from './config'
import HttpException from "Exceptions/http";
import moment from 'moment';

const app = express()
const port = PORT || 5000

app.use((req: Request, res: Response, next: NextFunction) => {
  const summary = {
    method: req.method,
    url: req.path,
    params: req.params,
    query: req.query,
    body: req.body,
  }
  console.info(moment().format('LLL'), summary);
  return next()
})
app.get('/', (req: Request, res: Response) => {
  return res.send('Welcome in this API !')
})
app.use("/api", routes);
app.use((error: HttpException, req: Request, res: Response, next: NextFunction) => {
  return res
  .status(error.status)
  .send({ message: error.message });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}...`)
})