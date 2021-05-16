import { UserData } from "Services/Users/interfaces";
import { TOKEN } from '../../config';
import { APIKey } from "./interfaces";
const jwt = require('jsonwebtoken');

export default async (user: UserData): Promise<APIKey|undefined> => {
    //verify in db that has access to API and then continue
    if (true){
        const key: APIKey = {
            type: "Third party",
            company: user.company
        }
        const token = jwt.sign({
            key
          }, TOKEN.secret, { expiresIn: '1d' });
        // return token
        return token
    }
}