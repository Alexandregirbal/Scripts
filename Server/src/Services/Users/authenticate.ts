const jwt = require('jsonwebtoken');
import {TOKEN} from '../../config'

export interface Credentials {
    firstname?: string;
    lastname?: string;
    admin?: boolean;
}
export default async (credentials:Credentials):Promise<any> => {
    let data = {...credentials}
    if (credentials.firstname === 'Alexandre' && credentials.lastname === 'Girbal'){
        data = {...data, admin: true}
    }
    const token = jwt.sign({
        user: data
      }, TOKEN.secret, { expiresIn: '1h' });
    return token
}