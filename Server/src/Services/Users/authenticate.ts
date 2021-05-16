const jwt = require('jsonwebtoken');
import {TOKEN} from '../../config'
import { UserCredentials, UserData } from './interfaces';

const mockUserData = (credentials:UserCredentials) => {
    //call to db
    if (credentials.email === 'alexandre.girbal.pro@gmail.com' && credentials.password === 'Test123') {
        return  {
            firstname: "Alexandre",
            lastname: "Girbal",
            email: "alexandre.girbal.pro@gmail.com",
            company: "Lox",
            accessRights: [],
            admin: true,
        }
    } else {
        return undefined
    }
}

export default async (credentials:UserCredentials):Promise<string> => {
    let userData: UserData | undefined = mockUserData(credentials)
    if (!userData) {
        return ''
    } else {
        const token = jwt.sign({
            user: userData
          }, TOKEN.secret, { expiresIn: '1h' });
        return token
    }
}