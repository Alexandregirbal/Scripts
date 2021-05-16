import { APIKeyToken, UserDataToken } from "interfaces";
import {TOKEN} from '../../config'
export default async (token?: string): Promise<UserDataToken | APIKeyToken> => {
    try{
        const jwt = require('jsonwebtoken');
        const decoded = jwt.verify(token , TOKEN.secret)
        // await sleep(1000) verify that user exists, admin rights, ...
        return decoded
    } catch(error) {
        throw error
    }
}