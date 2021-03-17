require('dotenv').config()
import "module-alias/register";
import express, { Request, Response, NextFunction } from "express";
import routes from './Routes'
import {PORT} from './config'

const app = express()
const port = PORT || 5000

app.use((req: Request, res: Response, next: NextFunction) => {
  console.info('Call to API: ', req.url);
  return next()
})
app.get('/', (req: Request, res: Response) => {
  return res.send('Welcome in this API !')
})
app.use("/api", routes);

app.listen(port, () => {
  console.log(`Server listening on port ${port}...\n`)
})